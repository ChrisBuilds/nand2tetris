with open("pong\Pong.asm") as f:
    code = [l.strip() for l in f.readlines() if l.strip() and not l.startswith("//")]


def remove_ignored_lines(code):
    """
    Remove all comments from the code.

    :param code: The assembly code to be cleaned
    :return: The list of assembly instructions.
    """
    assembly_instructions = []
    for assembly_inst in code:
        if "//" in assembly_inst:
            assembly_inst = assembly_inst[: assembly_inst.index("//")].strip()
        if assembly_inst:
            assembly_instructions.append(assembly_inst)
    return assembly_instructions


def find_labels(assembly_instructions):
    """
    Given a list of assembly instructions, return a dictionary of labels and their corresponding line
    numbers and return the list of instructions without the labels.

    :param assembly_instructions: A list of assembly instructions
    :return: The symbols and instructions
    """
    symbols = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "R0": 0,
        "R1": 1,
        "R2": 2,
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 8,
        "R9": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SCREEN": 16384,
        "KBD": 24576,
    }
    instructions = []
    labels_found = 0
    for line, inst in enumerate(assembly_instructions):
        if inst.startswith("("):
            label = inst.strip("()")
            # line number is reduced by number of lables found since the label is removed from the instructions
            if label not in symbols:
                symbols[label] = line - labels_found
            labels_found += 1
        else:
            instructions.append(inst)
    return symbols, instructions


def parse_instructions(assembly_instructions, symbols):
    """
    Given a list of assembly instructions, return a list of machine code instructions.

    :param assembly_instructions: A list of assembly instructions
    :param symbols: a dictionary of symbols and their values
    :return: A list of machine code strings.
    """
    dest_trans = {
        "null": "000",
        "M": "001",
        "D": "010",
        "MD": "011",
        "A": "100",
        "AM": "101",
        "AD": "110",
        "AMD": "111",
    }
    comp_trans = {
        "0": "101010",
        "1": "111111",
        "-1": "111010",
        "D": "001100",
        "A": "110000",
        "!D": "001101",
        "!A": "110001",
        "-D": "001111",
        "-A": "110011",
        "D+1": "011111",
        "A+1": "110111",
        "D-1": "001110",
        "A-1": "110010",
        "D+A": "000010",
        "D-A": "010011",
        "A-D": "000111",
        "D&A": "000000",
        "D|A": "010101",
        "M": "110000",
        "!M": "110001",
        "-M": "110011",
        "M+1": "110111",
        "M-1": "110010",
        "D+M": "000010",
        "D-M": "010011",
        "M-D": "000111",
        "D&M": "000000",
        "D|M": "010101",
    }
    jump_trans = {
        "null": "000",
        "JGT": "001",
        "JEQ": "010",
        "JGE": "011",
        "JLT": "100",
        "JNE": "101",
        "JLE": "110",
        "JMP": "111",
    }
    ram_address = 16
    machine_code = []
    for inst in assembly_instructions:
        dest = "null"
        comp = "null"
        jump = "null"
        # A-instruction
        if inst.startswith("@"):
            value = inst[1:]
            if value.isnumeric():
                # leading 0 for A-instruction, convert value to binary
                # and take lower 15 bits, zfill if required
                binary = "0" + bin(int(value))[2:][-15:].zfill(15)
            else:
                # add symbol to table with next available ram address
                if value not in symbols:
                    symbols[value] = ram_address
                    ram_address += 1
                binary = "0" + bin(int(symbols[value]))[2:][-15:].zfill(15)
            machine_code.append(binary)
            continue
        # C-instruction
        else:
            if "=" in inst:
                dest = inst.split("=")[0]
                # get comp
                comp = inst.split("=")[1].split(";")[0]
            if ";" in inst:
                jump = inst.split(";")[1]
                if not jump:
                    jump = "null"
                # get comp if not already found
                if comp == "null":
                    comp = inst.split(";")[0]
            if not comp:
                print("comp not found: " + inst)
            a = str(int("M" in comp))
            comp = a + comp_trans[comp]
            dest = dest_trans[dest]
            jump = jump_trans[jump]
            binary = f"111{comp}{dest}{jump}"
            machine_code.append(binary)
    return machine_code


assembly_instructions = remove_ignored_lines(code)
symbols, assembly_instructions = find_labels(assembly_instructions)
machine_code = parse_instructions(assembly_instructions, symbols)

with open("Pong.hack", "w+") as f:
    f.writelines([l + "\n" for l in machine_code])
