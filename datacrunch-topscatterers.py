import numpy as np
import matplotlib.pyplot as plt

ExpTimeArray = []
ScatArray = []

data00 = np.loadtxt("PyMeth03-258Ref-Comp258-ScatTracking.txt", delimiter=",")
time00 = 258
ScatArray.append(data00)
ExpTimeArray.append(time00)

data01 = np.loadtxt("PyMeth03-258Ref-Comp259-ScatTracking.txt", delimiter=",")
time01 = 259
ScatArray.append(data01)
ExpTimeArray.append(time01)

data02 = np.loadtxt("PyMeth03-259Ref-Comp260-ScatTracking.txt", delimiter=",")
time02 = 260
ScatArray.append(data02)
ExpTimeArray.append(time02)

data03 = np.loadtxt("PyMeth03-260Ref-Comp261-ScatTracking.txt", delimiter=",")
time03 = 261
ScatArray.append(data03)
ExpTimeArray.append(time03)

data04 = np.loadtxt("PyMeth03-261Ref-Comp262-ScatTracking.txt", delimiter=",")
time04 = 262
ScatArray.append(data04)
ExpTimeArray.append(time04)

MeanArray = []
SumArray = []
d = []

for a in range(len(ScatArray)):
    for b in range(len(ScatArray[a])):
        c = ScatArray[a][b][2]
        d.append(c)
    e = np.mean(d)
    f = np.sum(d)
    MeanArray.append(e)
    SumArray.append(f)
    d = []
    

plt.scatter(ExpTimeArray,SumArray)
plt.suptitle('Cumulative Luminosity of Top 50 Scatterers (Exposure Time = sec)')
plt.xscale('log')
plt.xlim(255,265)
plt.ylim(8e3,8e5)
plt.yscale('log')
plt.ylabel('Cumulative Luminosity (Arbitrary Units)')
plt.xlabel('Image Number')
plt.savefig('CumLumTop50.jpg')
plt.show()

plt.scatter(ExpTimeArray,MeanArray)
plt.suptitle('Mean Luminosity of Top 50 Scatterers (Exposure Time = sec)')
plt.xscale('log')
plt.xlim(255,265)
plt.ylim(2e2,2e4)
plt.yscale('log')
plt.ylabel('Mean Luminosity (Arbitrary Units)')
plt.xlabel('Image Number')
plt.savefig('MeanLumTop50.jpg')
plt.show()