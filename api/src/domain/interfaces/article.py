from abc import ABCMeta, abstractmethod
from typing import List

import src.domain.models as domain_models


class IArticleRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_all(self) -> List[domain_models.Article]:
        pass

    @abstractmethod
    def get(self, id: str) -> domain_models.Article:
        pass

    @abstractmethod
    def create(self, user: domain_models.Article):
        pass

    @abstractmethod
    def update(self, user: domain_models.Article):
        pass

    @abstractmethod
    def delete(self, id: str):
        pass
