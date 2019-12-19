import csv

def parse(filename):
	with open(filename) as csvfile:
		reader = csv.reader(csvfile)
		for x in reader:
			return x


def pathToMap(x, y, dir, num, map):
	for step in range(num):
		map["dist"] = map["dist"] + 1
		if dir == 1:
			y = y + 1
		if dir == -1:
			y = y - 1
		if dir == 2:
			x = x + 1
		if dir == -2:
			x = x - 1
		map[(str(x) + "~" + str(y))] = map["dist"]
	if dir == 1 or dir == -1:
		return y
	else:
		return x


if __name__ == '__main__':
	line1 = parse("line1.csv")
	line2 = parse("line2.csv")
	list1 = {"dist": 0}
	xcord = 0
	ycord = 0
	for path in line1:
		if path[0] == "U":
			num = int(path[1:])
			ycord = pathToMap(xcord, ycord, 1, num, list1)
		if path[0] == "D":
			num = int(path[1:])
			ycord = pathToMap(xcord, ycord, -1, num, list1)
		if path[0] == "R":
			num = int(path[1:])
			xcord = pathToMap(xcord, ycord, 2, num, list1)
		if path[0] == "L":
			num = int(path[1:])
			xcord = pathToMap(xcord, ycord, -2, num, list1)
	print("line1 created: dist = " + str(list1["dist"]))
	list2 = {"dist": 0}
	xcord = 0
	ycord = 0
	for path in line2:
		if path[0] == "U":
			num = int(path[1:])
			ycord = pathToMap(xcord, ycord, 1, num, list2)
		if path[0] == "D":
			num = int(path[1:])
			ycord = pathToMap(xcord, ycord, -1, num, list2)
		if path[0] == "R":
			num = int(path[1:])
			xcord = pathToMap(xcord, ycord, 2, num, list2)
		if path[0] == "L":
			num = int(path[1:])
			xcord = pathToMap(xcord, ycord, -2, num, list2)
	print("line2 created")
	outmap = {}
	for a in list1:
		if a in list2:
			outmap[a] = True
	min = 0
	print("intersect created")
	for intersect in outmap:
		#print(intersect)
		if intersect == "dist":
			continue
		nums = intersect.split("~")
		#print("nums 0 =" + str(nums[0]))
		#print("nums 1 =" + str(nums[1]))
		dist = list1[intersect] + list2[intersect]
		#print(dist)
		if min == 0:
			min = dist
		elif dist < min:
			min = dist
	print(min)

