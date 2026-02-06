from pydantic import BaseModel, EmailStr, Field, ConfigDict, validator
from datetime import datetime
from typing import Optional

# New user creation schema
class UserCreate(BaseModel):
    email: EmailStr  
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=8, max_length=72)


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
    

#schema for Password change
class ChangePassword(BaseModel):
    old_password: str = Field(..., min_length=3)
    new_password: str = Field(..., min_length=8, max_length=72)
    confirm_password: str = Field(..., min_length=8, max_length=72)

  
    
    @validator('new_password')
    def password_strength(cls, v):
        
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters long')
        
        # Check for at least one number
        if not any(char.isdigit() for char in v):
            raise ValueError('Password must contain at least one number')
        
        # Check for at least one letter
        if not any(char.isalpha() for char in v):
            raise ValueError('Password must contain at least one letter')
        
        return v
    
    @validator('confirm_password')
    def passwords_match(cls, v, values):
        
        if 'new_password' in values and v != values['new_password']:
            raise ValueError('Passwords do not match')
        return v


class TokenData(BaseModel):
    user_id: Optional[int] = None
    username: Optional[str] = None