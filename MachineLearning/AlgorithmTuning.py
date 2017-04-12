from RFESelection import *
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

estimators = np.array([10,100,200,300,400,700])

classifier = RandomForestClassifier()
param_grid = dict(n_estimators= estimators)
model = RandomForestClassifier(criterion='entropy', random_state=0,
									class_weight='balanced', n_jobs=-1)
grid = GridSearchCV(estimator=model, param_grid=param_grid)
grid.fit(X, Y)
print(grid.best_score_)
print(grid.best_estimator_.n_estimators)