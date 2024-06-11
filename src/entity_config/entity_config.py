import os 
import sys
from src.utils.logger import logging
from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    movies_dataset_path: Path
    reviews_dataset_path: Path

@dataclass
class DataPreparationConfig:
    movies_data_path: Path
    reviews_data_path: Path

@dataclass
class DataTransformationConfig:
    final_dataset_path: Path

@dataclass
class RecommendationsConfig:
    top_K: int
    similarity_path: Path
    movies_content_path: Path