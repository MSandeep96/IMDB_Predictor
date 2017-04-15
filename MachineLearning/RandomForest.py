from RFESelection import *
# Importing Libraries
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import cPickle

X_train, X_test, Y_train, Y_test = train_test_split(X, Ystr, test_size = 0.15, random_state = 0)

# Fitting Random Forest Classification to the Training set
classifier = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state=0,
									class_weight='balanced', n_jobs=-1)

classifier.fit(X_train, Y_train.ravel())

#with open('MyClassifier.pkl', 'wb') as fid:
#    cPickle.dump(classifier, fid)

# Predicting the Test set results
Y_pred = classifier.predict(X_test)
Y_pred = Y_pred.reshape(-1,1)

final_accuracy = accuracy_score(Y_test,Y_pred,normalize=True,sample_weight=None)

print 'Accuracy = ',final_accuracy*100, '%'