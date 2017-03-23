#feature selection
import numpy as np
from scipy.stats import pearsonr
x=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/numpy_data/mutationsite_x.npy")
print("load completed")
y=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/numpy_data/mutationscore_y.npy")
y=y.reshape(5164,)
x=np.double(x)
y=np.double(y)
sto=np.array([])#to store the ordinal number of feature
count=0
for i in range(83641):
    w=x[:,i]
    pea=pearsonr(y,w)
    sto=np.append(sto,np.nan_to_num(pea[0]))
    if count%836==0:
        print("percentage:%d" %(count/836))
    count+=1
