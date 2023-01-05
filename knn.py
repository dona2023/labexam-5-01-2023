
#import libraries
import sklearn

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_slr
import pandas as pd

#load csv
slrdata = datasets.load_slr()
x=slrdata.data
y=slrdata.target


x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1, random_state=42)
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)

y_pred=knn.predict(x_test)
print(y_pred)

c=knn.predict(x_train)
acc= metrics.accuracy_score(x_test,c)
print(c)
print(acc)
