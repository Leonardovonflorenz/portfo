"""
Contains various recommondation implementations
all algorithms return a list of movieids
"""

import pandas as pd
import numpy as np
from utils import lookup_movieId, match_movie_title


def recommend_random(movies, user_rating, k=3):
    """
    return k random unseen movies for user 
    """
    user = pd.DataFrame(user_rating, index=[0])
    user_t = user.T.reset_index()
    user_movie_entries = list(user_t["index"])
    movie_titles = list(movies["title"])
    intended_movies = [match_movie_title(title, movie_titles) for title in user_movie_entries]
    
    # convert these movies to intended movies and convert them into movie ids
    recommend = movies.copy()
    recommend = recommend.reset_index()
    recommend = recommend.set_index("title")
    recommend.drop(intended_movies, inplace=True)
    random_movies = np.random.choice(list(recommend.index), replace=False, size=k)
    return random_movies


def recommend_most_popular(user_rating, movies, ratings, k=5):
    """
    return k movies from list of 50 best rated movies unseen for user
    """

    # To get the most popular, you need to join the table with user ids and then check the movie that has been rated by most users!
    
    movie_ids = list(movies.sort_values("rating", ascending=False).head(k).index)

    popular_movies = [lookup_movieId(movies, movie_id) for movie_id in movie_ids]

    return popular_movies


def recommend_from_same_cluster(user_rating, movies, k=3):
    """
    Return k most similar movies to the one spicified in the movieID
    
    INPUT
    - user_rating: a dictionary of titles and ratings
    - movies: a data frame with movie titles and cluster number
    - k: number of movies to recommend

    OUTPUT
    - title: the matched movie title (with fuzzy wuzzy) of the best ranked entry
    - movie_titles 
    """

    return best_rated_title, movie_titles



def recommend_with_NMF(user_item_matrix, user_rating, model, k=5):
    """
    NMF Recommender
    INPUT
    - user_vector with shape (1, #number of movies)
    - user_item_matrix
    - trained NMF model

    OUTPUT
    - a list of movieIds
    """
    
    # initialization - impute missing values    
    
    # transform user vector into hidden feature space
    
    # inverse transformation

    # build a dataframe

    # discard seen movies and sort the prediction
    
    # return a list of movie ids
    pass

def recommend_with_user_similarity(user_item_matrix, user_rating, k=5):
    pass


def similar_movies(movieId, movie_movie_distance_matrix):
    pass
