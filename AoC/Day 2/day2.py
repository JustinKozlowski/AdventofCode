import csv

def parse(filename):
	with open(filename) as csvfile:
		spamreader = csv.reader(csvfile)
		for x in spamreader:
			state = "op"
			operation = "mult"
			int1 = 0
			int2 = 0
			out = ""
			for a in range(100):
				for b in range(100):
					start = []
					for y in x:
						start.append(y)
					start[1] = str(b)
					start[2] = str(a)
					for num in start:
						if state == "op":
							if num == "1":
								operation = "add"
							if num == "2":
								operation = "mult"
							if num == "99":
								if int(a) == 2 and int(b) == 12:
									print(start[0])
								if (19690720 == start[0]):
									return (100*a + b)
							state = "int1"
							continue
						if state == "int1":
							if int(num) > 165:
								break
							int1 = int(start[int(num)])
							state = "int2"
							continue
						if state == "int2":
							if int(num) > 165:
								break
							int2 = int(start[int(num)])
							state = "out"
							continue
						if state == "out":
							if int(num) > 165:
								break
							if operation == "add":
								start[int(num)] = int1 + int2
							if operation == "mult":
								start[int(num)] = int1 * int2
							state = "op"
							continue


if __name__ == '__main__':
	out = parse("day2.csv")
	print(out)