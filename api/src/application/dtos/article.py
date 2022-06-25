from dataclasses import dataclass

import src.domain.models as domain_models


@dataclass
class ArticleBaseDTO:
    title: str
    body: str


@dataclass
class ArticleDTO(ArticleBaseDTO):
    id: str

    # TODO: type annotation of return
    @classmethod
    def from_domain(cls, article: domain_models.Article):
        return cls(
            id=article.id.value,
            title=article.title,
            body=article.body,
        )


@dataclass
class ArticleCreateDTO(ArticleBaseDTO):
    pass


@dataclass
class ArticleUpdateDTO(ArticleBaseDTO):
    id: str
