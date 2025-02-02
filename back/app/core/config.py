import os
from dotenv import load_dotenv

load_dotenv()

class Env:
    DATABASE_URL:str=os.getenv("DATABASE_URL")
    SECRET_KEY  :str=os.getenv("SECRET_KEY")

env=Env()