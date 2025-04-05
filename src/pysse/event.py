from dataclasses import dataclass
from typing import Dict


@dataclass
class Event:
    name: str
    data: Dict
