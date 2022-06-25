from dataclasses import dataclass
from typing import Optional
from uuid import uuid4


@dataclass
class Article:
    id: str
    title: str
    body: str

    def __init__(self, title: str, body: str, id: Optional[str]=None):
        self.title = title
        self.body = body

        if id is None:
            self.id = str(uuid4())
        else:
            self.id = id


    def set_title(self, new_value: str):
        self.title = new_value

    def set_body(self, new_value: str):
        self.body = new_value
