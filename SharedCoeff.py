import re
import numpy as np

lines = open( 'LHOX262als.txt', "r" ).readlines()[::2]
textfile = open("testtext01.txt", "w")
textfile.writelines(lines)
l = []
for i in range(np.max(len(lines))):
    j = re.sub(' +', ',', lines[i])
    k = np.fromstring(j, sep=',')
    l.append(k)

m = np.array(l)

starnum = []
starnum.append(m[:,0])
starnum01 = np.asarray(starnum)
starnum01 = starnum01.astype(np.float)


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

zmagerror = []
zmagerror.append(m[:,4])
zmagerror01 = np.asarray(zmagerror)
zmagerror01 = zmagerror01.astype(np.float)
zlum = 10**(-(zmag01/2.5))
zlumcoeff = 1638324779.6286438
zlum01 = zlum * zlumcoeff

dataset = np.vstack((starnum01,xcenter01,ycenter01,zmag01,zmagerror01,zlum,zlum01))
dataset01 = np.transpose(dataset)
dataset02 = dataset01.astype(np.float)
np.savetxt('262-ShrCoeff-Scat.txt',dataset02,delimiter=',', fmt='%.9f')