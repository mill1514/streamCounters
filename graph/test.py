
import matplotlib.pyplot as plt
import numpy as np
import time

y = [5000, 5100, 5112, 5200, 5190, 5220, 5232, 5300, 5301, 5260]
x = np.linspace(0, 10, 10)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

while True:

	time.sleep(2)

	y.append(5400)
	x = np.linspace(0, len(y), len(y))

	line1.set_xdata(x)
	line1.set_ydata(y)

	fig.canvas.draw()
	fig.canvas.flush_events()