#different type of cancer prediction
import pdb
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import *
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB

def sub_cancer_type(x,y,t):
#choose cancer type idt means id_cancer_type

    #pdb.set_trace()
    idt=y[:,0]==t
    yt=y[idt]
    xt=np.r_[x[0].reshape(1,len(x[0])),x[1:][idt]]
    yth1,yth2=np.percentile(yt[:,1],(33,66))
    yr=np.array(yt[:,1],copy=True)
    id1=yr<=yth1
    id2=yr>=yth2
    yr[id1]=0
    yr[id2]=1
    yr=yr[np.logical_or(id1,id2)]
    xr=np.array(xt,copy=True)
    xr=np.r_[xr[0].reshape(1,len(xr[0])),xr[1:][np.logical_or(id1,id2)]]

#feature selection with chi2
    sp = SelectPercentile(chi2,percentile=50)
    sp.fit(xr[1:],yr)
    idg=sp.pvalues_<=0.1
    xr2=xr[:,idg]

#LogicticRegression
    clf=LogisticRegression()
    x_train, x_test, y_train, y_test = train_test_split(xr2[1:],yr,test_size=0.2)
    clf.fit(x_train,y_train)
    accuracy=clf.score(x_train,y_train)
    scores=clf.score(x_test,y_test)
    return(accuracy,scores)




#choose cancer type idt means id_cancer_type
x=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/npy_datasets1.1/cleaned_mutation_data_x.npy")
x=x.astype(np.int)
y=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/npy_datasets1.1/mutation_score_digital_y.npy")
#t=0

print("prepation finished")
#print(sub_cancer_type(x,y,0))
mos=np.zeros((21,3))
for i in range(21):
    mos[i][0]=i
    mos[i][1],mos[i][2]=sub_cancer_type(x,y,i)
    print(i)
print("information is stored at mos")
