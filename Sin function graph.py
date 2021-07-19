# Sin Function graph 

import matplotlib.pyplot as p
import numpy as n

x=n.arange(0 , 2*n.pi , 0.1)
y=n.sin(x)
p.plot(x,y,color='r',label='sin(x)')
p.xlabel("X-axis ---------->")
p.ylabel("Y-axis ---------->")
p.grid(True)
p.legend()
p.title("Sin Function")
p.show()
