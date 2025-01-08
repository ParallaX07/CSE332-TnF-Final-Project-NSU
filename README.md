# CSE332 TnF Final Project NSU
 Final project to design a 22-Bit MIPS ISA for CSE332 course from NSU under TnF

## Objective
The objective of the project is to design and implement a complete datapath and control unit capable of automatically executing a set of 15 instructions defined by the assigned 22-bit Instruction Set Architecture (ISA). The goal is to ensure seamless execution of instructions stored in memory by integrating the datapath and control units effectively, enabling the CPU to process instructions in a sequential manner.

## ISA Design
There are 3 instruction formats:
- R-Type
-I-Type
-J-Type


### R-Type
| Field          | Opcode | Rs   | Rt   | Rd   | Function Bits |
|----------------|--------|------|------|------|---------------|
| **Bit Width**  | 4 bits | 5 bits | 5 bits | 5 bits | 3 bits      |

### I-Type
| Field          | Opcode | Rs   | Rt   | Immediate Value |
|----------------|--------|------|------|-----------------|
| **Bit Width**  | 4 bits | 5 bits | 5 bits | 8 bits         |

### J-Type
| Field          | Opcode | Address / Target  |
|----------------|--------|--------------------|
| **Bit Width**  | 4 bits | 18 bits           |

# Control Signal Table
| Ins. Format | Instructions | Opcode | Function Bits | ALU Control | Mem To Reg | Reg Write | Mem Write | Mem Read | Branch | Jump | ALU Src | ALU OP | Reg Dest |
|-------------|--------------|--------|---------------|-------------|------------|-----------|-----------|----------|---------|------|---------|---------|-----------|
| R | SRL | 0000 | 000 | 001 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| I | BNE | 0001 | xxx | 110 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 01 | 0 |
| R | ADD | 0000 | 001 | 010 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| R | OR | 0000 | 010 | 011 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| I | BEQ | 0010 | xxx | 110 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 01 | 0 |
| R | NOR | 0000 | 011 | 100 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| I | NOP | 0011 | xxx | 000 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 00 | 0 |
| I | ADDi | 0100 | xxx | 010 | 0 | 1 | 0 | 0 | 0 | 0 | 1 | 00 | 0 |
| I | LW | 0101 | xxx | 010 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 00 | 0 |
| R | AND | 0000 | 100 | 101 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| J | J | 0111 | xxx | xxx | 0 | 0 | 0 | 0 | 0 | 1 | 0 | xx | 0 |
| R | SUB | 0000 | 101 | 110 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| R | SLL | 0000 | 110 | 000 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| R | SLT | 0000 | 111 | 111 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 10 | 1 |
| I | SW | 0110 | xxx | 010 | 0 | 0 | 1 | 0 | 0 | 0 | 1 | 00 | 0 |


#### **Datapath:**
![Datapath](https://i.ibb.co.com/3sfHwN4/datapath.png)
