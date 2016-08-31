#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import uu
from pymystem3 import Mystem

def printRAW(*Text):  
    RAWOut = open(1, 'w', encoding='utf8', closefd=False)  
    print(*Text, file=RAWOut)  
    RAWOut.flush()  
    RAWOut.close()   

def getA(text):   
  m = Mystem()
  w = []
  #f = open('output.txt','w')
  for a in m.analyze(text):
    try:
      type = (a['analysis'][0]['gr'][0])
      #print (a['text'].encode('utf8').decode('utf-16'))
    except: 
      type =''
    if type == 'A':
      w.append(a['analysis'][0]['lex'])
  return w
      
if __name__ == '__main__':
  #text = u'Красивая красное мама красиво мыла раму'
  #printRAW(getA(text))
  f = open('12193260.txt','r',encoding='utf8')
  f2 = open('output.txt','w',encoding='utf8')
  w = getA(f.read())
  w = list(set(w))
  for a in w:
    f2.write(a+'\n')
  f2.close()
  f.close()