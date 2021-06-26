import pandas
import numpy as np


#data = pandas.read_csv("Restaurant Data with Consumer Ratings/rating_final.csv",sep=',',names="userID,placeID,rating,food_rating,service_rating".split(","))
#np.set_printoptions(threshold=np.inf, linewidth=np.inf)
data2 = pandas.read_csv("Restaurant Data with Consumer Ratings/chefmozcuisine.csv",sep=',',names="placeID,Rcuisine".split(","))
print '0000000000000000000000000000'
print data2


labels, uniques = pandas.factorize(data2['Rcuisine'].as_matrix())
print labels,'888'
print uniques, '222222222222222222222'
labels_df = pandas.DataFrame(labels)
n_cuisine = data2.Rcuisine.unique().shape[0]
print n_cuisine
#merged = pandas.merge(data['userID'],labels_df, left_on=None, right_on=None)
#print merged
print labels_df, '999'

moviemapwithID_df = pandas.DataFrame(labels_df)
moviemapwithID_df.to_csv('Restaurant Data with Consumer Ratings/RcuisineIDs.csv', sep='\n', header=False, float_format='%.2f', index=False,)
