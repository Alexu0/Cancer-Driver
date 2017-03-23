#transfer txt to readable data
import numpy as np
f=open("/Users/apple/Desktop/domainXplorer-master/example_files/cycle 2/for_matlab_anlyze.txt")
total=f.read()
f.close()
total=total.split("\n")
x=np.array([])
y=np.array([])
zz=1
for i in total:
    if i!=total[0] and i!="":
        isp=i.split(" ")
        y=np.append(y,np.array(isp[1],dtype=np.float))
        isp[0:2]=[]
        isp="".join(isp)
        x=np.append(x,np.fromstring(isp,dtype=np.int8)-48)
        if zz%50==0:
            print(zz)
        zz+=1
x=x.reshape(-1,83641)
y=y.reshape(-1,1)
np.save("/Users/apple/Desktop/domainXplorer-master/example_files/numpy_data/mutationsite_x",x)
np.save("/Users/apple/Desktop/domainXplorer-master/example_files/numpy_data/mutationscore_y",y)
del total
