"""
Denne version bruger animation.ArtistAnimation, fra matplotlib.
ArtistAnimation kræver, som anden parameter en liste af 'Artist' obejekter.
På linie 56-57 tilføjer jeg dem til listen:
```
imgplot = plt.imshow(Matrix, vmin=0, vmax=1)
            images.append([imgplot])
```
man kan sige at det som `imshow()` returnerer er kompatibelt til et Artist objekt.

På line 65 kalder jeg 
```
cleaning_anim = animation.ArtistAnimation(fig, images, interval=50, blit=True, repeat=True, repeat_delay=500)
```
frem for at bruge `FuncAnimation()`, som kræver at man omskriver clean()-funktionen ret meget.

Til sidst (linie 70) eksporterer jeg til an animeret gif. 
Det gøres ganske vist på samme måde hvis det havde været en med  FuncAnimation()`.
Se 
    https://matplotlib.org/stable/gallery/animation/dynamic_image.html
    https://matplotlib.org/stable/api/_as_gen/matplotlib.animation.ArtistAnimation.html
    https://stackoverflow.com/questions/23176161/animating-pngs-in-matplotlib-using-artistanimation

"""

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as random
#import matplotlib.image as mgimg
from matplotlib.animation import PillowWriter

N = 5
Matrix = np.ones((N,N))
dust=[]
time=[]
t=0

# initialierer plt så der kun er et subplot. Bør kaldes inden clean() udføres
fig=plt.figure()

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

cleaning_anim = animation.ArtistAnimation(fig, images, interval=50, blit=True, repeat=True, repeat_delay=500)

plt.show()

#from matplotlib.animation import PillowWriter
cleaning_anim.save('randomvacum.gif', dpi=150, writer=PillowWriter(fps=1/(50/1000)))


