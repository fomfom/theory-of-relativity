import matplotlib.pyplot as plt
import math
import numpy as np
c = 300000000
w = 10000000
x = np.linspace(-300000000,300000000,100)
plt.xlabel('v')
plt.ylabel("u u'")
plt.grid(True)
y1 = (w+x)/(1+(w*x)/(c*c))
plt.plot(x,y1,label="Lorentz")
y2 = w + x
plt.plot(x,y2,label="Galilei")
plt.legend()
plt.show()