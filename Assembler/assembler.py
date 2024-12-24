from os import read


def convertBinToHex(bin):
    hexval = hex(int(bin, 2))[2:]
    return hexval


def convertOpcode(op):
    opcodeDict = {
        "srl": "0000",
        "bne": "0001",
        "add": "0000",
        "or": "0000",
        "beq": "0010",
        "nor": "0000",
        "nop": "0011",
        "addi": "0100",
        "lw": "0101",
        "and": "0000",
        "j": "0111",
        "sub": "0000",
        "sll": "0000",
        "slt": "0000",
        "sw": "0110",
    }
    return opcodeDict[op]


def convertFunctionBits(funcBits):
    functionDict = {
        "srl": "000",
        "add": "001",
        "or": "010",
        "nor": "011",
        "and": "100",
        "sub": "101",
        "sll": "110",
        "slt": "111",
    }
    return functionDict[funcBits]


def checkRegister(reg):
    registerNum = int(reg[1:])
    if registerNum > 21:
        print("Invalid register")
    return format(registerNum, "05b")


rtypeInstructions = [
    "srl",
    "and",
    "or",
    "nor",
    "add",
    "sub",
    "sll",
    "slt",
]

itypeInstructions = [
    "bne",
    "beq",
    "addi",
    "lw",
    "sw",
]
# addi, r3, r0, 6
# j, 7
readf = open("inputs.txt", "r")
writef = open("outputs.raw", "w")
writef.write("v2.0 raw\n")
for _ in readf:
    splitted = _.strip().split(',')

    if splitted[0] in rtypeInstructions:
        opcode = convertOpcode(splitted[0])
        funcBits = convertFunctionBits(splitted[0])
        rs = checkRegister(splitted[2])
        rt = checkRegister(splitted[3])
        rd = checkRegister(splitted[1])
        out = opcode + rs + rt + rd + funcBits
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    elif splitted[0] == "nop":
        out = "0000000000000000000000"
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    elif splitted[0] in itypeInstructions:
        opcode = convertOpcode(splitted[0])
        rs = checkRegister(splitted[2])
        rt = checkRegister(splitted[1])
        im = format(int(splitted[3]), "08b")
        out = opcode + rs + rt + im
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    elif splitted[0] == "j":
        opcode = convertOpcode(splitted[0])
        target = format(int(splitted[1]), "018b")
        out = opcode + target
        print(out)
        writef.write(convertBinToHex(out) + "\n")

    print(_)
