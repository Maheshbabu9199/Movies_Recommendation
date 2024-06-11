import os
import sys
from src.utils.logger import logging
import pandas as pd
from src.utils.utils import save_artifacts
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class DataPreparation:
    def __init__(self, config=None):
        self.config = config
        self.req_columns = ['title', 'rating', 'audienceScore', 'tomatoMeter', 'ratingContents', 'genre', 'originalLanguage', 'director', 'writer', 'reviewText','scoreSentiment']

    def initiate_data_preparation(self):
        try:
            logging.info("Entered the data preparation method or component")
            # read the csv file
            movies_data = pd.read_csv(self.config.movies_data_path)
            reviews_data = pd.read_csv(self.config.reviews_data_path)
            logging.info("Data imported successfully")
            logging.critical(f'{movies_data.shape}, {reviews_data.shape}')

            # combining the data
            combined_data = movies_data.merge(reviews_data, left_on='id', right_on='id')
            print('combined data shape: ', combined_data.shape)
            save_artifacts(data=combined_data, name="combined")
            
            data = combined_data[self.req_columns]

            print("before: ", data.shape)
            
            data = data.dropna(axis=0, subset=['title'])        # dropping rows with missing values in 'title' column
            data.loc[:, 'rating'] = data['rating'].fillna(value='G')    # replacing missing values in 'rating' column with 'G'
            data.loc[:, 'audienceScore'] = data['audienceScore'].fillna(value=data['audienceScore'].mean())    # replacing missing values in 'audienceScore' column with mean
            data.loc[:, 'tomatoMeter'] = data['tomatoMeter'].fillna(value=data['tomatoMeter'].mean())    # replacing missing values in 'tomatoMeter' column with mean
            top_ratingContent = "['Language', 'Sexual Content', 'Strong Violent Content']"
            data.loc[:, 'ratingContents'] = data['ratingContents'].fillna(value=top_ratingContent)        # replacing missing values in 'ratingContents' column with top rated content
            data.loc[:, 'genre'] = data['genre'].fillna(value=data['genre'].mode()[0])        # replacing missing values in 'genre' column with mode
            data.loc[:, 'originalLanguage'] = data['originalLanguage'].fillna(value=data['originalLanguage'].mode()[0])    # replacing missing values in 'originalLanguage' column with mode
            data = data.dropna(axis=0, subset=['director'])        # dropping rows with missing values in 'director' column
            data = data.dropna(axis=0, subset=['writer'])        # dropping rows with missing values in 'writer' column
            data = data.dropna(axis=0, subset=['reviewText'])    # dropping rows with missing values in 'reviewText' column

            print("after: ", data.shape)


            # splitting and combining values

            def split_value(text):
                text = text.replace('[','').replace(']','')
                return text

            def combine_value(text):
                text = text.replace(' ','')
                return text

            
            # splitting value

            data['ratingContents'] = data['ratingContents'].apply(split_value)

            # combine value

            data['director'] = data['director'].apply(combine_value)
            data['writer'] = data['writer'].apply(combine_value)
            
            # lemmatizing the text
            lemmatizer = WordNetLemmatizer()
            stopwords_ = set(stopwords.words('english'))

            def lemmatize_text(text):
                words = nltk.word_tokenize(text)
                words = [lemmatizer.lemmatize(word) for word in words if word not in stopwords_]
                text = ' '.join(words)
                return text

            data['reviewText'] = data['reviewText'].apply(lemmatize_text)

        
            
            data['average_score'] = data.groupby(['title', 'director'])['audienceScore'].transform('mean')
            data['new_ratingContents'] = data.groupby(['title', 'director'])['ratingContents'].transform(lambda x: x.value_counts().index[0])
            data['new_rating'] = data.groupby(['title', 'director'])['rating'].transform(lambda x: x.value_counts().index[0])
            data['new_genre'] = data.groupby(['title', 'director'])['genre'].transform(lambda x: x.value_counts().index[0])
            data['new_tomatoMeter'] = data.groupby(['title', 'director'])['tomatoMeter'].transform(lambda x: x.value_counts().index[0])
            data['new_scoreSentiment'] = data.groupby(['title', 'director'])['scoreSentiment'].transform(lambda x: x.value_counts().index[0])
            
            for col in data.columns.tolist():
                data.loc[:, col] = data[col].astype('str')
                data.loc[:, col] = data[col].str.lower()
            
            print('after processing the data: ', data.shape)
            print('the data columns are: ', data.columns.tolist())

            data = data.drop(columns=['ratingContents', 'rating', 'genre', 'tomatoMeter', 'audienceScore','scoreSentiment'])

            data['new_reviewText'] = data.groupby(['title', 'director'])['reviewText'].transform(lambda x: ', '.join(x))

            data.drop(columns=['reviewText'], inplace=True)
            data.drop_duplicates(inplace=True)
            
            print('\nthe new data shape is: ', data.shape)

            data.rename(columns={'new_scoreSentiment':'scoreSentiment', 'average_score':'score', 'new_ratingContents':'ratingContents', 'new_rating':'rating', 'new_genre':'genre',
            'new_tomatoMeter': 'tomatoMeter', 'new_scoreSentiment':'Sentimentscore', 'new_reviewText': 'review'}, inplace=True)

            data.reset_index(inplace=True)

            print('the processed data columns are: ', data.columns.tolist())

            data = data.drop(columns=['index'])

            save_artifacts(data=data, name="final_dataset")

            
            

            return
        except Exception as e:
            raise e