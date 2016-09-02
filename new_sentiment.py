#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymorphy2
from pymystem3 import Mystem
from sklearn.feature_extraction.text import HashingVectorizer
from  sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators = 100, criterion='entropy')
vz = HashingVectorizer()

def getA(text):
    '''Get all adv'''
    m = Mystem()
    w = []
    for a in m.analyze(text):
      try:
        atype = (a['analysis'][0]['gr'][0])
      except:
        atype =''
      if atype == 'A':
        w.append(a['analysis'][0]['lex'])
    return w
  
def get_inf(text):
    w=[]
    m = Mystem()
    for a in m.analyze(text):
      try:
        w.append(a['analysis'][0]['lex'])
      except:
        pass
    return w
  
def norm(s):
  morph = pymorphy2.MorphAnalyzer()
  t = morph.parse(s)
  if ('ADJF' or 'ADJS' or 'COMP') in t[0].tag:
    return t[0].normal_form
    
def man_norm(s):
  w=[]
  for a in s:
    w.append(norm(a))  
  return w

def prep():
  with open('out.txt','r',encoding='utf8') as fo,\
       open('in.txt','w',encoding='utf8') as fi,\
       open('x.txt','w',encoding='utf8') as fx:
    for o in fo:
      s = ''
      s = o
      fi.write(str(s).split('#')[1])
      fx.write(str(s).split('#')[0]+'\n')
      
def train():
  prep()
  with open('in.txt','r',encoding='utf8') as f:
    x=vz.fit_transform(f)
  with open('x.txt','r',encoding='utf8') as f:
    t = [a for a in f]
  model.fit(x, t)

def pred(text):
  return model.predict(vz.transform(get_inf(text)))

if __name__ == '__main__':
  train()
  print(pred('все хорошо'))

 

    
    