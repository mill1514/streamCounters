import matplotlib.pyplot as plt
import matplotlib.animation as anim
import time

def plot_cont(fun, xmax):
    y = []
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)

    def update(i):
        yi = fun(i)
        y.append(yi)
        if (len(y) > 10):
            y.remove(y[0])
        x = range(len(y))
        ax.clear()
        ax.plot(x, y)

    a = anim.FuncAnimation(fig, update, frames=xmax, repeat=False)
    plt.show()


def ex(i):
    while (True):
        raw = input("-->")
        try:
            return int(raw)
        except:
            continue
    return -1

plot_cont(ex, 1000)