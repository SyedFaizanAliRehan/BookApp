from sqlalchemy import Boolean,Integer,Float,String,Column,ForeignKey
from sqlalchemy.orm import relationship
from Database.connection import BASE

class UserModel(BASE):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key = True, index = True)
    username = Column(String(100), unique = True)

class AuthorModel(BASE):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    books = relationship('BookModel', backref='author')

class BookModel(BASE):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author_id = Column(Integer, ForeignKey('author.id'))