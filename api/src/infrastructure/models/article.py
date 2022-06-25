from ..database import Base
from sqlalchemy import Column, String


class Article(Base):
    __tablename__ = "article"

    id = Column(String, primary_key=True)
    title = Column(String)
    body = Column(String)
