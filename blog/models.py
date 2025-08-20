from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = 'blogs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))

#relationship to link the blog to the user who created it
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

#relationship to link the user to the blogs they created
    blogs = relationship("Blog", back_populates="creator")