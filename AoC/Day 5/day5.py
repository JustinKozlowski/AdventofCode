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
	return 1


def run(intCode):
	intLen = len(intCode)
	state = "op"
	operation = "mult"
	int1 = 0
	int2 = 0
	out = ""
	paramlist = [0, 0, 0, 0]
	for num in intCode:
		print(num)
		if state == "op":
			paramlist = parseOpCode(int(num))
			if paramlist[0] == 01:
				operation = "add"
			if paramlist[0] == 02:
				operation = "mult"
			if paramlist[0] == 03:
				operation = "in"
			if paramlist[0] == 04:
				operation = "out"
			if paramlist[0] == "99":
				print("exit")
			if operation == "mult" or operation == "add":
				state = "int1"
			else:
				state = "out"
			continue
		if state == "int1":
			if int(num) >= intLen:
				print("out of range in state=out")
				break
			int1 = getVal(paramlist[1], int(num), intCode)
			state = "int2"
			continue
		if state == "int2":
			if int(num) >= intLen:
				print("out of range in state=out")
				break
			int2 = getVal(paramlist[2], int(num), intCode)
			state = "out"
			continue
		if state == "out":
			if int(num) >= intLen:
				print("out of range in state=out")
				break
			if operation == "add":
				intCode[int(num)] = int1 + int2
			if operation == "mult":
				intCode[int(num)] = int1 * int2
			if operation == "in":
				intCode[int(num)] = codeinput()
			if operation == "out":
				print("output: " + str(intCode[int(num)]))
			state = "op"
			continue


def parse(filename):
	with open(filename) as csvfile:
		spamreader = csv.reader(csvfile)
		for x in spamreader:
			return x
			

if __name__ == '__main__':
	out = parse("day5.csv")
	print("parsed")
	run(out)
	print("Diagnostics complete")
