from sklearn.ensemble import RandomForestClassifier
import cPickle

with open('MyClassifier.pkl','rb') as fid:
	classifier = cPickle.load(fid)
	print("Done bro")