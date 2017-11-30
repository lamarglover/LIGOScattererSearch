import numpy as np
import re

lines = open( 'LHOX206als.txt', "r" ).readlines()[::2] #reference ALS content here
textfile = open("testtext01.txt", "w")
textfile.writelines(lines)
l = []
for i in range(np.max(len(lines))):
    j = re.sub(' +', ',', lines[i])
    k = np.fromstring(j, sep=',')
    l.append(k)

RefFrameData = np.array(l)

xcenter = []
xcenter.append(RefFrameData[:,1])
xcenter01 = np.asarray(xcenter)
xcenter01 = xcenter01.astype(np.float)

ycenter = []
ycenter.append(RefFrameData[:,2])
ycenter01 = np.asarray(ycenter)
ycenter01 = ycenter01.astype(np.float)

zmag = []
zmag.append(RefFrameData[:,3])
zmag01 = np.asarray(zmag)
zmag01 = zmag01.astype(np.float)

zlum = 10**(-(zmag01/2.5))
zlumcoeff = 1638324779.6286438
zlum01 = zlum * zlumcoeff

dataset = np.vstack((xcenter01,ycenter01,zlum01))
dataset01 = np.transpose(dataset)
RefFrameData01 = dataset01.astype(np.float)

lines = open( 'LHOX207als.txt', "r" ).readlines()[::2] #comparison ALS content here
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

ScatAmt = 25 # Number of Most Luminous Scatterers to be tracked
XYDist = 40 #r value pixel distance between ref and comparison image
RefFrameName = 206 # designation of reference image
CompFrameName = 207 # designation of comparison image

ZSortRef = sorted(RefFrameData01, key=lambda arr: arr[2], reverse=True)
ZSortRef01 = np.vstack(ZSortRef)
TopZSortRef = ZSortRef01[0:ScatAmt]
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
        if RefXYDist < XYDist:
            o.append(n)
            for p in range(len(o)):
                q = o[p]
                RefXYZDist = np.sqrt((TopZSortRef[m,0] - q[0])**2 + (TopZSortRef[m,1] - q[1])**2 + + (TopZSortRef[m,2] - q[2])**2)
                r = np.append(q,RefXYZDist)
                s.append(r)
                for t in range(len(s)):
                    u.append(s[t][3])
                    v = np.min(u)
                    w = u.index(v)
                    x.append(s[w])
                    u = []
                s = []
            o = []

print (t)