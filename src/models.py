import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



    
class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    coments_id = Column(Integer, ForeignKey('coments.id'))
    coments = relationship('Coments')
    
    
class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)
    coments_id = Column(Integer, ForeignKey('coments.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    coments = relationship('Coments')

class Coments(Base):
    __tablename__ = 'coments'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    content = Column(String(250), nullable=False)
    likes = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship(Post)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
