from ..schemas import Article, ArticleCreate, ArticleUpdate

import src.application.dtos as app_dtos


class ArticleConverter:
    @staticmethod
    def to_schema(article_dto: app_dtos.ArticleDTO) -> Article:
        return Article(
            id=article_dto.id,
            title=article_dto.title,
            body=article_dto.body,
        )

    @staticmethod
    def to_create_dto(article_create: ArticleCreate) -> app_dtos.ArticleCreateDTO:
        return app_dtos.ArticleCreateDTO(
            title=article_create.title,
            body=article_create.body,
        )

    @staticmethod
    def to_update_dto(id: str, article_update: ArticleUpdate) -> app_dtos.ArticleUpdateDTO:
        return app_dtos.ArticleUpdateDTO(
            id=id,
            title=article_update.title,
            body=article_update.body,
        )
