from enum import Enum

from pydantic import BaseModel

#
# class DetailedLayout(BaseModel):
#     num: int
#     name: str


class AnswerType(Enum):
    layout = "layout"
    detailed = "detailed"
