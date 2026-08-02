from dotenv import load_dotenv
import os
load_dotenv()

MONGODB_URI=os.getenv("MONGODB_URI")
SECRET_KEY=os.getenv("SECRET_KEY")
DATABASE_NAME=os.getenv("DATABASE_NAME")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))