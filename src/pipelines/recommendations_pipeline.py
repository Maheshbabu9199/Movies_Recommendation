import os
import sys
from src.utils.logger import logging
from src.components.recommendations import Recommendations
from src.config.Configurations import Configuration


class RecommendationsPipeline:
    def __init__(self):
        pass
    def make_recommendations(self, movie_title=None):
        try:
            print('started..')
            logging.info("Recommendations Pipeline Started")
            config = Configuration()
            config = config.get_recommendations_config()
            recommendations = Recommendations(config=config)
            ground_truth, recommendations = recommendations.initiate_recommendations(movie_title)
            logging.info("Recommendations Pipeline Completed")
            # print('recommendations: ', recommendations)
            # print('ground truth: ', ground_truth)
            return recommendations, ground_truth
        except Exception as e:
            logging.error(e)

if __name__ == "__main__":
    pipeline = RecommendationsPipeline()
    recommendations, ground_truth = pipeline.make_recommendations(movie_title='angry rice wives')

    print('recommendations: ', recommendations)
    print('ground truth: ', ground_truth)