import math

def calc(num):
	num = num / 3
	num = math.floor(num)
	num = num - 2
	return num


def parse(filename):
	file = open(filename)
	output = 0
	for line in file:
		num = int(line)
		extra = calc(num)
		while(extra > 0):
			output = output + extra
			extra = calc(extra)
	return output


if __name__ == '__main__':
	out = parse("test.txt")
	print(out)