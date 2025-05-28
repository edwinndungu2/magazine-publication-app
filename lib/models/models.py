from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///magazine.db")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    articles = relationship("Article", back_populates="author")
    subscriptions = relationship("Subscription", back_populates="user")
    
    def __repr__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

class Magazine(Base):
    __tablename__ = 'magazines'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    issues = relationship("Issue", back_populates="magazine")
    subscriptions = relationship("Subscription", back_populates="magazine")
    
    def __repr__(self):
        return f"<Magazine(title='{self.title}')>"

class Issue(Base):
    __tablename__ = 'issues'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    publication_date = Column(DateTime, default=datetime.utcnow)
    magazine_id = Column(Integer, ForeignKey('magazines.id'))
    
    magazine = relationship("Magazine", back_populates="issues")
    articles = relationship("Article", back_populates="issue")
    
    def __repr__(self):
        return f"<Issue(title='{self.title}', magazine='{self.magazine.title}')>"

class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    issue_id = Column(Integer, ForeignKey('issues.id'))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    author = relationship("User", back_populates="articles")
    issue = relationship("Issue", back_populates="articles")
    
    def __repr__(self):
        return f"<Article(title='{self.title}', author='{self.author.username}')>"

class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    magazine_id = Column(Integer, ForeignKey('magazines.id'))
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime)
    
    user = relationship("User", back_populates="subscriptions")
    magazine = relationship("Magazine", back_populates="subscriptions")
    
    def __repr__(self):
        return f"<Subscription(user='{self.user.username}', magazine='{self.magazine.title}')>"

def init_db():
    Base.metadata.create_all(engine)