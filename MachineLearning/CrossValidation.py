from RFESelection import *
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import NuSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier

models = []
models.append(("Log Reg",LogisticRegression()))
models.append(("Linear Disc",LinearDiscriminantAnalysis()))
models.append(("KNeighbours",KNeighborsClassifier()))
models.append(("GaussianNB",GaussianNB()))
models.append(("Decision Tree",DecisionTreeClassifier()))
models.append(("SVC",NuSVC()))
models.append(("RandomForestClassifier",RandomForestClassifier(n_estimators=200)))
models.append(("Gradient Decent",SGDClassifier()))

for name, model in models:
	kfold = KFold(n_splits=10, random_state=7)
	cv_results = cross_val_score(model, X, Y, cv=kfold, scoring="accuracy")
	msg = "%s: %.2f (%f)" % (name, cv_results.mean()*100, cv_results.std())
	print(msg)