from pylab import *
from numpy import *
from matplotlib import *
a = imread('penguins.png')
l = imread('lambo.jpg')
l = copy(l)
print(type(l))
print(l.dtype)
print(l.shape)
l[(2560-360):-1,(2560-360):-1] = a[:,:,:3]
# print(type(a))  # <class 'numpy.ndarray'> nd.array is a n-dimensional array
# print(a.shape) # (370, 370, 4) 3 is for RGB and 1 is for opacity
# print(a[0,0,0]) #red value of the first 
# print(a[0,0,1]) #green value of the first pixel
# imshow(a[:,:,1]) # red channel
 # color bar to show the color scale
# show()

# a = a[:200,:100,:2]
# a[100:200] = 0
# imshow(a)
# colorbar() 
# print(np.max(a[:,:,0]))
# print(np.min(a[:,:,0]))
# print(a.dtype)
# print(colormaps())
# print(a)



# //////  get the top left corner of the image
# a = a[0:180,0:180,:]
# imshow(a)

#     GET TEH FACE OF TEH BABY PENGUIN
# a = a[220:320,140:240,:]
# a[:,:,0] = 0.2
# imshow(a)

# /////////////// Resize image to half by dropping half of the pxels

l = l[::4,::4,:]
imshow(l)
print("hey")

show()
# print("hey")


# Save the image to a file

imsave('lambo_size.png', l)
print("Image saved as 'lambo_size.png'")