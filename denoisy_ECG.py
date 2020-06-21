"""
Created on Tue Mar 31 10:15:18 2020

@author: vibuitruong
"""
def clear_all():
    from IPython import get_ipython
    get_ipython().magic('reset -sf')
clear_all()
import wfdb
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def wavelet_denoise(S,lev,wavename): #trong dau () la inputdata, lev: level
    import pywt as pw #thu vien wavelet
    Cf=pw.wavedec(S,wavename,level=lev) #ptich tin hieu roi rac cho tin hieu vao
    m=len(S)
    An=pw.upcoef('a',Cf[0],wavename,level=lev,take=m)
    return An
#record1 = wfdb.Record(recordname='100.dat', fs=360, nsig=1, siglen=1000, filename=['100.dat'])
#data = np.genfromtxt('/Users/vibuitruong/Desktop/LV_2020/MIT_BIH_DATABASE/mit-bih-arrhythmia-database-1.0.0/100.dat',delimiter=',') 
NN = list() #Normal beat
LL = list() #Left bundle branch block beat
RR = list() #Right bundle branch block beat
AA = list() #Atrial premature beat
a = list() #Aberrated atrial premature beat
J = list() #Nodal (junctional) premature beat
S = list() #Supraventricular premature beat
VV = list() #Premature ventricular contraction
F = list() #Fusion of ventricular and normal beat
s = list() #Start of ventricular flutter/fibrillation
v = list() #Ventricular flutter wave
K = list() #End of ventricular flutter/fibrillation
e = list() #Atrial escape beat
n = list() #Nodal (junctional) escape beat
E = list() #Ventricular escape beat
PP = list() #Paced beat
f = list() #Fusion of paced and normal beat
x = list() #Non-conducted P-wave (blocked APB)
QQ = list() #Unclassifiable beat
I = list() #Isolated QRS-like artifact

N_record=list(); N_nb=list()
NOR = list()  
LBB = list()
RBB	= list()
APC = list()
PVC = list()
PAB = list()
QQQ = list()
CC = []
DD = []

#name=list(['103'])

name=list(['100','104','108','113','117','122','201','207','212','217','222','231','101','105','109','118','123',
               '202','208','213','219','223','232','102','106','111','115','119','124','209','214','220','228','233',
               '103','107','112','116','121','200','205','210','221','230','234'])

   
for i in range(len(name)):
    annn = wfdb.rdann(name[i], 'atr')
    ecgrecord = wfdb.rdsamp(name[i], channels = [0])
    ann=annn.sample
    anntype=annn.symbol
    ann = np.array(ann)[:]
    anntype = list(anntype)[1:-1]
    data=ecgrecord[0]
    data=np.array(data).reshape(650000,)
    wavename='sym8'
    level=2
    data=wavelet_denoise(data,level,wavename) - wavelet_denoise(data,12,wavename)

