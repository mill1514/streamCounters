import counterUtils as cu
import keyboardThread as kbt
import scrapingThread as st
import keylistenerThread as klt

import _thread

def main():

	cu.updateValue("cc", 0)

	#_thread.start_new_thread(kbt.keyboardThread, ())
	_thread.start_new_thread(st.scrapingThread, ())
	_thread.start_new_thread(klt.keylistenerThread, ())

	kbt.keyboardThread()

main()

