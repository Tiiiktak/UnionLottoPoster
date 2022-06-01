from typing import List
from pydantic import BaseModel


class WinningInfoDto(BaseModel):
    date: str
    stage: str
    lotto_name: str
    code: List[int]
