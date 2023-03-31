class GetData():
	def getData():
	    data = []
	    f = open("./data.txt")
	    lines = f.readlines()
	    for x in range(len(lines)):
		    arg = lines[x].split()
		    data.append([int(arg[0]),int(arg[1])])
	    return data

