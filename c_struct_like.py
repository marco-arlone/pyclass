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

# Record examples
r1 = Record(1, 'Roj', 'via Vercellone, 11', 'Biella')
r2 = Record(2, 'Roj', 'via S. Agata, 9', 'Biella')

# Print full records
print(r1)
print(r2)

# Print a single component
print(r1.id)
print(r2.id)
