import pandas
import numpy as np


data = pandas.read_csv("Restaurant Data with Consumer Ratings/rating_final.csv",sep=',',names="userID,placeID,rating,food_rating,service_rating".split(","))
np.set_printoptions(threshold=np.inf, linewidth=np.inf)

print '0000000000000000000000000000'
print data['userID']


labels, uniques = pandas.factorize(data['userID'].as_matrix())
print labels,'888'
labels_df = pandas.DataFrame(labels)
#merged = pandas.merge(data['userID'],labels_df, left_on=None, right_on=None)
#print merged
print labels_df, '999'

moviemapwithID_df = pandas.DataFrame(labels_df)
moviemapwithID_df.to_csv('Restaurant Data with Consumer Ratings/userIDs.csv', sep='\n', header=False, float_format='%.2f', index=False,)
