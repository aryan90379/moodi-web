from numpy import *
import matplotlib.pyplot as plt
from pylab import *

time = [0.,1.,2,3]
distance = [7.,11,15,19]
# plot(time,distance,'r',label = 'Distance vs Time')
# plot(time,distance,'o',label = 'Distance vs Time') # o is for points

# plot(time,distance,'-',label = 'Distance vs Time') 
plot(time,distance,'--',label = 'Distance vs Time') # double dashed lines
# plot(time,distance,'.',label = 'Distance vs Time') 
xlabel('Time (hours)')
ylabel('Distance (miles)')
title('Distance vs Time')
legend()

show()
# clf() // clear the figure
