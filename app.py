from fastapi import FastAPI, HTTPException
from pydantic import BaseModel # type: ignore
from pymongo import MongoClient # type: ignore
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore

app = FastAPI()

class user(BaseModel):
    username:str
    password:str
    email:str

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']
collection = db['user']
client = AsyncIOMotorClient('mongodb://localhost:27017/')
 
def confirm_password(password:str):
    if len(password)<8 and len(password)>15 :
        return 0
    return 1
def check_user(username: str):
    user1=user_collection.get(username=username)    
    if  user1:
         return 0
    return 1      
    

@app.post("/signup")
async def signup(user: dict):
    username=user.get('username')
    email=user.get('email')
    password=user.get('password')
    num=confirm_password(password)
    if num == 0:
        raise httpexceptions( statue_code =300 , detail="invalid passwords")
    check_usere= await check_user(username)
    if check_user == 0:
       raise httpexceptions(statue_code=300,detail=" username already exists")
    await users_collection.insert_one(user.dict())
    return{'message':'success'}
    
        
        
    
    

    


