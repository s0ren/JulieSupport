import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random



# N = 5
# Matrix = np.ones((N,N))
# dust=[]
# time=[]
# t=0


# def clean(i,j,t):
#     while Matrix.sum()>0:
#         disti=random.randint(-1,2)
#         distj=random.randint(-1,2)
#         if 0<=i+disti<N and 0<=j+distj<N:
#             i,j=i+disti,j +distj

#         if Matrix[i,j]>0:
#             Matrix[i,j]=0
#             plt.imshow(Matrix, vmin=0, vmax=1)
#             plt.show()
#         t += 1
#         dust.append(Matrix.sum())
#         time.append(t)          
#     return Matrix

# clean(2,2,t)


N = 5
Matrix = np.ones((N,N))
dust=[]
time=[]
t=0

ANIMATION = True



def clean(i,j,t, ANIMATION=False):
    #global i, j, Matrix, im

    def clean_step(frame, i, j, Matrix, im, ANIMATION):
        #global i, j, Matrix, im, ANIMATION
        disti=random.randint(-1,2)
        distj=random.randint(-1,2)
        if 0<=i+disti<N and 0<=j+distj<N:
            i,j=i+disti,j +distj

        if Matrix[i,j]>0:
            Matrix[i,j]=0
            if ANIMATION:
                im.set_array(Matrix)
            else:
                plt.imshow(Matrix, vmin=0, vmax=1)
                #plt.show()
        t += 1
        dust.append(Matrix.sum())
        time.append(t)  
        if ANIMATION:
            return im,
        else:
            return Matrix


    N = 5
    Matrix = np.ones((N,N))
    if ANIMATION:
        fig = plt.figure()
        im = plt.imshow(Matrix,  vmin=0, vmax=1, animated=True)
        ani = animation.FuncAnimation(fig, clean_step, interval=200, blit=True)
    else:
        while Matrix.sum() > 0:
            clean_step(None, i, j, Matrix, im, ANIMATION)
    plt.show()

clean(2,2,t, ANIMATION=False)