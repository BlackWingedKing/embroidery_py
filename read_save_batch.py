import numpy as np
import pyembroidery as pe
import cv2
import glob

indir = './designs/'
inindir = 'design/'
pngdir = './png/'
sdir = './saved/'

ncount = len(indir) + len(inindir)

ext = '*.pes'
pngext = '.png'
sext = '.DST'

filelist = []

for dfile in glob.glob(indir + inindir + ext):
    filelist.append(dfile)

print('no of files found = ', len(filelist))

for f in filelist:
    print('file started ', f[ncount:])
    pattern = pe.read_pec(f)
    pngname = pngdir + inindir + f[ncount:-4] + pngext
    pe.write_png(pattern, pngname)
    img = cv2.imread(pngname, cv2.IMREAD_UNCHANGED)
    alpha_channel = img[:, :, 3]
    _, mask = cv2.threshold(alpha_channel, 254, 255, cv2.THRESH_BINARY)  # binarize mask
    color = img[:, :, :3]
    new_img = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
    cv2.imwrite(pngname, new_img)

    sname = sdir + inindir + f[ncount:-4] + sext
    pe.write_dst(pattern, sname)
    
