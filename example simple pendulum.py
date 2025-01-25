from pylab import * # basically import everything
from mathfunction import * # basically import everything


L = [0.2,0.3,0.4,0.5,0.6,0.7,0.8]
t = [0.90,1.19,1.30,1.47,1.58,1.77,1.83]


print(len(L),len(t))

plot(L,t,'r',label = 'T vs L')

tsq = []
for time in t:
    # tsq.append(time**2)
    tsq.append(sqr(time))

# print(len(L),len(tsq))
# print (tsq)
plot(L,tsq,'b',label = 'T^2 vs L')
legend()
# show()
# print(sqr(238))
print("square array is",Arrsq(L))


