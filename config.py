# .env
import os

from dotenv import load_dotenv, find_dotenv

#get path where this file is
BASEDIR = os.path.abspath(os.path.dirname(__file__))
#file path with your '.env' file name
#load_dotenv(os.path.join(BASEDIR, '.env'))

#will search for .env file in local folder and load variables
load_dotenv(find_dotenv())

#load in the API keys 
COHERE_API_KEY = os.getenv('COHERE_API_KEY')
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
