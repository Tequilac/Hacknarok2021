from enum import Enum, auto


class PopState(Enum):
    healthy = auto()
    ill = auto()
    recovered = auto()
    dead = auto()
    vaccinated = auto()
