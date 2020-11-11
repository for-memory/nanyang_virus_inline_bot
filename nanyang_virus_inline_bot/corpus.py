import random
from dataclasses import dataclass, field
from typing import List

from httpx import AsyncClient, NetworkError, HTTPError
from httpcore import TimeoutException

BASE_URL = "https://raw.githubusercontent.com/for-memory/nanyang_virus_inline_bot/master"


class UpdateException(Exception):
    pass


@dataclass
class Corpus:
    common: List[str] = field(default_factory=list)
    zhi: List[str] = field(default_factory=list)
    na: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.http = AsyncClient()

    async def update(self):
        try:
            self.common = (await self.http.get(f"{BASE_URL}/common.txt")).text.strip().split("\n")
            self.zhi = (await self.http.get(f"{BASE_URL}/zhi.txt")).text.strip().split("\n")
            self.na = (await self.http.get(f"{BASE_URL}/na.txt")).text.strip().split("\n")
        except (NetworkError, HTTPError, TimeoutException) as e:
            raise UpdateException from e

    def get_rnd_common(self):
        return self.common[random.randint(0, len(self.common) - 1)]

    def get_rnd_zhi(self):
        return self.zhi[random.randint(0, len(self.zhi) - 1)]
