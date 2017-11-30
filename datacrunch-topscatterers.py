import numpy as np
import matplotlib.pyplot as plt

ExpTime = [1.25E-04,1.56E-04,2.00E-04,2.50E-04,4.00E-04,5.00E-04,6.25E-04,8.00E-04,1.00E-03,1.25E-03,1.56E-03,2.00E-03,2.50E-03,3.13E-03,4.00E-03,5.00E-03,6.25E-03,8.00E-03,1.00E-02,1.25E-02,1.67E-02,2.00E-02,2.50E-02,3.33E-02,4.00E-02,5.00E-02,6.67E-02,7.69E-02,1.00E-01,1.25E-01,1.67E-01,2.00E-01,2.50E-01,3.03E-01,4.00E-01,5.00E-01,6.25E-01,7.69E-01,1.00E+00,1.30E+00]
ScatAmt = 50
SumSet = []
MeanSet = []
LumArray = []

DummyLum = np.zeros((50,1)) #spaceholder for missing data
DummyVal = 0 #spaceholder for missing data

data00 = np.loadtxt("206-ShrCoeff-Scat.txt", delimiter=",")

ZSortRef = sorted(data00, key=lambda arr: arr[6], reverse=True)
ZSortRef01 = np.vstack(ZSortRef)
TopZSortRef = ZSortRef01[0:ScatAmt]

zlum00 = []
for row in TopZSortRef:
    zlum00.append(row[6])

LumTotal00 = np.sum(TopZSortRef[:ScatAmt])
zlummean00 = np.mean(zlum00)

LumArray.append(zlum00)
SumSet.append(LumTotal00)
MeanSet.append(zlummean00)
print (zlum00)
print (LumTotal00)
print (np.mean(zlum00))

data01 = np.loadtxt("206Ref-Comp207-ScatTracking.txt", delimiter=",")

zlum01 = []
for row in data01:
    zlum01.append(row[2])

LumTotal01 = np.sum(zlum01[:])
zlummean01 = np.mean(zlum01)

LumArray.append(zlum01)
SumSet.append(LumTotal01)
MeanSet.append(zlummean01)
print (zlum01)
print (LumTotal01)
print (np.mean(zlum01))

data02 = np.loadtxt("206Ref-Comp208-ScatTracking.txt", delimiter=",")

zlum02 = []
for row in data02:
    zlum02.append(row[2])

LumTotal02 = np.sum(zlum02[:])
zlummean02 = np.mean(zlum02)

LumArray.append(zlum02)
SumSet.append(LumTotal02)
MeanSet.append(zlummean02)
print (zlum02)
print (LumTotal02)
print (np.mean(zlum02))

data03 = np.loadtxt("206Ref-Comp209-ScatTracking.txt", delimiter=",")

zlum03 = []
for row in data03:
    zlum03.append(row[2])

LumTotal03 = np.sum(zlum03[:])
zlummean03 = np.mean(zlum03)

LumArray.append(zlum03)
SumSet.append(LumTotal03)
MeanSet.append(zlummean03)
print (zlum03)
print (LumTotal03)
print (np.mean(zlum03))

data04 = np.loadtxt("206Ref-Comp210-ScatTracking.txt", delimiter=",")

zlum04 = []
for row in data04:
    zlum04.append(row[2])

LumTotal04 = np.sum(zlum04[:])
zlummean04 = np.mean(zlum04)

LumArray.append(zlum04)
SumSet.append(LumTotal04)
MeanSet.append(zlummean04)
print (zlum04)
print (LumTotal04)
print (np.mean(zlum04))

data05 = np.loadtxt("206Ref-Comp211-ScatTracking.txt", delimiter=",")

zlum05 = []
for row in data05:
    zlum05.append(row[2])

LumTotal05 = np.sum(zlum05[:])
zlummean05 = np.mean(zlum05)

LumArray.append(zlum05)
SumSet.append(LumTotal05)
MeanSet.append(zlummean05)
print (zlum05)
print (LumTotal05)
print (np.mean(zlum05))

data06 = np.loadtxt("206Ref-Comp212-ScatTracking.txt", delimiter=",")

zlum06 = []
for row in data06:
    zlum06.append(row[2])

LumTotal06 = np.sum(zlum06[:])
zlummean06 = np.mean(zlum06)

