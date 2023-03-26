from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from blog.models.database import db

class Article(db.Model):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("author.id"))
    author = relationship("Author", back_populates="articles")