import numpy as np
import matplotlib.pyplot as plt


AllLumArray = []
ExpTimeArray = []

thresh01 = 10
thresh02 = 100
thresh03 = 1000
thresh04 = 10000
thresh05 = 100000
thresh06 = 1000000

data00 = np.loadtxt("206-ShrCoeff-Scat.txt", delimiter=",")
time00 = 1.25E-04
AllLumArray.append(data00)
ExpTimeArray.append(time00)

data01 = np.loadtxt("207-ShrCoeff-Scat.txt", delimiter=",")
time01 = 1.56E-04
AllLumArray.append(data01)
ExpTimeArray.append(time01)

data02 = np.loadtxt("208-ShrCoeff-Scat.txt", delimiter=",")
time02 = 2.00E-04
AllLumArray.append(data02)
ExpTimeArray.append(time02)

data03 = np.loadtxt("209-ShrCoeff-Scat.txt", delimiter=",")
time03 = 2.50E-04
AllLumArray.append(data03)
ExpTimeArray.append(time03)

data04 = np.loadtxt("210-ShrCoeff-Scat.txt", delimiter=",")
time04 = 4.00E-04
AllLumArray.append(data04)
ExpTimeArray.append(time04)

data05 = np.loadtxt("211-ShrCoeff-Scat.txt", delimiter=",")
time05 = 5.00E-04
AllLumArray.append(data05)
ExpTimeArray.append(time05)

data06 = np.loadtxt("212-ShrCoeff-Scat.txt", delimiter=",")
time06 = 6.25E-04
AllLumArray.append(data06)
ExpTimeArray.append(time06)

data07 = np.loadtxt("213-ShrCoeff-Scat.txt", delimiter=",")
time07 = 8.00E-04
AllLumArray.append(data07)
ExpTimeArray.append(time07)

data08 = np.loadtxt("214-ShrCoeff-Scat.txt", delimiter=",")
time08 = 1.00E-03
AllLumArray.append(data08)
ExpTimeArray.append(time08)

data09 = np.loadtxt("215-ShrCoeff-Scat.txt", delimiter=",")
time09 = 1.25E-03
AllLumArray.append(data09)
ExpTimeArray.append(time09)

data10 = np.loadtxt("216-ShrCoeff-Scat.txt", delimiter=",")
time10 = 1.56E-03
AllLumArray.append(data10)
ExpTimeArray.append(time10)

data11 = np.loadtxt("217-ShrCoeff-Scat.txt", delimiter=",")
time11 = 2.00E-03
AllLumArray.append(data11)
ExpTimeArray.append(time11)

data12 = np.loadtxt("218-ShrCoeff-Scat.txt", delimiter=",")
time12 = 2.50E-03
AllLumArray.append(data12)
ExpTimeArray.append(time12)

data13 = np.loadtxt("219-ShrCoeff-Scat.txt", delimiter=",")
time13 = 3.13E-03
AllLumArray.append(data13)
ExpTimeArray.append(time13)

data14 = np.loadtxt("220-ShrCoeff-Scat.txt", delimiter=",")
time14 = 4.00E-03
AllLumArray.append(data14)
ExpTimeArray.append(time14)

data15 = np.loadtxt("221-ShrCoeff-Scat.txt", delimiter=",")
time15 = 5.00E-03
AllLumArray.append(data15)
ExpTimeArray.append(time15)

data16 = np.loadtxt("222-ShrCoeff-Scat.txt", delimiter=",")
time16 = 6.25E-03
AllLumArray.append(data16)
ExpTimeArray.append(time16)

data17 = np.loadtxt("223-ShrCoeff-Scat.txt", delimiter=",")
time17 = 8.00E-03
AllLumArray.append(data17)
ExpTimeArray.append(time17)

data18 = np.loadtxt("224-ShrCoeff-Scat.txt", delimiter=",")
time18 = 1.00E-02
AllLumArray.append(data18)
ExpTimeArray.append(time18)

data19 = np.loadtxt("225-ShrCoeff-Scat.txt", delimiter=",")
time19 = 1.25E-02
AllLumArray.append(data19)
ExpTimeArray.append(time19)

data20 = np.loadtxt("226-ShrCoeff-Scat.txt", delimiter=",")
time20 = 1.67E-02
AllLumArray.append(data20)
ExpTimeArray.append(time20)

data21 = np.loadtxt("227-ShrCoeff-Scat.txt", delimiter=",")
time21 = 2.00E-02
AllLumArray.append(data21)
ExpTimeArray.append(time21)

