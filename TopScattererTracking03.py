import numpy as np
import re

#lines = open( '206-ShrCoeff-Scat.txt', "r" ).readlines()[::2] #reference ALS content here
#textfile = open("testtext01.txt", "w")
#textfile.writelines(lines)
#l = []
#for i in range(np.max(len(lines))):
#    j = re.sub(' +', ',', lines[i])
#    k = np.fromstring(j, sep=',')
#    l.append(k)
#
#RefFrameData = np.array(l)
#
#xcenter = []
#xcenter.append(RefFrameData[:,1])
#xcenter01 = np.asarray(xcenter)
#xcenter01 = xcenter01.astype(np.float)
#
#ycenter = []
#ycenter.append(RefFrameData[:,2])
#ycenter01 = np.asarray(ycenter)
#ycenter01 = ycenter01.astype(np.float)
#
#zmag = []
#zmag.append(RefFrameData[:,3])
#zmag01 = np.asarray(zmag)
#zmag01 = zmag01.astype(np.float)
#
#zlum = 10**(-(zmag01/2.5))
#zlumcoeff = 1638324779.6286438
#zlum01 = zlum * zlumcoeff
#
#dataset = np.vstack((xcenter01,ycenter01,zlum01))
#dataset01 = np.transpose(dataset)
#RefFrameData01 = dataset01.astype(np.float)

lines = open( '262-ShrCoeff-Scat.txt', "r" ).readlines()[::2] #comparison ALS content here
textfile = open("testtext01.txt", "w")
textfile.writelines(lines)
l = []
for i in range(np.max(len(lines))):
    j = re.sub(' +', ',', lines[i])
    k = np.fromstring(j, sep=',')
    l.append(k)

CompFrameData = np.array(l)

xcenter = []
xcenter.append(CompFrameData[:,1])
xcenter01 = np.asarray(xcenter)
xcenter01 = xcenter01.astype(np.float)

ycenter = []
ycenter.append(CompFrameData[:,2])
ycenter01 = np.asarray(ycenter)
ycenter01 = ycenter01.astype(np.float)

zmag = []
zmag.append(CompFrameData[:,3])
zmag01 = np.asarray(zmag)
zmag01 = zmag01.astype(np.float)

zlum = 10**(-(zmag01/2.5))
zlumcoeff = 1638324779.6286438
zlum01 = zlum * zlumcoeff

dataset04 = np.vstack((xcenter01,ycenter01,zlum01))
dataset05 = np.transpose(dataset04)
CompFrameData01 = dataset05.astype(np.float)

ScatAmt = 50 # Number of Most Luminous Scatterers to be tracked
XYDist = 10.5 #r value pixel distance between ref and comparison image

#ZSortRef = sorted(RefFrameData01, key=lambda arr: arr[2], reverse=True)
#ZSortRef01 = np.vstack(ZSortRef)

TopZSortRef = np.loadtxt( 'PyMeth03-260Ref-Comp261-ScatTracking.txt', delimiter=",")

Threshold = 0.5 * (np.min(ZSortRef01[:99,2])) #may be simpler to set to specific number
CompFrameData02 = []
for j in range (len(CompFrameData01)):
    k = CompFrameData01[j]
    if k[2] > Threshold:
        CompFrameData02.append(k)
                  
o = []
s = []
u = []
x = []
for m in range(len(TopZSortRef)):
    for l in range (len(CompFrameData02)):  
        n = CompFrameData02[l]
        RefXYDist = np.sqrt((TopZSortRef[m,0] - n[0])**2 + (TopZSortRef[m,1] - n[1])**2)
        RefXYZDist = np.sqrt((TopZSortRef[m,0] - n[0])**2 + (TopZSortRef[m,1] - n[1])**2 + (TopZSortRef[m,2] - n[2])**2)
        y = np.append(n,RefXYDist)
        z = np.append(y,RefXYZDist)
        o.append(z)
    for p in range(len(o)):
        if o[p][3] < XYDist:
            q = o[p]
            s.append(q)
        if s == []:
            s.append((TopZSortRef[m][0],TopZSortRef[m][1],0,(XYDist+1),(9e+10)))
            s02 = sorted(s, key=lambda arr: arr[4], reverse=True) #a device to check calculations
    for t in range(len(s)):
        u.append(s[t][4])
    w = u.index(np.min(u))
    x.append(s[(w)])
    u = []
    s = []
    o = []
print (len(x))
print (x)

x = np.array(x)

x01 = []
x01.append(x[:,0])
x02 = np.asarray(x01)
x02 = x02.astype(np.float)

x03 = []
x03.append(x[:,1])
x04 = np.asarray(x03)
x04 = x04.astype(np.float)

x05 = []
x05.append(x[:,2])
x06 = np.asarray(x05)
x06 = x06.astype(np.float)

x07 = []
x07.append(x[:,3])
x08 = np.asarray(x07)
x08 = x08.astype(np.float)

x09 = []
x09.append(x[:,4])
x10 = np.asarray(x09)
x10 = x02.astype(np.float)

x002 = np.vstack((x02,x04,x06,x08,x10))
x003 = np.transpose(x002)
x004 = x003.astype(np.float)
np.savetxt('PyMeth03-261Ref-Comp262-ScatTracking.txt',x004,delimiter=',', fmt='%.9f')

RefCoord = []

for a in range(len(TopZSortRef)):
    RefCoord.append(TopZSortRef[a,:2])
    
np.savetxt('PyMeth03-TopScat-261-RefXYCoordinates.txt',RefCoord,delimiter=',', fmt='%.9f')

x005 = np.vstack((x02,x04))
x006 = np.transpose(x005)
x007 = x006.astype(np.float)
np.savetxt('PyMeth03-261Ref-Comp262-XYCoord.txt',x007,delimiter=',', fmt='%.9f')