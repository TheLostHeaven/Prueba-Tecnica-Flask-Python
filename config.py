from decouple import config
from dotenv import load_dotenv
import os 

load_dotenv()

class Config():
    SECRET_KEY = config('SECRET_KEY')

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
database = os.environ["MYSQL_DATABASE"]
jwtKey = os.environ["JTW_KEY"]

username=os.getenv("ADMIN_USERNAME"),
fullname=os.getenv("ADMIN_FULLNAME"),
email=os.getenv("ADMIN_EMAIL"),
password_admin=os.getenv("ADMIN_PASSWORD"),
role_id=os.getenv("ADMIN_ROLE_ID")

user_test = os.environ["MYSQL_USER_TEST"]
password_test = os.environ["MYSQL_PASSWORD_TEST"]
host_test = os.environ["MYSQL_HOST_TEST"]
database_test = os.environ["MYSQL_DATABASE_TEST"]

DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{database}'

DATABASE_CONNECTION_URI_TEST = f'mysql://{user_test}:{password_test}@{host_test}/{database_test}'
