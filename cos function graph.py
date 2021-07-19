# cos Function graph 

import matplotlib.pyplot as p
import numpy as n

x=n.arange(0 , 2*n.pi , 0.1)
y=n.cos(x)
p.plot(x,y,color='r',label='cos(x)')
p.xlabel("X-axis ---------->")
p.ylabel("Y-axis ---------->")
p.grid(True)
p.legend()
p.title("cos Function")
p.show()
