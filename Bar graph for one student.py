# Bar graph for single data for example one student mark

import matplotlib.pyplot as p
import numpy as n

subject=['English','Mathamatics','Physics','Chemistry','Computer']
marks=[71,54,51,58,63]

xpos=n.arange(len(subject))

p.bar(xpos,marks,width=0.5,label='Marks of subject',color='m')

p.title('Subject Marks')
p.xticks(xpos,subject)
p.legend()
p.show()
