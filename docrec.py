#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
#import argparse
import cv2

def get_ct():
  image = cv2.imread('img.jpg')
  # переобразуем в оттенки серого
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # размытие по гауссу
  sm = cv2.blur(gray, (9,9));
  # фильтр Собеля
  gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
  gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)
 
  # разница по вертикальному/горизонтальному градиенту
  gradient = cv2.subtract(gradX, gradY)
  gradient = cv2.convertScaleAbs(gradient)
  # преобразуем в Ч/Б 
  # ToDo: попробовать разные
  (_, thresh) = cv2.threshold(gradient, 225, 255, cv2.THRESH_BINARY)
  # поиск контуров
  img, contours, hierarchy = cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
  # находим самый большой контур
  c = sorted(contours, key = cv2.contourArea, reverse = True)[0]
 
  # расчитываем область
  rect = cv2.minAreaRect(c)
  box = np.int0(cv2.boxPoints(rect))
  print (box)
 
  x,y,w,h = cv2.boundingRect(box)
  # вырезаем документ
  img2 = cv2.getRectSubPix(image,(w,h),(x+w/2,y+h/2))

  cv2.imwrite('out.png',img2 )
  
if __name__ == '__main__':
  get_ct()
