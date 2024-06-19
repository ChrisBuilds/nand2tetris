# Nand2Tetris

This repo documents my solutions to the nand2tetris course in which students build a fully working computer including
the hardware and software starting from only Nand gates.

The associated website is available here: [From Nand to Tetris](https://www.nand2tetris.org/).

The first part of the course (and this repo) ends after the assembler has been built and the computer successfully executes code written in its assembly language. That code is executed by assembling it down to binary, loading it into memory directly via the hardware emulator, and pointing the program counter at the start. 

## Assembler

The course leaves the implementation of the assembler up to the students. I chose to write it in Python, it can be found [here](https://github.com/ChrisBuilds/nand2tetris/blob/main/projects/06/assembler.py)

## Logic Visualizations

The course includes a custom VHDL and design IDE. However, I also implemented most of the logic structures (up to the
limitations of the visualization software) in Logicly, a visual logic application.

Some of the structures can be seen below.

### Half Adder
![half_adder](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/0aa6e8ed-e1eb-4b7d-84bd-df42be85f0b7)

### Full Adder
![full_adder](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/ed1a8196-d5a9-4ac5-9846-0c1f80836b7a)

### 16-bit Adder
![ADD16](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/4f53b635-9020-4a18-be71-5ffbf2338a4c)

### Arithmetic Logic Unit
![ALU](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/8f83a7f6-f0f3-4899-b7f9-c5cdf56288f1)

### Program Counter
![program_counter](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/013faba9-82fa-4850-847e-2149e67e5e38)

### Full CPU
![cpu_full](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/b2c54fde-7474-4616-a80f-c81c6a77d170)

### 1-bit Register
![1-bit_register](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/83fe1e8e-78af-4920-9d85-0f50f5e91bd5)

### 16-bit Register
![16-bit_register](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/615f6bbd-f796-424d-b7a3-e5977075d525)

### RAM64
![RAM64](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/8e296552-b95e-49a3-ac4c-ba22a6d69cc3)

### RAM64 Package
![RAM64_package](https://github.com/ChrisBuilds/nand2tetris/assets/57874186/0ce7e085-fea4-427e-b98b-6acd163b8083)
