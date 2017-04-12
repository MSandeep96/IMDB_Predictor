from Normalisation import *

wanted_feats=[0,1,6,9,14,16]

#Drop the unimportant features
drop_list = []
j = 0
for i in range(0,X.shape[1]):
	if i == wanted_feats[j]:
		print(df.columns.values[i])
		j+=1
	else:
		drop_list.append(i)
X = np.delete(X,drop_list,axis=1)