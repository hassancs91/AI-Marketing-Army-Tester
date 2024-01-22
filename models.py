from typing import List
from pydantic import BaseModel

class SuggestionsModel(BaseModel):
    result: List[str]