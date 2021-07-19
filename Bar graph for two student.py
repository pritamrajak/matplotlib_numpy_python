# Bar graph for multipule data for example 2 student mark

import matplotlib.pyplot as p
import numpy as n

subject=['English','Mathamatics','Physics','Chemistry','Computer']
mark1=[71,54,51,58,63]
mark2=[46,50,34,25,65]

xpos1=n.arange(len(subject))
xpos2=xpos1 + 0.5

p.bar(xpos1,mark1,width=0.4,label='Marks of one student',color='m')
p.bar(xpos2,mark2,width=0.4,label='Marks of other student',color='c')

p.title('Subject Marks')
p.xticks(xpos1 + 0.25,subject)
p.legend()
p.show()
