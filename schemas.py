from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    
class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    
class userRespones(BaseModel):
    id: int
    name: str
    email: str
    
    class Config:
        from_attribute = True