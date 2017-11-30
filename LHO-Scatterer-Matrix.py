import numpy as np

ScatMatrix = []

data00 = np.loadtxt("206-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data00)
data01 = np.loadtxt("207-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data01)
data02 = np.loadtxt("208-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data02)
data03 = np.loadtxt("209-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data03)

data04 = np.loadtxt("210-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data04)
data05 = np.loadtxt("211-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data05)
data06 = np.loadtxt("212-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data06)
data07 = np.loadtxt("213-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data07)

data08 = np.loadtxt("214-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data08)
data09 = np.loadtxt("215-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data09)
data10 = np.loadtxt("216-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data10)
data11 = np.loadtxt("217-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data11)

data12 = np.loadtxt("218-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data12)
data13 = np.loadtxt("219-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data13)
data14 = np.loadtxt("220-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data14)
data15 = np.loadtxt("221-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data15)

data16 = np.loadtxt("222-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data16)
data17 = np.loadtxt("223-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data17)
data18 = np.loadtxt("224-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data18)
data19 = np.loadtxt("225-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data19)

data20 = np.loadtxt("226-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data20)
data21 = np.loadtxt("227-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data21)
data22 = np.loadtxt("228-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data22)
data23 = np.loadtxt("229-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data23)

data24 = np.loadtxt("230-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data24)
data25 = np.loadtxt("231-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data25)
data26 = np.loadtxt("232-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data26)
data27 = np.loadtxt("233-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data27)

data28 = np.loadtxt("234-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data28)
data29 = np.loadtxt("235-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data29)
data30 = np.loadtxt("236-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data30)
data31 = np.loadtxt("237-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data31)

data32 = np.loadtxt("238-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data32)
data33 = np.loadtxt("239-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data33)
data34 = np.loadtxt("240-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data34)
data35 = np.loadtxt("241-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data35)

data36 = np.loadtxt("242-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data36)
data37 = np.loadtxt("243-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data37)
data38 = np.loadtxt("244-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data38)
data39 = np.loadtxt("245-ShrCoeff-Scat.txt", delimiter=",")
ScatMatrix.append(data39)

#np.savetxt('ScatCoordMatrix-Coeff01.txt',ScatMatrix,delimiter=',', fmt='%.9f')
b = 0

dataset = np.vstack((ScatMatrix[b][:,1],ScatMatrix[b][:,2],ScatMatrix[b][:,6]))
dataset01 = np.transpose(dataset)
RefFrameData01 = dataset01.astype(np.float)

dataset04 = np.vstack((ScatMatrix[b+1][:,1],ScatMatrix[b+1][:,2],ScatMatrix[b+1][:,6]))
dataset05 = np.transpose(dataset04)
CompFrameData01 = dataset05.astype(np.float)

ScatAmt = 50 # Number of Most Luminous Scatterers to be tracked
XYDist = 5.5 #r value pixel distance between ref and comparison image

ZSortRef = sorted(RefFrameData01, key=lambda arr: arr[2], reverse=True)
ZSortRef01 = np.vstack(ZSortRef)
TopZSortRef = ZSortRef01[0:ScatAmt]
Threshold = 0.5 * (np.min(ZSortRef01[:999,2])) #may be simpler to set to specific number
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
np.savetxt('244Ref-Comp245-ScatTracking.txt',x004,delimiter=',', fmt='%.9f')

RefCoord = []

for a in range(len(TopZSortRef)):
    RefCoord.append(TopZSortRef[a,:2])
    
np.savetxt('XYCoord-TopScat-245Ref.txt',RefCoord,delimiter=',', fmt='%.9f')

x005 = np.vstack((x02,x04))
x006 = np.transpose(x005)
x007 = x006.astype(np.float)
np.savetxt('XYCoord-TopScat-245Comp244Ref-.txt',x007,delimiter=',', fmt='%.9f')

np.savetxt('PyMeth03-206Ref-Comp206-ScatTracking.txt',TopZSortRef,delimiter=',', fmt='%.9f')
