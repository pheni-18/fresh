from ..dtos.article import ArticleDTO, ArticleCreateDTO, ArticleUpdateDTO
from typing import List

import src.domain.interfaces as domain_interfaces
import src.domain.models as domain_models
import pinject


class AppArticleService:
    _article_repo: domain_interfaces.IArticleRepository

    @pinject.inject()
    def __init__(self, article_repo: domain_interfaces.IArticleRepository):
        self._article_repo = article_repo

    def get_all(self) -> List[ArticleDTO]:
        articles = self._article_repo.get_all()
        return [ArticleDTO.from_domain(article) for article in articles]

    def get(self, id: str) -> ArticleDTO:
        id_ = domain_models.ArticleID(value=id)
        article = self._article_repo.get(id_)
        return ArticleDTO.from_domain(article)

    def register(self, article_create_dto: ArticleCreateDTO) -> ArticleDTO:
        article = domain_models.Article(
            title=article_create_dto.title,
            body=article_create_dto.body,
        )
        self._article_repo.create(article)
        return ArticleDTO.from_domain(article)

    def update(self, article_update_dto: ArticleUpdateDTO) -> ArticleDTO:
        id = domain_models.ArticleID(value=article_update_dto.id)
        article = self._article_repo.get(id)
        if not article_update_dto.title == article.title:
            article.set_title(article_update_dto.title)

        if not article_update_dto.body == article.body:
            article.set_body(article_update_dto.body)

        self._article_repo.update(article)
        return ArticleDTO.from_domain(article)

    def delete(self, id: str):
        id_ = domain_models.ArticleID(value=id)
        self._article_repo.delete(id_)
