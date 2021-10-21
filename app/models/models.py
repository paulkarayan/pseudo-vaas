from enum import Enum

from pydantic import BaseModel
from pydantic.schema import Optional


class Extractor(str, Enum):
    MONKEY_LEARN = 'monkey_learn'
    SHUTTERSTOCK = 'shutterstock'


class TextSearch(BaseModel):
    text: str
    extractor: Optional[Extractor]

    class Config:
        use_enum_values = True
