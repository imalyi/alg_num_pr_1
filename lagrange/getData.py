class GetData():
	def getData(self):
		data = []
		try:
			f = open("./data.txt")
		except FileNotFoundError:
			print("PLik nie istnieje!")
			exit()
		lines = f.readlines()
		for x in range(len(lines)):
			arg = lines[x].split()
			data.append([int(arg[0]),int(arg[1])])
		return data

