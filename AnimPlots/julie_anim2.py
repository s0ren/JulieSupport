import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random

N = 5

Matrix = np.ones((N,N))
dust=[]
time=[]
t=0
i=2
j=2

fig = plt.figure()
im = plt.imshow(Matrix,  vmin=0, vmax=1, animated=True)

def clean(*args):
#    while Matrix.sum()>0:
    global i,j,t
    disti=random.randint(-1,2)
    distj=random.randint(-1,2)
    if 0<=i+disti<N and 0<=j+distj<N:
        i,j = i+disti, j+distj

#        if Matrix[i,j]>0:
    Matrix[i,j]=0
    im.set_array(Matrix)
#    plt.imshow(Matrix, vmin=0, vmax=1)
#    plt.show()
    t += 1
    dust.append(Matrix.sum())
    time.append(t)  

    #return Matrix

    return im,

ani = animation.FuncAnimation(fig, clean, interval=500, blit=True)
plt.show()
