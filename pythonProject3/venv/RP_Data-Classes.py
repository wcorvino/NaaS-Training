"""
python3 -m bpython
"""
# dataclass
# wrapper adds __eq__, etc
from collections import namedtuple
from dataclasses import dataclass


@dataclass
class DataClassCard:
    rank: str
    suit: str


# compare Regular Class and Named Tuple


class RegularCard:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f"{self.__class__.__name__}"
                f"(rank={self.rank!r}, suit={self.suit!r})")

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return (self.rank, self.suit) == (other.rank, other.suit)


NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])


def greeting(name: str) -> str:  # adds type & type Hint
    return 'Hello ' + name


def greetings(name):  # not type hint
    return 'Hello ' + name


if __name__ == '__main__':
    Ace_of_Spades = RegularCard("Ace", "Spades")
    print(Ace_of_Spades == RegularCard("Ace", "Spades"))

    Queen_of_Hearts = DataClassCard("Queen", "Hearts")
    print(Queen_of_Hearts == DataClassCard("Queen", "Hearts"))

    Queen_of_Diamonds = NamedTupleCard('Queen', 'Diamonds')
    print(Queen_of_Diamonds == NamedTupleCard('Queen', 'Diamonds'))

    print(greeting("_Hello"))

    print(greetings("_Hello Hello"))
