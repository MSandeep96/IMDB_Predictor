from Normalisation import *
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier

NUM_FEATURES_WANTED = 15

#Lets pick the important features
model = RandomForestClassifier()
rfe = RFE(model,NUM_FEATURES_WANTED)
rfe = rfe.fit(X,Ystr)

#Drop the unimportant features
drop_list = []
for i in range(0,len(rfe.support_)):
	if not rfe.support_[i]:
		drop_list.append(i)
X = np.delete(X,drop_list,axis=1)