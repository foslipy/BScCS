import matplotlib.pyplot as plt
s={1+2j,1+1j,2+4j}
x=[x.real for X in s]
y=[y.imag for X in s]
plt.plot(x,y,'ro')
plt.axis([0,15,0,15])
plt.show()
