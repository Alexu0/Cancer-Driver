#function module
import numpy as np
def getsubdata(sn,target,data):
    dn=[]
    for i in range(len(target)):
        if target[i][0]!=sn:
            dn+=[i]
    dn=np.array(dn)
    return(np.delete(target,dn,0),np.delete(data,dn,0))

