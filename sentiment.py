#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import uu
from pymystem3 import Mystem
import re
from sklearn.feature_extraction.text import CountVectorizer

def printRAW(*Text):
    RAWOut = open(1, 'w', encoding='utf8', closefd=False)
    print(*Text, file=RAWOut)
    RAWOut.flush()
    RAWOut.close()
class emotion:
  m = Mystem()
  emotion_dictonary = {}

  def getA(self,text):
    '''Get all adv'''
    w = []
    for a in self.m.analyze(text):
      try:
        atype = (a['analysis'][0]['gr'][0])
      except:
        atype =''
      if atype == 'A':
        w.append(a['analysis'][0]['lex'])
    return w

  def get_inf(self,text):
    w=[]
    for a in self.m.analyze(text):
      try:
        w.append(a['analysis'][0]['lex'])
      except:
        pass
    return w

  def add(self,text):
    try:
      self.emotion_dictonary[text]=len(self.emotion_dictonary)
    except:
      pass


  def get_vector(self,mass):
    v=[]
    for a in mass:
      v.append(self.emotion_dictonary[a])
    return v

def main():
  m = Mystem()
  vz = CountVectorizer(preprocessor=emotion.getA)
  with open('stem.txt','r',encoding='utf8') as f:
    X = vz.fit_transform(f)
  print (X[0])

def sste():
  with open('12193260.txt','r',encoding='utf8') as f, open('stem.txt','w',encoding='utf8') as f2:
    for a in f:
      if a != ' ':
        for i in emotion.get_inf(emotion,a):
          f2.write(i+' ')
        #f2.write('\n')


if __name__ == '__main__':
  main()
  #sste()



def default():
  f = open('12193260.txt','r',encoding='utf8')
  l = re.findall('[–]{1}\s[^a-zA-Z0-9_]{1,}[.?!]', f.read())
  for a in l:
    if a !='':
      inf = (emotion.getA(emotion,a))
      for i in inf:
        emotion.add(emotion,i)

  #printRAW(emotion.emotion_dictonary)
  for a in l:
    if a != '':
      printRAW(a)
      inf = (emotion.getA(emotion,a))
      print(emotion.get_vector(emotion,inf))
      #printRAW(inf)
  #printRAW(emotion.emotion_dictonary)
  f.close()
