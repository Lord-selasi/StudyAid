from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

# New user creation schema
class UserCreate(BaseModel):
    email: EmailStr  
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=100)


# Login schema
class UserLogin(BaseModel):
    email_or_username: str
    password: str

# Schema for returning user data 
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    is_premium: bool
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

# Schema for updating user
class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=50)

# Schema for token response
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None