import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import psycopg2

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
database=os.getenv('database')
port=str(os.getenv("port"))


def read_postgresql_data():
    logging.info("Reading PostgreSQL database started")
    try:
        mydb=psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            port=port
        )
        logging.info("Connection established %s",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df
    

    except Exception as ex:
        raise CustomException(ex)