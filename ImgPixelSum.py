import numpy as np
import tifffile as tiff
raw = tiff.imread('TEST01.tif') ### make sure to edit filename and remove one of the "f"s. Otherwise, it won't work.
img02 = np.array(raw)
r02 = np.split(img02,3, axis=2)
rb = r02[0]
gb = r02[1]
bb = r02[2]
gray02 = (rb/3 + gb/3 + bb/3)
gray021 = np.around(gray02,0)
gray022 = gray021.astype(np.uint16)
tiff.imsave('TEST01Gray.tif',gray022)

raw1 = tiff.imread('TEST01Gray.tif')
arr01 = np.array(raw1)
unravel01 = np.ravel(arr01)
arr02 = np.sum(arr01)
unravel02 = np.sum(unravel01)

print (arr02, unravel02)