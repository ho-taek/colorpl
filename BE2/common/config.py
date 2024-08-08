from dotenv import load_dotenv
from urllib.parse import quote_plus
import os

load_dotenv()

class Settings:
    DATABASE_USER: str = os.getenv('DATABASE_USER')
    DATABASE_PASSWORD: str = quote_plus(os.getenv('DATABASE_PASSWORD'))
    DATABASE_HOST: str = os.getenv('DATABASE_HOST')
    DATABASE_NAME: str = os.getenv('DATABASE_NAME')
    DATABASE_NAME2: str = os.getenv('DATABASE_NAME2')
    SUPERADMIN_USERNAME: str = os.getenv('SUPERADMIN_USERNAME')
    SUPERADMIN_EMAIL: str = os.getenv('SUPERADMIN_EMAIL')
    SUPERADMIN_PASSWORD: str = os.getenv('SUPERADMIN_PASSWORD')

settings = Settings()

class EC2:
    EC2_DB_ID: str = os.getenv('EC2_DB_ID')
    EC2_DB_PW: str = quote_plus(os.getenv('EC2_DB_PW'))
    EC2_DB_HOST: str = os.getenv('EC2_DB_HOST')
    EC2_DB_PORT: str = os.getenv('EC2_DB_PORT')
    EC2_DB_NAME: str = os.getenv('EC2_DB_NAME')

ec2 = EC2()