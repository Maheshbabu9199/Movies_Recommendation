import os
import sys
from src.utils.logger import logging
import pickle 
import pandas as pd


class Recommendations:
    def __init__(self, config):
        self.config = config
        print('inside recommendations constructor') 

    def initiate_recommendations(self, movie_title):
        try:
            logging.info("Initiating recommendations")
            print('inside initiate recommendations')
            with open(self.config.similarity_path, 'rb') as f:
                similarity = pickle.load(f)

            print('similarity loaded: ', type(similarity))

            movies_info = pd.read_csv(self.config.movies_content_path)
            print('movies_info loaded: ', type(movies_info), movies_info.shape)

            def recommend(movie,K):
                index = movies_info[movies_info['title'] == movie].index[0]
                distances = sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
                result = []
                for i in distances[1:self.config.top_K+1]:
                    result.append(movies_info.iloc[i[0]].title)
                return result

    
            def recommend_by_genre(movie_title):
                """
                Recommends movies with the same genre as a given movie title.

                Args:
                    movie_title: The title of the movie for which to recommend similar genres.
                    df: The DataFrame containing movie data (title, genre, ratings).

                Returns:
                    A list of movies with the same genre as the input movie.
                """
                try:

                    # Find the movie in the DataFrame
                    movie = movies_info[movies_info['title'] == movie_title]

                    # Get the director of the movie (assuming there's only one genre per movie)
                    genre = movie['genre'].values[0]
                    print('genre is: ', genre)

                    # Filter movies with the same genre
                    similar_movies = movies_info[movies_info['genre'] == genre]

                    # Exclude the original movie from recommendations
                    similar_movies = similar_movies[similar_movies['title'] != movie_title]
                    
                    # Return a list of movie titles
                    return similar_movies['title'].tolist()

                except IndexError:
                    print(f"Movie '{movie_title}' not found.")
                    return []
            return recommend_by_genre(movie_title), recommend(movie_title, self.config.top_K)
        except Exception as e:
            print(e)
            raise e