"""
UTILS 
- Helper functions to use for your recommender funcions, etc
- Data: import files/models here e.g.
    - movies: list of movie titles and assigned cluster
    - ratings
    - user_item_matrix
    - item-item matrix 
- Models:
    - nmf_model: trained sklearn NMF model
"""
import pandas as pd
import numpy as np
from fuzzywuzzy import process


movies = pd.read_csv('/home/Leonardo85/portfo/data/movies_clusters_ratings.csv', index_col='movieid')  


def match_movie_title(input_title, movie_titles):
    """
    Matches inputed movie title to existing one in the list with fuzzywuzzy
    """
    matched_title = process.extractOne(input_title, movie_titles)[0]

    return matched_title

def print_movie_titles(movie_titles):
    """
    Prints list of movie titles in cli app
    """    
    for movie_id in movie_titles:
        print(f'            > {movie_id}')
    pass


def create_user_vector(user_rating, movies):
    """
    Convert dict of user_ratings to a user_vector
    """       
    # generate the user vector
    print(user_rating)
    user_vector = None
    return user_vector


def lookup_movieId(movies, movieId):
    """
    Convert output of recommendation to movie title
    """
    # match movieId to title
    movies = movies.reset_index()
    boolean = movies["movieid"] == movieId
    movie_title = list(movies[boolean]["title"])[0]
    return movie_title

    return movie_title


if __name__ == "__main__":
    user_rating = {
        "four rooms": 5,
        "sudden death": 3,
        "othello": 4,
        "nixon": 3,
        "Golden eye": 1,
        "total eclipse": 5,
        "nadja": 3
    }
    print(create_user_vector(user_rating, movies))