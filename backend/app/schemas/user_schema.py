from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(UserBase):
    id: int
    trust_score: int

    class Config:
        from_attributes = True  # Pydantic v2 support
        orm_mode = True         # Pydantic v1 support
