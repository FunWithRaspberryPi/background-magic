import cv2
import numpy as np 

img1=cv2.imread('cr73.jpg')
img2=cv2.imread('opencv2.png')

rows,cols,channels=img2.shape
roi=img1[0:rows,0:cols]
#select the area where the img2 will be placed

img2gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(img2gray,250,255,cv2.THRESH_BINARY_INV)
cv2.namedWindow('mask',cv2.WINDOW_NORMAL)
cv2.imshow('mask',mask)
#check the itensity . if the itensity is less than 250 then make it white
mask_inv=cv2.bitwise_not(mask)
# invert the mask pixel by pixel

img1_bg=cv2.bitwise_and(roi,roi,mask=mask_inv)
# if mask(i)!=0 then img1_bg(i) = roi(i) and roi(i) else img1_bg(i)=mask(i)
cv2.namedWindow('img1',cv2.WINDOW_NORMAL)
cv2.namedWindow('roi',cv2.WINDOW_NORMAL)
cv2.namedWindow('mask_inv',cv2.WINDOW_NORMAL)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img1',img1_bg)
cv2.imshow('roi',roi)
cv2.waitKey(0)

img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
cv2.namedWindow('img2_fg',cv2.WINDOW_NORMAL)
cv2.imshow('img2_fg',img2_fg)

dst=cv2.add(img1_bg,img2_fg)
# adds each pixel of img1_bg(i)+img2_fg(i) . if res>=255 then res=255 else res=res

img1[0:rows,0:cols]=dst
cv2.namedWindow('image',cv2.WINDOW_NORMAL)
cv2.imshow('image',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()