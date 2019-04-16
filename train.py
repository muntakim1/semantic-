# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 23:13:56 2017

@author: pranto
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import io
import codecs
import gensim, logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim.models import Word2Vec
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import pandas as pd
from matplotlib import animation

class FileToSent(object):
    def __init__(self,filename):
        self.filename=filename
    def __iter__(self):
        for line in open(self.filename,'r', encoding='utf-8'):
            lines = [x for x in line.split()]
            yield lines
       
sentences = gensim.models.word2vec.PathLineSentences('E:\Workspace\\InputAll')
model = gensim.models.Word2Vec(sentences=sentences,window=40,min_count=0,workers=4,hs=1,size=1000)    
model.save('test%.model')
plt.rc('font',**{'sans-serif':'Vrinda','family':'sans-serif'})


