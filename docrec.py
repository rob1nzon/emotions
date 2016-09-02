#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
#import argparse
import cv2

def get_ct():
  image = cv2.imread('img.jpg')
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  sm = cv2.blur(gray, (9,9));
  gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
  gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
 
  # subtract the y-gradient from the x-gradient
  gradient = cv2.subtract(gradX, gradY)
  gradient = cv2.convertScaleAbs(gradient)

  (_, thresh) = cv2.threshold(gradient, 225, 255, cv2.THRESH_BINARY)
  img, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  c = sorted(contours, key = cv2.contourArea, reverse = True)[0]
 
  # compute the rotated bounding box of the largest contour
  rect = cv2.minAreaRect(c)
  box = np.int0(cv2.boxPoints(rect))
  print (box)
 
  # draw a bounding box arounded the detected barcode and display the
  # image
  #img = cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
  x,y,w,h = cv2.boundingRect(box)
  img2 = cv2.getRectSubPix(image,(w,h),(x+w/2,y+h/2))

  cv2.imwrite('out.png',img2 )
  
if __name__ == '__main__':
  get_ct()