LumArray.append(zlum06)
SumSet.append(LumTotal06)
MeanSet.append(zlummean06)
print (zlum06)
print (LumTotal06)
print (np.mean(zlum06))

data07 = np.loadtxt("206Ref-Comp213-ScatTracking.txt", delimiter=",")

zlum07 = []
for row in data07:
    zlum07.append(row[2])

LumTotal07 = np.sum(zlum07[:])
zlummean07 = np.mean(zlum07)

LumArray.append(zlum07)
SumSet.append(LumTotal07)
MeanSet.append(zlummean07)
print (zlum07)
print (LumTotal07)
print (np.mean(zlum07))

data08 = np.loadtxt("206Ref-Comp214-ScatTracking.txt", delimiter=",")

zlum08 = []
for row in data08:
    zlum08.append(row[2])

LumTotal08 = np.sum(zlum08[:])
zlummean08 = np.mean(zlum08)

LumArray.append(zlum08)
SumSet.append(LumTotal08)
MeanSet.append(zlummean08)
print (zlum08)
print (LumTotal08)
print (np.mean(zlum08))

data09 = np.loadtxt("206Ref-Comp215-ScatTracking.txt", delimiter=",")

zlum09 = []
for row in data09:
    zlum09.append(row[2])

LumTotal09 = np.sum(zlum09[:])
zlummean09 = np.mean(zlum09)

LumArray.append(zlum09)
SumSet.append(LumTotal09)
MeanSet.append(zlummean09)
print (zlum09)
print (LumTotal09)
print (np.mean(zlum09))

#data10 = np.loadtxt("206Ref-Comp216-ScatTracking.txt", delimiter=",")
#
#zlum10 = []
#for row in data10:
#    zlum10.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum10)
#LumTotal10 = np.sum(zlum10[:])
#zlummean10 = np.mean(zlum10)
#
#SumSet.append(LumTotal10)
#MeanSet.append(zlummean10)
#print (zlum10)
#print (LumTotal10)
#print (np.mean(zlum10))

data11 = np.loadtxt("206Ref-Comp217-ScatTracking.txt", delimiter=",")

zlum11 = []
for row in data11:
    zlum11.append(row[2])

LumTotal11 = np.sum(zlum11[:])
zlummean11 = np.mean(zlum11)

LumArray.append(zlum11)
SumSet.append(LumTotal11)
MeanSet.append(zlummean11)
print (zlum11)
print (LumTotal11)
print (np.mean(zlum11))

data12 = np.loadtxt("206Ref-Comp218-ScatTracking.txt", delimiter=",")

zlum12 = []
for row in data12:
    zlum12.append(row[2])

LumTotal12 = np.sum(zlum12[:])
zlummean12 = np.mean(zlum12)

LumArray.append(zlum12)
SumSet.append(LumTotal12)
MeanSet.append(zlummean12)
print (zlum12)
print (LumTotal12)
print (np.mean(zlum12))

data13 = np.loadtxt("206Ref-Comp219-ScatTracking.txt", delimiter=",")

zlum13 = []
for row in data13:
    zlum13.append(row[2])

LumTotal13 = np.sum(zlum13[:])
zlummean13 = np.mean(zlum13)

LumArray.append(zlum13)
SumSet.append(LumTotal13)
MeanSet.append(zlummean13)
print (zlum13)
print (LumTotal13)
print (np.mean(zlum13))

data14 = np.loadtxt("206Ref-Comp220-ScatTracking.txt", delimiter=",")

zlum14 = []
for row in data14:
    zlum14.append(row[2])

LumTotal14 = np.sum(zlum14[:])
zlummean14 = np.mean(zlum14)

LumArray.append(zlum14)
SumSet.append(LumTotal14)
MeanSet.append(zlummean14)
print (zlum14)
print (LumTotal14)
print (np.mean(zlum14))

data15 = np.loadtxt("206Ref-Comp221-ScatTracking.txt", delimiter=",")

zlum15 = []
for row in data15:
    zlum15.append(row[2])

LumTotal15 = np.sum(zlum15[:])
zlummean15 = np.mean(zlum15)

LumArray.append(zlum15)
SumSet.append(LumTotal15)
MeanSet.append(zlummean15)
print (zlum15)
print (LumTotal15)
print (np.mean(zlum15))