data22 = np.loadtxt("228-ShrCoeff-Scat.txt", delimiter=",")
time22 = 2.50E-02
AllLumArray.append(data22)
ExpTimeArray.append(time22)

data23 = np.loadtxt("229-ShrCoeff-Scat.txt", delimiter=",")
time23 = 3.33E-02
AllLumArray.append(data23)
ExpTimeArray.append(time23)

data24 = np.loadtxt("230-ShrCoeff-Scat.txt", delimiter=",")
time24 = 4.00E-02
AllLumArray.append(data24)
ExpTimeArray.append(time24)

data25 = np.loadtxt("231-ShrCoeff-Scat.txt", delimiter=",")
time25 = 5.00E-02
AllLumArray.append(data25)
ExpTimeArray.append(time25)

data26 = np.loadtxt("232-ShrCoeff-Scat.txt", delimiter=",")
time26 = 6.67E-02
AllLumArray.append(data26)
ExpTimeArray.append(time26)

data27 = np.loadtxt("233-ShrCoeff-Scat.txt", delimiter=",")
time27 = 7.69E-02
AllLumArray.append(data27)
ExpTimeArray.append(time27)

data28 = np.loadtxt("234-ShrCoeff-Scat.txt", delimiter=",")
time28 = 1.00E-01
AllLumArray.append(data28)
ExpTimeArray.append(time28)

data29 = np.loadtxt("235-ShrCoeff-Scat.txt", delimiter=",")
time29 = 1.25E-01
AllLumArray.append(data29)
ExpTimeArray.append(time29)

data30 = np.loadtxt("236-ShrCoeff-Scat.txt", delimiter=",")
time30 = 1.67E-01
AllLumArray.append(data30)
ExpTimeArray.append(time30)

data31 = np.loadtxt("237-ShrCoeff-Scat.txt", delimiter=",")
time31 = 2.00E-01
AllLumArray.append(data31)
ExpTimeArray.append(time31)

data32 = np.loadtxt("238-ShrCoeff-Scat.txt", delimiter=",")
time32 = 2.50E-01
AllLumArray.append(data32)
ExpTimeArray.append(time32)

data33 = np.loadtxt("239-ShrCoeff-Scat.txt", delimiter=",")
time33 = 3.03E-01
AllLumArray.append(data33)
ExpTimeArray.append(time33)

data34 = np.loadtxt("240-ShrCoeff-Scat.txt", delimiter=",")
time34 = 4.00E-01
AllLumArray.append(data34)
ExpTimeArray.append(time34)

data35 = np.loadtxt("241-ShrCoeff-Scat.txt", delimiter=",")
time35 = 5.00E-01
AllLumArray.append(data35)
ExpTimeArray.append(time35)

data36 = np.loadtxt("242-ShrCoeff-Scat.txt", delimiter=",")
time36 = 6.25E-01
AllLumArray.append(data36)
ExpTimeArray.append(time36)

data37 = np.loadtxt("243-ShrCoeff-Scat.txt", delimiter=",")
time37 = 7.69E-01
AllLumArray.append(data37)
ExpTimeArray.append(time37)

data38 = np.loadtxt("244-ShrCoeff-Scat.txt", delimiter=",")
time38 = 1.00E+00
AllLumArray.append(data38)
ExpTimeArray.append(time38)

data39 = np.loadtxt("245-ShrCoeff-Scat.txt", delimiter=",")
time38 = 1.30E+00
AllLumArray.append(data38)
ExpTimeArray.append(time38)

LogStepArray01 = []
for i in range (len(AllLumArray)):
    data00a = []
    data00b = []
    data00c = []
    data00d = []
    data00e = []
    data00f = []
    
    for j in range (len(AllLumArray[i])):
        k = AllLumArray[i][j]
        if k[6] <= thresh01:
            data00a.append(k,)
        if thresh01 < k[6] <= thresh02:
            data00b.append(k,)
        if thresh02 < k[6] <= thresh03:
            data00c.append(k,)
        if thresh03 < k[6] <= thresh04:
            data00d.append(k,)
        if thresh04 < k[6] <= thresh05:
            data00e.append(k,)
        if thresh05 < k[6] <= thresh06:
            data00f.append(k,)
    
    print (len(AllLumArray[i]))
    print (len(data00a))
    print (len(data00b))
    print (len(data00c))
    print (len(data00d))
    print (len(data00e))
    print (len(data00f))
    print (len(AllLumArray[i]) - (len(data00a) + len(data00b) + len(data00c) + len(data00d) + len(data00e) + len(data00f)))
    
    n = []
    for l in range (len(data00a)):
        m = data00a[l]
        n.append(m[6])
    o = np.sum(n)
    
    n = []
    for l in range (len(data00b)):
        m = data00b[l]
        n.append(m[6])
    p = np.sum(n)
    
    n = []
    for l in range (len(data00c)):
        m = data00c[l]
        n.append(m[6])
    q = np.sum(n)
    
    n = []
    for l in range (len(data00d)):
        m = data00d[l]
        n.append(m[6])
    r = np.sum(n)
    
    n = []
    for l in range (len(data00e)):
        m = data00e[l]
        n.append(m[6])
    s = np.sum(n)
    
    n = []
    for l in range (len(data00f)):
        m = data00f[l]
        n.append(m[6])
    t = np.sum(n)
    
    print(o)
    print(p)
    print(q)
    print(r)
    print(s)
    print(t)
    
    LogStepArray00 = [len(data00a),len(data00b),len(data00c),len(data00d),len(data00e),len(data00f),o,p,q,r,s,t]
    LogStepArray01.append(LogStepArray00)

