import numpy as np

from bokeh.plotting import figure, show

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

p = figure()

p.scatter(x, y, legend_label="sin(x)")
p.line(x, y, legend_label="sin(x)")

p.line(x, 2*y, legend_label="2*sin(x)",
       line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3*y, legend_label="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3*y, legend_label="3*sin(x)", line_color="green")

p.legend.orientation = "horizontal"

show(p)
