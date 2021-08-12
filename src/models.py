import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Follower (Base):
    __tablename__ = "Follower"
    id = Column(Integer, primary_key = True)
    User_id = Column(Integer, ForeignKey("User.id"))

class User (Base):
    __tablename__= "User"
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250) ,nullable=False)
    email = Column(String(250), nullable=False)
    Follower = relationship("Follower")

class Comment (Base):
    __tablename__ = "Comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    User_id = Column(Integer, ForeignKey("User.id"))
    Post_id = Column(Integer, ForeignKey("Post.id"))

class Post (Base):
    __tablename__ = "Post"
    id = Column (Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey("User.id"))

class Media (Base):
    __tablename__ = "Media"
    id = Column (Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    Post_id = Column(Integer, ForeignKey("Post.id"))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e