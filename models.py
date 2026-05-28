from database import Base
from sqlalchemy import Column, Integer, String, Boolean

class Favorites(Base):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True, index=True)
    parks = Column(String, nullable=False)
    description = Column(String, nullable=False)
    image = Column(String, nullable=True)
    planned_visit = Column(Boolean, nullable=True, default=False)
    email = Column(String, nullable=True)



 