import counterUtils as cu

def keyboardThread():

	global dic

	while (True):

		if cu.getDicVal("kill") is not None:
			return

		# Get input
		s = input()
		input_arr = s.split(" ")

		f = input_arr[0]

		if len(input_arr) > 1:
			try:
				cu.updateValue(f, int(input_arr[1]))
			except ValueError:
				cu.updateValue(f, input_arr[1])

		else:
			if cu.getDicVal(f) == None:
				cu.updateValue(f, 0)
			else:
				try:
					cu.updateValue(f, cu.getDicVal(f) + 1)
				except TypeError:
					print("It's a not a number!")
		
