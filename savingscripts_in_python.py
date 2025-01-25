# from pylab import linspace, plot, legend, gca, show , pi, sin
from pylab import * # basicaaly import everything
x = linspace(-5*pi, 5*pi, 500)
plot(x,x,'b',label = 'x')
plot(x,-x,'b',label = '-x')
plot(x,sin(x),'b',label = 'sin(x)')
plot(x,sin(x),'g',label = 'sin(x)')
plot(x,x*sin(x),'r',label = 'xsin(x)', linewidth = 4)
legend()
legend()
show()
