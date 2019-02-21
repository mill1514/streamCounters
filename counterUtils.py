import re
import sys

dic = dict() # Holds values of all counters

def writeStrToFile(s, fname):
	ob = open(fname + ".txt", "w")
	ob.write(str(s))
	ob.close()

# Writes to dictionary and then to text file
def updateValue(s, newVal, printOpt=True):
	global dic
	valids = re.sub(r"[^A-Za-z]+", '', s)

	dic[valids] = newVal
	writeStrToFile(dic[valids], valids)
	if printOpt:
		print(str(valids) + " == " + str(dic[valids]))
		print("-->", end="")
		sys.stdout.flush()

def incrementValue(s, printOpt=True):
	global dic

	try:
		updateValue(s, dic[s] + 1, printOpt=printOpt)
	except:
		print("Tried to increment string!")
		return

def decrementValue(s, printOpt=True):
	global dic

	try:
		updateValue(s, dic[s] - 1, printOpt=printOpt)
	except:
		print("Tried to increment string!")
		return

# Attempts to return value of key in dic. Returns None if not found
def getDicVal(s):
	global dic
	try:
		return dic[s]
	except KeyError:
		return None
