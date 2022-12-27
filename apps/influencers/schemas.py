from pydantic import BaseModel, validator
from typing import Optional

class InfluencersSchema(BaseModel):
    username: str
    bio: Optional[str]
    followers_count: int

    class Config:
        orm_mode = True

    @validator('bio')
    def validate_bio(cls, v):
        if v and len(v) > 100:
            raise ValueError('Bio must not exceed 100 characters')
        return v