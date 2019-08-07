import numpy as np
import pyembroidery as pe
import cv2

pattern = pe.read_pes('shadow-rose.PES')
pe.write_png(pattern, '003.png')
img = cv2.imread('003.png', cv2.IMREAD_UNCHANGED)
alpha_channel = img[:, :, 3]
_, mask = cv2.threshold(alpha_channel, 254, 255, cv2.THRESH_BINARY)  # binarize mask
color = img[:, :, :3]
new_img = cv2.bitwise_not(cv2.bitwise_not(color, mask=mask))
cv2.imwrite('t.png', new_img)
nimg = cv2.imread('t.png')
cv2.imshow('t', nimg)
cv2.waitKey(0)