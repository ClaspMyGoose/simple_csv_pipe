import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

# dir setup 
cwd = os.getcwd()
dataDir = 'csvdata'
dataF = 'data.csv'
path = os.path.join(cwd,dataDir,dataF)


# env variables
user = os.environ.get('user')
pwd = os.environ.get('pwd')
host = os.environ.get('host')
port = os.environ.get('port')
db = os.environ.get('db')


# engine setup 
engine = create_engine(f'postgresql://{user}:{pwd}@{host}:{port}/{db}')


# creating table using headers 
date_columns = ['tpep_pickup_datetime','tpep_dropoff_datetime']
headerSample = pd.read_csv(path, nrows=5, parse_dates=date_columns)
header = headerSample.head(0)

header.to_sql('yellow_taxi', con=engine, if_exists='replace')


# loading rest of the csv data 
for chunk in pd.read_csv(path, chunksize=100000, parse_dates=date_columns):
  chunk.to_sql('yellow_taxi', con=engine, if_exists='append')
  print('wrote chunk...')





