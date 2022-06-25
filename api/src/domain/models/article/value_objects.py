from dataclasses import dataclass

import uuid


@dataclass(frozen=True)
class ArticleID:
    value: str = str(uuid.uuid4())
