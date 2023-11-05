from dataclasses import dataclass
from typing import NamedTuple

# -----------------------------------------------------------------------------
#   Point
# -----------------------------------------------------------------------------
@dataclass
class Point:

    x: float = 0.0
    y: float = 0.0

    def __add__(self, o):
        return Point(self.x + o.x, self.y + o.y)

# -----------------------------------------------------------------------------
#   Record
# -----------------------------------------------------------------------------
class Record(NamedTuple):

    id: int
    company: str
    address: str
    city: str

# -----------------------------------------------------------------------------

# Point example
p1 = Point(1.2, 3.4)
print(p1)
print(p1.x)
print(p1.y)
p2 = Point(.1, .1)
print(p1 + p2)

# Record example
r = Record(12345678, 'Roj', 'via Vercellone, 11', 'Biella')
print(r)
print(r.id)
