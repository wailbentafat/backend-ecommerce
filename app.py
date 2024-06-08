

from fastapi import FastAPI 
from pydantic import BaseModel
import pymongo

app = FastAPI()
class user(BaseModel):
    username:str
    password:str
    email:str

client=pymongo.MongoClient("")
@app.post("/signup")
async def signup(user: dict):
    username=user.get('username')
    password=user.get('password')
    email=user.get('email')
    return {"username":username,"password":password,"email":email}
    