data16 = np.loadtxt("206Ref-Comp222-ScatTracking.txt", delimiter=",")

zlum16 = []
for row in data16:
    zlum16.append(row[2])

LumTotal16 = np.sum(zlum16[:])
zlummean16 = np.mean(zlum16)

LumArray.append(zlum16)
SumSet.append(LumTotal16)
MeanSet.append(zlummean16)
print (zlum16)
print (LumTotal16)
print (np.mean(zlum16))

data17 = np.loadtxt("206Ref-Comp223-ScatTracking.txt", delimiter=",")

zlum17 = []
for row in data17:
    zlum17.append(row[2])

LumTotal17 = np.sum(zlum17[:])
zlummean17 = np.mean(zlum17)

LumArray.append(zlum17)
SumSet.append(LumTotal17)
MeanSet.append(zlummean17)
print (zlum17)
print (LumTotal17)
print (np.mean(zlum17))

data18 = np.loadtxt("206Ref-Comp224-ScatTracking.txt", delimiter=",")

zlum18 = []
for row in data18:
    zlum18.append(row[2])

LumTotal18 = np.sum(zlum18[:])
zlummean18 = np.mean(zlum18)

LumArray.append(zlum18)
SumSet.append(LumTotal18)
MeanSet.append(zlummean18)
print (zlum18)
print (LumTotal18)
print (np.mean(zlum18))

data19 = np.loadtxt("206Ref-Comp225-ScatTracking.txt", delimiter=",")

zlum19 = []
for row in data19:
    zlum19.append(row[2])

LumTotal19 = np.sum(zlum19[:])
zlummean19 = np.mean(zlum19)

LumArray.append(zlum19)
SumSet.append(LumTotal19)
MeanSet.append(zlummean19)
print (zlum19)
print (LumTotal19)
print (np.mean(zlum19))

#data20 = np.loadtxt("206Ref-Comp226-ScatTracking.txt", delimiter=",")
#
#zlum20 = []
#for row in data20:
#    zlum20.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum20)
#LumTotal20 = np.sum(zlum20[:])
#zlummean20 = np.mean(zlum20)
#
#SumSet.append(LumTotal20)
#MeanSet.append(zlummean20)
#print (zlum20)
#print (LumTotal20)
#print (np.mean(zlum20))
#
#data21 = np.loadtxt("206Ref-Comp227-ScatTracking.txt", delimiter=",")
#
#zlum21 = []
#for row in data21:
#    zlum21.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum21)
#LumTotal21 = np.sum(zlum21[:])
#zlummean21 = np.mean(zlum21)
#
#SumSet.append(LumTotal21)
#MeanSet.append(zlummean21)
#print (zlum21)
#print (LumTotal21)
#print (np.mean(zlum21))

data22 = np.loadtxt("206Ref-Comp228-ScatTracking.txt", delimiter=",")

zlum22 = []
for row in data22:
    zlum22.append(row[2])

LumTotal22 = np.sum(zlum22[:])
zlummean22 = np.mean(zlum22)

LumArray.append(zlum22)
SumSet.append(LumTotal22)
MeanSet.append(zlummean22)
print (zlum22)
print (LumTotal22)
print (np.mean(zlum22))

#data23 = np.loadtxt("206Ref-Comp229-ScatTracking.txt", delimiter=",")
#
#zlum23 = []
#for row in data23:
#    zlum23.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum23)
#LumTotal23 = np.sum(zlum23[:])
#zlummean23 = np.mean(zlum23)
#
#SumSet.append(LumTotal23)
#MeanSet.append(zlummean23)
#print (zlum23)
#print (LumTotal23)
#print (np.mean(zlum23))
#
#data24 = np.loadtxt("206Ref-Comp230-ScatTracking.txt", delimiter=",")
#
#zlum24 = []
#for row in data24:
#    zlum24.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum24)
#LumTotal24 = np.sum(zlum24[:])
#zlummean24 = np.mean(zlum24)
#
#SumSet.append(LumTotal24)
#MeanSet.append(zlummean24)
#print (zlum24)
#print (LumTotal24)
#print (np.mean(zlum24))

data25 = np.loadtxt("206Ref-Comp231-ScatTracking.txt", delimiter=",")

