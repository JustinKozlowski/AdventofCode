def testPassword(password):
	lastChar = 0
	lockFilter = False
	filter1 = False
	filter2 = False
	tempFilter = False
	for c in password:
		if not lockFilter:
			if c != lastChar and filter1:
				lockFilter = True
			if c != lastChar:
				tempFilter = False
			if tempFilter:
				filter1 = False
			if c == lastChar and not tempFilter:
				filter1 = True
				tempFilter = True
		if c < lastChar:
			filter2 = True
		lastChar = c
	if filter1 and not filter2:
		print(password)
		return True
	else:
		return False


if __name__ == '__main__':
	base = 183564
	count = 0
	altShift = 0
	for shift in range(473911):
		password = str(base + shift)
		if testPassword(password):
			count = count + 1
	print(count)
			
