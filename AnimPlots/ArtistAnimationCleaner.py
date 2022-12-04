import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
import matplotlib.image as mgimg


N = 5
Matrix = np.ones((N,N))
dust=[]
time=[]
t=0

images = []

def clean(i,j,t):
    global images
    while Matrix.sum()>0:
        disti=random.randint(-1,2)
        distj=random.randint(-1,2)
        if 0<=i+disti<N and 0<=j+distj<N:
            i,j=i+disti,j +distj

        if Matrix[i,j]>0:
            Matrix[i,j]=0
            # plt.imshow(Matrix, vmin=0, vmax=1)
            # plt.show()
            imgplot = plt.imshow(Matrix, vmin=0, vmax=1)
            images.append([imgplot])
        t += 1
        dust.append(Matrix.sum())
        time.append(t)          
    return Matrix

clean(2,2,t)

fig = plt.figure()
cleaning_anim = animation.ArtistAnimation(fig, images, interval=50, blit=True, repeat=False)

plt.show()

# from matplotlib.animation import PillowWriter
# cleaning_anim.save('randomvacum.gif', dpi=150, writer=PillowWriter(fps=3))


