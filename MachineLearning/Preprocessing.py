from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
from sklearn.preprocessing import (Imputer, LabelEncoder)

import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)



# CONVERTS RATING TO INT
def reduceRatings(rating):
	return str(int(float(rating)))


#data from the csv file
dataset = pd.read_csv('Data.csv')

# Removing some columns which aren't useful for our calculation
df = dataset.drop([col for col in ['movie_title', 'color', 'plot_keywords', 'movie_imdb_link',
								   'aspect_ratio', 'genres','actor_2_name','actor_3_name','actor_1_name',
								   'director_name']
				   if col in dataset], axis=1)

#get the positions of the columns which are categorical values
language_pos = df.columns.get_loc("language")
country_pos = df.columns.get_loc("country")
content_rating_pos = df.columns.get_loc("content_rating")


#create a exclude list of these excluded attributes
categorical_fts = []
categorical_fts.append(language_pos)
categorical_fts.append(country_pos)
categorical_fts.append(content_rating_pos)

# ALL FEATURES :Array of features, exludes the last column
X = df.iloc[:, :-1].values

# ORIGINAL RATING :Last column array, string of length 6 (dtype)
Y_Org = np.asarray(df.iloc[:, df.shape[1]-1], dtype="|S6")
Y_OrgI = Y_Org.astype(np.float)
# REDUCE RATINGS TO DOMAINS
dicer = np.vectorize(reduceRatings)
Ystr = dicer(Y_Org)

# Y FLOAT REPRESENTATION :Convert it to float
Y = Ystr.astype(np.int)

label_language = LabelEncoder()
X[0:, language_pos] = label_language.fit_transform(X[0:, language_pos])
label_country = LabelEncoder()
X[0:, country_pos] = label_country.fit_transform(X[0:, country_pos])
label_content_rating = LabelEncoder()
X[0:, content_rating_pos] = label_content_rating.fit_transform(X[0:, content_rating_pos])

imp = Imputer(missing_values='NaN', strategy='mean', axis=0)
X = imp.fit_transform(X)			   

"""
X has all features.
Y_str has all IMDB scores in string format.
Y_Org has all original IMDB scores.
Y has all IMDB scores in int format.
"""