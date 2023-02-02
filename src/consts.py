from dotenv import load_dotenv
import os

load_dotenv()
'''
env variables loaded from .env file
'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))[:-3]
DATA_DIR = os.path.join(BASE_DIR, 'data')
API_KEY = os.getenv("API_KEY")
