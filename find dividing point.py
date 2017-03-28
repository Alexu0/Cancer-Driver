#select best two dividing point
import numpy as np
from sklearn.naive_bayes import BernoulliNB
from sklearn.model_selection import train_test_split
clf=BernoulliNB()
x4=np.load("/Users/apple/Desktop/result/1.2/cleaned_x4.npy")
y4=np.load("/Users/apple/Desktop/result/1.2/cleaned_y4.npy")
data4=x4[1:]
neg=np.arange(y4.min(),np.median(y4),50)
pos=np.arange(np.median(y4),y4.max(),50)
diving_point=np.zeros((len(neg),len(pos)))
for i in range(len(neg)):
	for j in range(len(pos)):
		t4=np.zeros(len(y4))
		for q in range(len(y4)):
			if y4[q]<=neg[i]:
				t4[q]=0
			elif y4[q]>=pos[j]:
				t4[q]=2
			else:
				t4[q]=1
		dn4=[]
		for q in range(len(t4)):
			if t4[q]==1:
				dn4+=[q]
		dn4=np.array(dn4)
		target=np.delete(t4,dn4,0)
		data=np.delete(data4,dn4,0)
		x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.3)
		clf.fit(x_train,y_train)
		diving_point[i][j]=clf.score(x_test,y_test)
