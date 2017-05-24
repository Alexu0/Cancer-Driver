#different type of cancer prediction
import pdb
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LogisticRegressionCV
from sklearn.feature_selection import *
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import matplotlib.pyplot as plt
print("module importation finished")

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
    #clf=LogisticRegression()
    x_train, x_test, y_train, y_test = train_test_split(xr2[1:],yr,test_size=0.2)
    clf=LogisticRegressionCV(Cs=[0.001,0.01,0.1,1.,10.,100.,1000.],penalty='l2',max_iter=1000,cv=10).fit(x_train,y_train)
    #clf.fit(x_train,y_train)
    accuracy=clf.score(x_train,y_train)
    scores=clf.score(x_test,y_test)
    return(accuracy,scores,idg,clf.coef_)

def output_domain_name(dn,num,coef,idl,n):
    #pdb.set_trace()
    gids=num[idl==1]
    td1,td2=np.percentile(coef,(10,90))
    nai=gids[coef<=td1]#new antigen ids
    emi=gids[coef>=td2]#escaping mechanism ids
    naw="\n".join(dn[nai].tolist())
    emw="\n".join(dn[emi].tolist())
    fn="C:/Users/N1604313C/Desktop/python_projext/selected_domain_names/new_antigen_"+str(n)+".txt"
    fe="C:/Users/N1604313C/Desktop/python_projext/selected_domain_names/escaping_mechaism_"+str(n)+".txt"
    f=open(fn,"w")
    f.write(naw)
    f.close()
    f=open(fe,"w")
    f.write(emw)
    f.close()
    return()


#choose cancer type idt means id_cancer_type
x=np.load("C:/Users/N1604313C/Desktop/python_projext/npy_datasets1.1/cleaned_mutation_data_x.npy")
x=x.astype(np.int)
y=np.load("C:/Users/N1604313C/Desktop/python_projext/npy_datasets1.1/mutation_score_digital_y.npy")
f=open("C:\Users\N1604313C\Desktop\python_projext\protein_name.txt")
dn=f.read()
f.close()
dn=dn.split("\n")
dn=np.array(dn)
#t=0
num=np.arange(83641)
good_list=np.array([1,11,12,13,14,15,16])

print("prepation finished")
#print(sub_cancer_type(x,y,0))
mos=np.zeros((21,3))
ids=np.zeros((21,83641))
idn=[0]*21

for i in range(21):
    mos[i][0]=i
    mos[i][1],mos[i][2],ids[i],idn[i]=sub_cancer_type(x,y,i)
    print(i)
#idn=np.array(idn)
#for i in good_list:
    #write out the domain_name
    #output_domain_name(dn,num,idn[i][0],ids[i],i)
#print("file stores domain name successfully created")    
#print("information is stored at mos")
