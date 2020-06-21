"""
Created on Wed Mar 18 16:39:07 2020

@author: Admin
"""

def clear_all():
    from IPython import get_ipython
    get_ipython().magic('reset -sf')
clear_all()
    

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

path='/Users/vibuitruong/Desktop/LV_2020/MIT_BIH_DATABASE/giua_500n/'
filename='QQQ'
S=np.array(pd.read_csv(path+filename+'.csv',skiprows=1,header=None))
plt.close('all')


plt.boxplot(S, boxprops=dict(color='royalblue'),
               whiskerprops=dict(color='royalblue'),
               flierprops=dict(markeredgecolor='salmon', marker='+',))