from pydantic import BaseModel
from typing import Optional

class FavoriteCreate(BaseModel):
    parks: str
    description: str
    image: Optional[str] = None
    planned_visit: Optional[bool] = False
    email: Optional[str] = None


    # id = Column(Integer, primary_key=True, index=True)
    # parks = Column(String, nulllable=False)
    # description = Column(String, nullable=False)
    # image = Column(String, nullable=True)
    # planned_visit = Column(Boolean, nullable=True)
    # email = Column(String, nullable=True)

class FavoriteResponse(BaseModel):
    id: int
    parks: str
    description: str
    image: Optional[str] = None
    planned_visit: Optional[bool] = False
    email: Optional[str] = None

    class Config:
        from_attribute: True
        