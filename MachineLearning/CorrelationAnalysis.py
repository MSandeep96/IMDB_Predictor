from Preprocessing import *
from pandas.tools.plotting import scatter_matrix
from sklearn.preprocessing import (Imputer, LabelEncoder)
import matplotlib.pyplot as plt
import seaborn as sns

#append result array to the features array
comp_data = np.append(X,Y_OrgI[:,None],1)

ds = pd.DataFrame(data=comp_data,columns=df.columns.values)

#computes the correlation matrix
corr = ds.corr()

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(ds.shape[1],ds.shape[1]))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3,
            square=True,
            linewidths=.5, cbar_kws={"shrink": .5}, ax=ax)

plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.show()