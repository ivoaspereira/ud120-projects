#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
#clf = svm.SVC(kernel="linear")
clf = svm.SVC(kernel="rbf",C=10000.0)

### reduces the length of the training dataset
features_train = features_train[:int(len(features_train)/100)]
labels_train = labels_train[:int(len(labels_train)/100)]


### train
t0 = time()
clf.fit(features_train, labels_train)
print("training time:", round(time()-t0, 3), "s")

### test
t0 = time()
pred = clf.predict(features_test)
print("testing time:", round(time()-t0, 3), "s")


### evaluate
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred,labels_test)
print("accuracy:", round(acc,3))

#quiz 36
print("element 10: ", pred[10])
print("element 26: ", pred[26])
print("element 50: ", pred[50])

#quiz 37
lst = list(pred)
print("total of Chris (1) class:  ", lst.count(1))

#########################################################


