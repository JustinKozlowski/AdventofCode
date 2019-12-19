import csv


def getVal(opCode, num, intCode):
    if opCode == "p":
        return int(intCode[num])
    if opCode == "i":
        return num


def parseOpCode(incode):
    paramList = [0, 0, 0, 0]
    incode = incode - 10000
    if incode >= 0:
        paramList[3] = "i"
    else:
        paramList[3] = "p"
        incode = incode + 10000
    incode = incode - 1000
    if incode >= 0:
        paramList[2] = "i"
    else:
        paramList[2] = "p"
        incode = incode + 1000
    incode = incode - 100
    if incode >= 0:
        paramList[1] = "i"
    else:
        paramList[1] = "p"
        incode = incode + 100
    paramList[0] = incode
    return paramList


def codeoutput():
    print("out")


def codeinput():
    return 5


def run(intCode):
    intLen = len(intCode)
    state = "op"
    operation = "mult"
    int1 = 0
    int2 = 0
    out = ""
    paramlist = [0, 0, 0, 0]
    nextnum = 0
    while nextnum < intLen:
        num = int(intCode[nextnum])
        nextnum += 1
        if state == "op":
            paramlist = parseOpCode(int(num))
            if paramlist[0] == 1:
                operation = "add"
            if paramlist[0] == 2:
                operation = "mult"
            if paramlist[0] == 3:
                operation = "in"
            if paramlist[0] == 4:
                operation = "out"
            if paramlist[0] == 5:
                state = "jumpt"
                continue
            if paramlist[0] == 6:
                state = "jumpf"
                continue
            if paramlist[0] == 7:
                operation = "lesst"
            if paramlist[0] == 8:
                operation = "equals"
            if paramlist[0] == 99:
                print("exit")
                break
            if operation == "in" or operation == "out":
                state = "out"
            else:
                state = "int1"
            continue
        if state == "int1":
            int1 = getVal(paramlist[1], int(num), intCode)
            state = "int2"
            continue
        if state == "int2":
            int2 = getVal(paramlist[2], int(num), intCode)
            state = "out"
            continue
        if state == "jumpt":
            if int(num) > 0:
                state = "jumpto"
                continue
            else:
                state = "out"
                continue
        if state == "jumpf":
            if int(num) == 0:
                state = "jumpto"
                continue
            else:
                state = "out"
                continue
        if state == "jumpto":
            state = "op"
            nextnum = int(num)
            continue
        if state == "out":
            if operation == "add":
                intCode[int(num)] = int1 + int2
            if operation == "mult":
                intCode[int(num)] = int1 * int2
            if operation == "in":
                intCode[int(num)] = codeinput()
            if operation == "out":
                print("output: " + str(intCode[int(num)]))
            if operation == "lesst":
                if int1 < int2:
                    intCode[int(num)] = 1
                else:
                    intCode[int(num)] = 0
            if operation == "equals":
                if int1 == int2:
                    intCode[int(num)] = 1
                else:
                    intCode[int(num)] = 0
            state = "op"
            continue


def parse(filename):
    with open(filename) as csvfile:
        spamreader = csv.reader(csvfile)
        for x in spamreader:
            return x


if __name__ == '__main__':
    out = parse("day5p2.csv")
    print("parsed")
    run(out)
    print("Diagnostics complete")
