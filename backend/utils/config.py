import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')


class Config:
    DATABASE_PATH = os.path.join(DATA_DIR, 'electricity.db')
    OCR_UPLOAD_PATH = os.path.join(BASE_DIR, 'uploads')
    MODEL_PATH = os.path.join(DATA_DIR, 'bill_model.pkl')
    TRAINING_DATA_PATH = os.path.join(DATA_DIR, 'bill_training.csv')