CountAArray = []
CountBArray = []
CountCArray = []
CountDArray = []
CountEArray = []
CountFArray = []

for e in range (len(LogStepArray01)):
    CountAArray.append(LogStepArray01[e][0])
    CountBArray.append(LogStepArray01[e][1])
    CountCArray.append(LogStepArray01[e][2])
    CountDArray.append(LogStepArray01[e][3])
    CountEArray.append(LogStepArray01[e][4])
    CountFArray.append(LogStepArray01[e][5])

CumAArray = []
CumBArray = []
CumCArray = []
CumDArray = []
CumEArray = []
CumFArray = []

for e in range (len(LogStepArray01)):
    CumAArray.append(LogStepArray01[e][6])
    CumBArray.append(LogStepArray01[e][7])
    CumCArray.append(LogStepArray01[e][8])
    CumDArray.append(LogStepArray01[e][9])
    CumEArray.append(LogStepArray01[e][10])
    CumFArray.append(LogStepArray01[e][11]) 
    
plt.scatter(ExpTimeArray,CountAArray)
plt.scatter(ExpTimeArray,CountBArray)
plt.scatter(ExpTimeArray,CountCArray)
plt.scatter(ExpTimeArray,CountDArray)
plt.scatter(ExpTimeArray,CountEArray)
plt.scatter(ExpTimeArray,CountFArray)
plt.legend(['< 10^1', '>10^1 to 10^2', '>10^2 to 10^3', '>10^3 to 10^4', '>10^4 to 10^5', '>10^5 to 10^6'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.suptitle('# of Scatterers vs Exposure Time (Log Step Grouping)')
plt.xscale('log')
plt.xlim(9e-5,2)
plt.ylim(1,4e5)
plt.yscale('log')
plt.ylabel('Number of Scatterers')
plt.xlabel('Exposure Time (seconds)')
plt.savefig('ScatCountVExpTime-LogStep.jpg')
plt.show()

plt.scatter(ExpTimeArray,CumAArray)
plt.scatter(ExpTimeArray,CumBArray)
plt.scatter(ExpTimeArray,CumCArray)
plt.scatter(ExpTimeArray,CumDArray)
plt.scatter(ExpTimeArray,CumEArray)
plt.scatter(ExpTimeArray,CumFArray)
plt.legend(['< 10^1', '>10^1 to 10^2', '>10^2 to 10^3', '>10^3 to 10^4', '>10^4 to 10^5', '>10^5 to 10^6'],bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.suptitle('Cumulative Scatterer Luminosity vs Exposure Time (Log Step Grouping)')
plt.xscale('log')
plt.xlim(9e-5,2)
plt.ylim(1,2e9)
plt.yscale('log')
plt.ylabel('Luminosity (Arbitrary Units)')
plt.xlabel('Exposure Time (seconds)')
plt.savefig('ScatCumLumVExpTime-LogStep.jpg')
plt.show()

#MedianData = []
#meddata = []
#for a in range (len(AllLumArray)):
#    for b in range (len(AllLumArray[a])):
#        c = AllLumArray[a][b][6]
#        meddata.append(c,)
#    d = np.median(meddata)
#    MedianData.append(d,)
#    meddata = []

#plt.scatter(ExpTimeArray,MedianData)
#plt.suptitle('Median Scatterer Luminosity vs Exposure Time')
#plt.xscale('log')
#plt.xlim(9e-5,2)
#plt.ylim(1,5e3)
#plt.yscale('log')
#plt.ylabel('Luminosity (Arbitrary Units)')
#plt.xlabel('Exposure Time (seconds)')
#plt.savefig('MedianScatLumVExpTime-LinLin.jpg')
#plt.show()