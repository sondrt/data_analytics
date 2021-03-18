#This code utilizes data from https://grouplens.org/datasets/movielens/

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation','zip']
users = pd.read_table('./../ml-1m/users.dat', sep = '::', names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../ml-1m/ratings.dat', sep = '::', names = rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../ml-1m/movies.dat', sep ='::', names = mnames)

#merge
data = pd.merge(pd.merge(users,ratings, on = 'user_id'), movies,on ='movie_id')#, right_on='user_id')


mean_ratings = data.pivot_table('rating',index ='title',columns= 'gender', aggfunc='mean')

ratings_by_title = data.groupby('title').size()
# print(ratings_by_title[:10])

active_titles = ratings_by_title.index[ratings_by_title >= 250]

mean_ratings = mean_ratings.loc[active_titles]
# print(mean_ratings.keys())

#sort by:
top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
# print(top_female_ratings[:100])

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_values(by='diff', ascending=False)
# print(sorted_by_diff[:15]) 

#reverse order of rows, take first 15 rows
# print(sorted_by_diff[::-1][:15])

# Stdev of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()

#Filter down to active_titles
rating_std_by_title = rating_std_by_title.loc[active_titles]

#order series by value in descending order
print(rating_std_by_title.sort_values(ascending=False)[:10])











