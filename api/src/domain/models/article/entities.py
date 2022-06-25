from .value_objects import ArticleID
from dataclasses import dataclass


@dataclass
class Article:
    title: str
    body: str

    id: ArticleID = ArticleID()

    def set_title(self, new_value: str):
        self.title = new_value

    def set_body(self, new_value: str):
        self.body = new_value
