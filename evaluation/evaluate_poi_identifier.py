#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson13_keys.pkl')
labels, features = targetFeatureSplit(data)



### your code goes here 

from sklearn.cross_validation import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

acc = accuracy_score(pred,labels_test)

print("accuracy:", round(acc,3))

print("How many POIs are in the test set for your POI identifier?", len([e for e in labels_test if e == 1.0]))
print("How many people total are in your test set?",len(labels_test))
print("If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?", 1-4/29)
print("Do you get any true positives? ",len([i for i,j in zip(labels_test, pred) if i == 1.0 and i == j]))

from sklearn.metrics import precision_score, recall_score

precision = precision_score(labels_test,pred)
recall = recall_score(labels_test,pred)

print("What is the precision?",precision)
print("What is the recall?",recall)


