# here we go
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import re
import scipy.optimize as opt

lines = open( 'LHOX206als.txt', "r" ).readlines()[::2]
textfile = open("testtext01.txt", "w")
textfile.writelines(lines)
l = []
for i in range(np.max(len(lines))):
    j = re.sub(' +', ',', lines[i])
    k = np.fromstring(j, sep=',')
    l.append(k)

m = np.array(l)

xcenter = []
xcenter.append(m[:,1])
xcenter01 = np.asarray(xcenter)
xcenter01 = xcenter01.astype(np.float)

ycenter = []
ycenter.append(m[:,2])
ycenter01 = np.asarray(ycenter)
ycenter01 = ycenter01.astype(np.float)

zmag = []
zmag.append(m[:,3])
zmag01 = np.asarray(zmag)
zmag01 = zmag01.astype(np.float)

zlum = 10**(-(zmag01/2.5))
zlumcoeff = 1638324779.6286438
zlum01 = zlum * zlumcoeff

dataset = np.vstack((xcenter01,ycenter01,zlum01))
dataset01 = np.transpose(dataset)
dataset02 = dataset01.astype(np.float)

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
plt.scatter(dataset02[:,0],dataset02[:,2])
ax.set_yscale('log')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(2,1,1)
plt.scatter(dataset02[:,1],dataset02[:,2])
ax.set_yscale('log')
plt.show()

amplitude = 3000
xo = 2500
yo = 2450
sigma_x = 1000
sigma_y = 1000
theta = 0
offset = 0

def twoD_Gaussian((x, y), amplitude, xo, yo, sigma_x, sigma_y, theta, offset):
    xo = float(xo)
    yo = float(yo)    
    a = (np.cos(theta)**2)/(2*sigma_x**2) + (np.sin(theta)**2)/(2*sigma_y**2)
    b = -(np.sin(2*theta))/(4*sigma_x**2) + (np.sin(2*theta))/(4*sigma_y**2)
    c = (np.sin(theta)**2)/(2*sigma_x**2) + (np.cos(theta)**2)/(2*sigma_y**2)
    g = offset + amplitude*np.exp( - (a*((x-xo)**2) + 2*b*(x-xo)*(y-yo) 
                            + c*((y-yo)**2)))
    return g.ravel()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dataset02[:,0], dataset02[:,1], dataset02[:,2], zdir='z', s=5, depthshade=True )
#ax.set_xlim3d(2200,2800)
#ax.set_ylim3d(2200,2800)
ax.set_zlim3d(500,30000)
plt.show()

dataset03 = (dataset02[:,0], dataset02[:,1])

initial_guess = (amplitude,xo,yo,sigma_x,sigma_y,theta,offset)

data_noisy = dataset02[:,2] + 0.0*np.random.normal(size=(dataset02[:,2]).shape)

popt, pcov = opt.curve_fit(twoD_Gaussian, (dataset03), data_noisy, p0=initial_guess, maxfev=100000)