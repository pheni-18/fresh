from ..converters import ArticleConverter
from ..schemas import ArticleCreate, ArticleUpdate, Article, ArticleNotFound
from src.depends_provider import DependsProvider
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_utils.cbv import cbv
from typing import ClassVar, List

import src.application.exceptions as app_exceptions
import src.application.services as app_services


depends_provider = DependsProvider()
app_article_service = depends_provider.provide(app_services.AppArticleService)

router = APIRouter(
    # prefix='/articles',  https://github.com/dmontagu/fastapi-utils/issues/154
    tags=['articles'],
)


@cbv(router)
class ArticleController:
    _prefix: ClassVar[str] = '/articles'

    def __init__(
        self,
        app_article_service: app_services.AppArticleService = Depends(lambda: app_article_service),
        article_converter: ArticleConverter = Depends(lambda: ArticleConverter())
    ):
        self._app_article_service = app_article_service
        self._article_converter = article_converter

    @router.get(
        _prefix + '/',
        response_model=List[Article]
    )
    async def get_articles(self):
        article_dtos = self._app_article_service.get_all()
        return [self._article_converter.to_schema(article_dto) for article_dto in article_dtos]

    @router.get(
        _prefix + '/{id}',
        response_model=Article,
        responses={
            status.HTTP_404_NOT_FOUND: {'model': ArticleNotFound, 'description': 'The article was not found'},
        },
    )
    async def get_article(self, id: str):
        try:
            article_dto = self._app_article_service.get(id)
        except app_exceptions.ArticleNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')

        return self._article_converter.to_schema(article_dto)

    @router.post(
        _prefix + '/',
        status_code=status.HTTP_201_CREATED,
        response_model=Article,
    )
    async def create_article(self, article_create: ArticleCreate):
        article_create_dto = self._article_converter.to_create_dto(article_create)
        article_dto = self._app_article_service.register(article_create_dto)
        return self._article_converter.to_schema(article_dto)

    @router.patch(
        _prefix + '/{id}',
        response_model=Article,
        responses={
            status.HTTP_404_NOT_FOUND: {'model': ArticleNotFound, 'description': 'The article was not found'},
        },
    )
    async def update_article(self, id: str, article_update: ArticleUpdate):
        article_update_dto = self._article_converter.to_update_dto(id, article_update)
        try:
            article_dto = self._app_article_service.update(article_update_dto)
        except app_exceptions.ArticleNotFoundException as e:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Article not found')

        return self._article_converter.to_schema(article_dto)

    @router.delete(
        _prefix + '/{id}',
        status_code=status.HTTP_204_NO_CONTENT,
    )
    async def delete_article(self, id: str):
        self._app_article_service.delete(id)
        return
