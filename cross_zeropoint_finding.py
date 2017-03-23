import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
clf=BernoulliNB()
x=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/npy_datasets1.1/cleaned_mutation_data_x.npy")
y=np.load("/Users/apple/Desktop/domainXplorer-master/example_files/npy_datasets1.1/mutation_score_digital_y.npy")
x=np.delete(x,0,0)
data=x.astype(np.int)
print("data prepared")
zero_point=np.arange(y[:,1].min(),y[:,1].max(),100)
scores=np.array([0.0]*100)
target=np.array([1]*len(y))
print("target prepared")
for zp in range(len(zero_point)):
    for i in range(len(target)):
        if y[i][1]>=zero_point[zp]:
            target[i]=1
        else:
            target[i]=0
    #location
    x_train, x_test, y_train, y_test = train_test_split(data,target,test_size=0.1)
    clf.fit(x_train,y_train)
    scores[zp]=clf.score(x_test,y_test)
    print("this is the "+str(zp)+" run")
    