zlum25 = []
for row in data25:
    zlum25.append(row[2])

LumTotal25 = np.sum(zlum25[:])
zlummean25 = np.mean(zlum25)

LumArray.append(zlum25)
SumSet.append(LumTotal25)
MeanSet.append(zlummean25)
print (zlum25)
print (LumTotal25)
print (np.mean(zlum25))

#data26 = np.loadtxt("206Ref-Comp232-ScatTracking.txt", delimiter=",")
#
#zlum26 = []
#for row in data26:
#    zlum26.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum26)
#LumTotal26 = np.sum(zlum26[:])
#zlummean26 = np.mean(zlum26)
#
#SumSet.append(LumTotal26)
#MeanSet.append(zlummean26)
#print (zlum26)
#print (LumTotal26)
#print (np.mean(zlum26))

data27 = np.loadtxt("206Ref-Comp233-ScatTracking.txt", delimiter=",")

zlum27 = []
for row in data27:
    zlum27.append(row[2])

LumTotal27 = np.sum(zlum27[:])
zlummean27 = np.mean(zlum27)

LumArray.append(zlum27)
SumSet.append(LumTotal27)
MeanSet.append(zlummean27)
print (zlum27)
print (LumTotal27)
print (np.mean(zlum27))

#data28 = np.loadtxt("206Ref-Comp234-ScatTracking.txt", delimiter=",")
#
#zlum28 = []
#for row in data28:
#    zlum28.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum28)
#LumTotal28 = np.sum(zlum28[:])
#zlummean28 = np.mean(zlum28)
#
#SumSet.append(LumTotal28)
#MeanSet.append(zlummean28)
#print (zlum28)
#print (LumTotal28)
#print (np.mean(zlum28))

data29 = np.loadtxt("206Ref-Comp235-ScatTracking.txt", delimiter=",")

zlum29 = []
for row in data29:
    zlum29.append(row[2])

LumTotal29 = np.sum(zlum29[:])
zlummean29 = np.mean(zlum29)

LumArray.append(zlum29)
SumSet.append(LumTotal29)
MeanSet.append(zlummean29)
print (zlum29)
print (LumTotal29)
print (np.mean(zlum29))

#data30 = np.loadtxt("206Ref-Comp236-ScatTracking.txt", delimiter=",")
#
#zlum30 = []
#for row in data30:
#    zlum30.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum30)
#LumTotal30 = np.sum(zlum30[:])
#zlummean30 = np.mean(zlum30)
#
#SumSet.append(LumTotal30)
#MeanSet.append(zlummean30)
#print (zlum30)
#print (LumTotal30)
#print (np.mean(zlum30))

data31 = np.loadtxt("206Ref-Comp237-ScatTracking.txt", delimiter=",")

zlum31 = []
for row in data31:
    zlum31.append(row[2])

LumTotal31 = np.sum(zlum31[:])
zlummean31 = np.mean(zlum31)

LumArray.append(zlum31)
SumSet.append(LumTotal31)
MeanSet.append(zlummean31)
print (zlum31)
print (LumTotal31)
print (np.mean(zlum31))

#data32 = np.loadtxt("206Ref-Comp238-ScatTracking.txt", delimiter=",")
#
#zlum32 = []
#for row in data32:
#    zlum32.append(row[2])

LumArray.append(DummyLum)
SumSet.append(DummyVal)
MeanSet.append(DummyVal)

#LumArray.append(zlum32)
#LumTotal32 = np.sum(zlum32[:])
#zlummean32 = np.mean(zlum32)
#
#SumSet.append(LumTotal32)
#MeanSet.append(zlummean32)
#print (zlum32)
#print (LumTotal32)
#print (np.mean(zlum32))

data33 = np.loadtxt("206Ref-Comp239-ScatTracking.txt", delimiter=",")

zlum33 = []
for row in data33:
    zlum33.append(row[2])

LumTotal33 = np.sum(zlum33[:])
zlummean33 = np.mean(zlum33)

LumArray.append(zlum33)
SumSet.append(LumTotal33)
MeanSet.append(zlummean33)
print (zlum33)
print (LumTotal33)
print (np.mean(zlum33))

data34 = np.loadtxt("206Ref-Comp240-ScatTracking.txt", delimiter=",")

