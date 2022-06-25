from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    body: str


class ArticleCreate(ArticleBase):
    pass


class ArticleUpdate(ArticleBase):
    pass


class Article(ArticleBase):
    id: str

    class Config:
        orm_mode = True


class ArticleNotFound(BaseModel):
    detail: str
