from ..db_session import SessionGenerator
from ..models import Article
from typing import List

import src.application.exceptions as app_exceptions
import src.domain.interfaces as domain_interfaces
import src.domain.models as domain_models
import pinject


class ArticleRepository(domain_interfaces.IArticleRepository):
    _session_generator: SessionGenerator

    @pinject.inject()
    def __init__(self, session_generator: SessionGenerator):
        self._session_generator = session_generator

    def get_all(self) -> List[domain_models.Article]:
        with self._session_generator.generate() as session:
            db_articles = session.query(Article).all()
            return [
                domain_models.Article(
                    id=db_article.id,
                    title=db_article.title,
                    body=db_article.body,
                )
                for db_article in db_articles
            ]

    def get(self, id: str) -> domain_models.Article:
        with self._session_generator.generate() as session:
            db_article = session.query(Article).filter(Article.id == id.value).first()
            if db_article is None:
                raise app_exceptions.ArticleNotFoundException()

            return domain_models.Article(
                id=db_article.id,
                title=db_article.title,
                body=db_article.body,
            )

    def create(self, article: domain_models.Article):
        with self._session_generator.generate() as session:
            db_article = Article(
                id=article.id,
                title=article.title,
                body=article.body,
            )
            session.add(db_article)
            session.commit()

    def update(self, article: domain_models.Article):
        with self._session_generator.generate() as session:
            db_article = session.query(Article).filter(Article.id == article.id).first()
            if db_article is None:
                raise app_exceptions.ArticleNotFoundException()
            db_article.title = article.title
            db_article.body = article.body
            session.commit()

    def delete(self, id: str):
        with self._session_generator.generate() as session:
            db_article = session.query(Article).filter(Article.id == id.value)
            db_article.delete()
            session.commit()
