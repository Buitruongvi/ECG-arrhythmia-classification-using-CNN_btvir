




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


NOR = list()  
LBB = list()
RBB	= list()
APC = list()
PVC = list()
PAB = list()
QQQ = list()

path='/Users/vibuitruong/Desktop/LV_2020/MIT_BIH_DATABASE/size_312/size_312_loc/'
filename=['NOR','LBB','RBB','APC','PVC','PAB','QQQ']
N=np.array(pd.read_csv(path+filename[0]+'.csv',skiprows=1,header=None))
L=np.array(pd.read_csv(path+filename[1]+'.csv',skiprows=1,header=None))
R=np.array(pd.read_csv(path+filename[2]+'.csv',skiprows=1,header=None))
A=np.array(pd.read_csv(path+filename[3]+'.csv',skiprows=1,header=None))
V=np.array(pd.read_csv(path+filename[4]+'.csv',skiprows=1,header=None))
P=np.array(pd.read_csv(path+filename[5]+'.csv',skiprows=1,header=None))
Q=np.array(pd.read_csv(path+filename[6]+'.csv',skiprows=1,header=None))
#NOR = list()   
for j in range(len(N)):   
    N2=np.lib.pad(N[j], (0,1), 'constant', constant_values=(0)) #thêm số type vào hàng cuối cùng 361
    NOR.append(N2)

#LBB = list()   
for j in range(len(L)):  
    L2=np.lib.pad(L[j], (0,1), 'constant', constant_values=(1)) #thêm số type vào hàng cuối cùng 361
    LBB.append(L2)

#RBB = list()   
for j in range(len(R)):   
    R2=np.lib.pad(R[j], (0,1), 'constant', constant_values=(2)) #thêm số type vào hàng cuối cùng 361
    RBB.append(R2)

#APC = list()   
for j in range(len(A)):   
    A2=np.lib.pad(A[j], (0,1), 'constant', constant_values=(3)) #thêm số type vào hàng cuối cùng 361
    APC.append(A2)

#PVC = list()   
for j in range(len(V)):   
    V2=np.lib.pad(V[j], (0,1), 'constant', constant_values=(4)) #thêm số type vào hàng cuối cùng 361
    PVC.append(V2)

#PAB = list()   
for j in range(len(P)):
    P2=np.lib.pad(P[j], (0,1), 'constant', constant_values=(5)) #thêm số type vào hàng cuối cùng 361
    PAB.append(P2)

#QQQ = list()   
for j in range(len(Q)):   
    Q2=np.lib.pad(Q[j], (0,1), 'constant', constant_values=(6)) #thêm số type vào hàng cuối cùng 361
    QQQ.append(Q2)

#NOR
nor= np.random.randint(0,40000,int(len(N)*0.2))
NOR_TEST=list()

for i in range(len(nor)):
    NOR_TEST.append(NOR[nor[i]])
for i in range(len(nor)):
    del NOR[nor[i]]
NOR_TRAIN=NOR   
#LBB
lbb= np.random.randint(0,4000,int(len(L)*0.2))
LBB_TEST=list()

for i in range(len(lbb)):
    LBB_TEST.append(LBB[lbb[i]])
for i in range(len(lbb)):
    del LBB[lbb[i]]
LBB_TRAIN=LBB  
#RBB
rbb= np.random.randint(0,2000,int(len(R)*0.2))
RBB_TEST=list()

for i in range(len(rbb)):
    RBB_TEST.append(RBB[rbb[i]])
for i in range(len(rbb)):
    del RBB[rbb[i]]
RBB_TRAIN=RBB   
#APC
apc= np.random.randint(0,600,int(len(A)*0.2))
APC_TEST=list()

for i in range(len(apc)):
    APC_TEST.append(APC[apc[i]])
for i in range(len(apc)):
    del APC[apc[i]]
APC_TRAIN=APC   
#PVC
pvc= np.random.randint(0,1000,int(len(V)*0.2))
PVC_TEST=list()

for i in range(len(pvc)):
    PVC_TEST.append(PVC[pvc[i]])
for i in range(len(pvc)):
    del PVC[pvc[i]]
PVC_TRAIN=PVC   
#PAB
pab= np.random.randint(0,1100,int(len(P)*0.2))
PAB_TEST=list()

for i in range(len(pab)):
    PAB_TEST.append(PAB[pab[i]])
for i in range(len(pab)):
    del PAB[pab[i]]
PAB_TRAIN=PAB   
#QQQ
qqq= np.random.randint(0,1500,int(len(Q)*0.2))
QQQ_TEST=list()

for i in range(len(qqq)):
    QQQ_TEST.append(QQQ[qqq[i]])
for i in range(len(qqq)):
    del QQQ[qqq[i]]
QQQ_TRAIN=QQQ


TRAIN_DATA = NOR_TRAIN + LBB_TRAIN + RBB_TRAIN + APC_TRAIN + PVC_TRAIN + PAB_TRAIN + QQQ_TRAIN
da=np.asarray(TRAIN_DATA)
df = pd.DataFrame(data=da[0:,0:])
df=df.sample(frac=1)
export_csv = df.to_csv (r'C:/Users/thin/Desktop/AI_ECG/TRAIN_DATA_paper_afterfilter.csv', index = None, header=None)


TEST_DATA = NOR_TEST + LBB_TEST + RBB_TEST + APC_TEST + PVC_TEST + PAB_TEST + QQQ_TEST
db=np.asarray(TEST_DATA)
dt = pd.DataFrame(data=db[0:,0:]) 
export_csv = dt.to_csv (r'C:/Users/thin/Desktop/AI_ECG/TEST_DATA_paper_afterfilter.csv', index = None, header=None)