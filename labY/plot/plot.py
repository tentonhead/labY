#--------\---------\---------\---------\---------\---------\---------\---------\
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import LinearLocator
from scipy.interpolate import UnivariateSpline


def plot(x, y, **kwargs):
    plt.plot(x.data, y.data, **kwargs)

def scatter(x, y, **kwargs):
    plt.scatter(x.data, y.data, **kwargs)

def interpolate(x, y, smooth, dots=200):
    spline_interp = UnivariateSpline(x.data, y.data, s=smooth)
    x_new = np.linspace(x.data.min(), x.data.max(), dots)
    y_new = spline_interp(x_new)
    return x_new, y_new

class GraphPaper():
    def __init__(self, xlabels="", ylabels="", title="",orientation='h'):
        WIDTH, HEIGHT = 28/2.54, 20/2.54
        DPI = 100
        if orientation == 'h':
            self.fig, self.ax = plt.subplots(figsize=(WIDTH, HEIGHT), dpi=DPI)
            self.x_origin, self.x_end = 0, 28 # number of 1cm cells horizontally
            self.y_origin, self.y_end = 0, 20 # number of 1cm cells vertically
        else:
            self.fig, self.ax = plt.subplots(figsize=(HEIGHT, WIDTH), dpi=DPI)
            self.x_origin, self.x_end = 0, 20 # number of 1cm cells horizontally
            self.y_origin, self.y_end = 0, 28 # number of 1cm cells vertically

        self.ax.set_aspect('equal')
        self.ax.set_xticks(range(self.x_end+1), xlabels)  # X ticks every 1 cm
        self.ax.set_yticks(range(self.y_end+1), ylabels)  # Y ticks every 1 cm
        self.ax.xaxis.set_minor_locator(LinearLocator(self.x_end*10))
        self.ax.yaxis.set_minor_locator(LinearLocator(self.y_end*10))
        #self.ax.set_xticklabels()
        self.ax.set(xlim=(self.x_origin, self.x_end), 
                    ylim=(self.y_origin, self.y_end),
                    title=title)
        self.ax.set_xticklabels(xlabels)
        self.ax.set_yticklabels(ylabels)
        self.ax.grid(which="major",color='c', lw=1)
        self.ax.grid(which="minor",color='c', lw=0.25)
        # Adjust margins to specific values
        # (left: 8.5 mm, right: 8.5 mm, top: 5 mm, bottom: 5 mm)
        plt.subplots_adjust(left=0.0286, right=0.9714, 
                            top=0.9762, bottom=0.0238)

    """
    def autoplot(self, x, y):
        #Do stuff on x and y
        self.plot(x, y)

    def autoscat(self, x, y, color="black", s=10, **kwargs):
        print("automatic scatter")
        x /= xstep; x += xoff
        y /= ystep; y += yoff
        plt.scatter(x, y, color=color, s=s, **kwargs)
    """

    def plot(self, *args, **kwargs):
        plt.plot(*args, color="black", **kwargs)

    def save(self, *args, **kwargs):
        plt.savefig(*args, **kwargs)

    def show(self):
        plt.show()

    def scatter(self, x, y, color="black", s=10, **kwargs):
        if type(x) == np.ndarray:
            xstep = find_step(np.floor(x[0]), np.ceil(x[-1]))
            ystep = find_step(np.floor(y[0]), np.ceil(y[-1]), 'y')
        else:
            xstep = find_step(np.floor(x), np.ceil(x))
            ystep = find_step(np.floor(y), np.ceil(y), 'y')

        print("x, y steps:", xstep, ystep)
        plt.scatter(x, y, color=color, s=s, **kwargs)

    def test_plot(self, x, y):
        plt.scatter(x[0], y[0], color="red")
        plt.scatter(x, y, color="black", s=10)
        plt.plot(x, y, color="black")
        plt.scatter(x[-1], y[-1], color="red")

    def scale(self, x_array, y_array):
        x = np.copy(x_array)
        y = np.copy(y_array)
        x_min = np.floor(np.min(x)); x_max = np.ceil(np.max(x))
        y_min = np.floor(np.min(y)); y_max = np.ceil(np.max(y))
        xcells = self.x_end - self.x_origin
        ycells = self.y_end - self.y_origin
        print(f"x: {x_min} - {x_max}")
        print(f"y: {y_min} - {y_max}")
        return x, y


#???????????????????????????
def find_step(a, b, ax='x'):
    cells = 0
    if ax in ['y', 'Y']:
        cells = 20
    else:
        cells = 28
    steps = [1, 2, 4, 5, 10]
    i = 0
    l = abs(b-a)
    while True:
        if l/steps[i] < cells:
            break
        else:
            l = abs(b-a)
            i += 1
    return steps[i]
