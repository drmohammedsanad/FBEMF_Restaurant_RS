import pandas
import numpy as np


data = pandas.read_csv("Restaurant Data with Consumer Ratings/rating_final.csv",sep=',',names="userID,UniqueU,placeID,UniqueP,rating,food_rating,service_rating".split(","))
#np.set_printoptions(threshold=np.inf, linewidth=np.inf)
data2 = pandas.read_csv("Restaurant Data with Consumer Ratings/chefmozcuisine.csv",sep=',',names="placeID,Rcuisine,UniqueCuisineIDs".split(","))
print '0000000000000000000000000000'
#print data
#print data2


#labels, uniques = pandas.factorize(data2['Rcuisine'].as_matrix())
#print labels,'888'
#labels_df = pandas.DataFrame(labels)
merged = pandas.merge(data,data2, on='placeID', how='left').fillna(0)
#merged.fillna(value='Non', method=None, axis=None, inplace=False)

merged_df = pandas.DataFrame(merged)
#print merged
print merged_df, '999'

moviemapwithID_df = pandas.DataFrame(merged_df)
moviemapwithID_df.to_csv('Restaurant Data with Consumer Ratings/Merged.csv', sep=',', header=False, float_format='%.2f', index=False,)
