import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
import sklearn.metrics as sm
clf=BernoulliNB()
x=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/npy_datasets1.1/cleaned_mutation_data_x.npy")
y=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/npy_datasets1.1/mutation_score_digital_y.npy")
x=np.delete(x,0,0)
data=x.astype(np.int)
del x
print("data prepared")
zero_point=np.arange(y[:,1].min(),y[:,1].max(),56)
scores=np.array([0.0]*len(zero_point))
scores1=np.array([0.0]*len(zero_point))
target=np.array([1]*len(y))
print("target prepared")
for zp in range(len(zero_point)):
    c0=0#for class 0
    c1=0#for class 1
    fm0=1#for class 0
    fm1=1#for class 1
    for i in range(len(target)):
        if y[i][1]>=zero_point[zp]:
            target[i]=1
        else:
            target[i]=0
    #location
    x_train, x_test, y_train, y_test = train_test_split(data,target,test_size=0.3)
    clf.fit(x_train,y_train)
    te=clf.predict(x_test)
    for i in range(len(te)):
        if y_test[i]==0:
            fm0+=1
            if te[i]==y_test[i]:
                c0+=1
        elif y_test[i]==1:
            fm1+=1
            if te[i]==y_test[i]:
                c1+=1
    scores[zp]=c0/fm0
    scores1[zp]=c1/fm1
    print("this is the "+str(zp)+" run")
    
