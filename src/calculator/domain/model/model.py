from dataclasses import dataclass


@dataclass
class Operands:
    left: int
    right: int

    def __hash__(self):
        return hash(self.left + self.right)

    def __eq__(self, other):
        if not isinstance(other, Operands):
            return False
        return self.left == other.left and self.right == other.right
