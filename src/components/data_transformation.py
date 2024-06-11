import os
import sys
from src.utils.logger import logging
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from src.utils.utils import save_artifacts
import pickle

class DataTransformation:
    def __init__(self, config= None):
        self.config = config

    def initiate_data_transformation(self):
        try:
            logging.info('data transformation initiated')
            data = pd.read_csv(self.config.final_dataset_path)

            print(data.info())
            data.loc[:, 'score'] = data['score'].astype('str')
            data.loc[:, 'tomatoMeter'] = data['tomatoMeter'].astype('str')
            
            data['content'] = data['title'] + ' ' + data['originalLanguage'] + ' ' + data['director'] + ' ' + data['writer'] + ' ' + data['score'] + ' ' + data['ratingContents'] + ' ' + data['rating'] + ' ' + data['genre'] + ' ' + data['tomatoMeter'] + ' ' + data['Sentimentscore'] 

            final_data = data[['content', 'title', 'genre']]
            
            print('the shape is :, ',final_data.shape)

            final_data = final_data.iloc[:2000]
            save_artifacts(data=final_data, name="final_data")
            vectorizer = CountVectorizer(max_features=100)

            features = vectorizer.fit_transform(final_data['content'])
            features.toarray()

            print("features shape is :, ",features.shape)

            similarity = cosine_similarity(features)
            
            print('similarity shape is :, ',similarity.shape)

            #pickle.dump(similarity, open('similarity.pkl', 'wb'))
            return 

        except Exception as e:
            raise e