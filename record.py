from dataclasses import dataclass
from typing import NamedTuple

@dataclass
class Point:

    x: float = 0.0
    y: float = 0.0

p = Point(1.2, 3.4)

print(p)
