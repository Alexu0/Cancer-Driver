#function module
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
def getsubdata(sn,target,data):
    dn=[]
    for i in range(len(target)):
        if target[i][0]!=sn:
            dn+=[i]
    dn=np.array(dn)
    return(np.delete(target,dn,0),np.delete(data,dn,0))

def getscores(target,data):
    ys=target.tolist()
    ys.sort()
    t=np.zeros(len(target))
    neg=ys[19]
    pos=ys[-20]
    for i in range(len(t)):
        if target[i]<=neg:
            t[i]=0
        elif target[i]>=pos:
            t[i]=2
        else:
            t[i]=1
    dn=[]
    for i in range(len(t)):
        if t[i]==1:
            dn+=[i]
    dn=np.array(dn)
    y=np.delete(t,dn,0)
    x=np.delete(data,dn,0)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)
    clf=BernoulliNB()
    clf.fit(x_train,y_train)
    scores=clf.score(x_test,y_test)
    return(scores)
