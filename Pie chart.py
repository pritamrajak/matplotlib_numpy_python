# Pie chart for one student mark

import matplotlib.pyplot as p
import numpy as n

subject=['English','Mathamatics','Physics','Chemistry','Computer']
marks=[71,54,51,58,63]

color=['red','yellow','blue','orange','green']

p.pie(marks,labels=subject,colors=color,shadow='True',autopct="%1.1f%%",startangle=45)

p.title('Marks Distribution')

p.show()