zlum34 = []
for row in data34:
    zlum34.append(row[2])

LumTotal34 = np.sum(zlum34[:])
zlummean34 = np.mean(zlum34)

LumArray.append(zlum34)
SumSet.append(LumTotal34)
MeanSet.append(zlummean34)
print (zlum34)
print (LumTotal34)
print (np.mean(zlum34))

data35 = np.loadtxt("206Ref-Comp241-ScatTracking.txt", delimiter=",")

zlum35 = []
for row in data35:
    zlum35.append(row[2])

LumTotal35 = np.sum(zlum35[:])
zlummean35 = np.mean(zlum35)

LumArray.append(zlum35)
SumSet.append(LumTotal35)
MeanSet.append(zlummean35)
print (zlum35)
print (LumTotal35)
print (np.mean(zlum35))

data36 = np.loadtxt("206Ref-Comp242-ScatTracking.txt", delimiter=",")

zlum36 = []
for row in data36:
    zlum36.append(row[2])

LumTotal36 = np.sum(zlum36[:])
zlummean36 = np.mean(zlum36)

LumArray.append(zlum36)
SumSet.append(LumTotal36)
MeanSet.append(zlummean36)
print (zlum36)
print (LumTotal36)
print (np.mean(zlum36))

data37 = np.loadtxt("206Ref-Comp243-ScatTracking.txt", delimiter=",")

zlum37 = []
for row in data37:
    zlum37.append(row[2])

LumTotal37 = np.sum(zlum37[:])
zlummean37 = np.mean(zlum37)

LumArray.append(zlum37)
SumSet.append(LumTotal37)
MeanSet.append(zlummean37)
print (zlum37)
print (LumTotal37)
print (np.mean(zlum37))

data38 = np.loadtxt("206Ref-Comp244-ScatTracking.txt", delimiter=",")

zlum38 = []
for row in data38:
    zlum38.append(row[2])

LumTotal38 = np.sum(zlum38[:])
zlummean38 = np.mean(zlum38)

LumArray.append(zlum38)
SumSet.append(LumTotal38)
MeanSet.append(zlummean38)
print (zlum38)
print (LumTotal38)
print (np.mean(zlum38))

data39 = np.loadtxt("206Ref-Comp245-ScatTracking.txt", delimiter=",")

zlum39 = []
for row in data39:
    zlum39.append(row[2])

LumTotal39 = np.sum(zlum39[:])
zlummean39 = np.mean(zlum39)

LumArray.append(zlum39)
SumSet.append(LumTotal39)
MeanSet.append(zlummean39)
print (zlum39)
print (LumTotal39)
print (np.mean(zlum39))

print (SumSet)
print (MeanSet)

plt.scatter(ExpTime,SumSet)
plt.suptitle('Cumulative Luminosity of Top 50 Scatterers vs Exposure Time')
plt.xscale('log')
plt.xlim(9e-5,2)
plt.ylim(1e5,1e8)
plt.yscale('log')
plt.ylabel('Cumulative Luminosity (Arbitrary Units)')
plt.xlabel('Exposure Time (seconds)')
plt.savefig('CumLumTop50.jpg')
plt.show()

plt.scatter(ExpTime,MeanSet)
plt.suptitle('Mean Luminosity of Top 50 Scatterers vs Exposure Time')
plt.xscale('log')
plt.xlim(9e-5,2)
plt.ylim(5e3,2e5)
plt.yscale('log')
plt.ylabel('Mean Luminosity (Arbitrary Units)')
plt.xlabel('Exposure Time (seconds)')
plt.savefig('MeanLumTop50.jpg')
plt.show()

a = []
d = []
for c in range (ScatAmt):
    for b in range (40):
        a.append(float(LumArray[b][c]))
    d.append(a)
    a = []
for e in range (ScatAmt):
    plt.scatter(ExpTime,d[e])
    plt.suptitle('Luminosity of Scatterer vs Exposure Time')
    plt.xscale('log')
    plt.xlim(9e-5,2)
    plt.ylim(5e3,2e6)
    plt.yscale('log')
    plt.ylabel('Luminosity (Arbitrary Units)')
    plt.xlabel('Exposure Time (seconds)')
    #plt.savefig('MeanLumTop50.jpg')
    plt.show()