from tkinter import *
from tkinter.ttk import *
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from SampleData import *

root = Tk()

# make new figure with size and dpi
figure = Figure(figsize=(5, 4), dpi=100)
# change to add more figures
plot = figure.add_subplot(1, 1, 1)

# plot red point
plot.plot(0.5, 0.3, color="red", marker="o", linestyle="")

data = []
# x = np.linspace(1, 100)
GenerateData(data,300,100,20)
data = np.array(data)


plot.plot(data, color="blue", marker="x", linestyle="")

canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()