class Point:

    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b
        self.x = x
        self.y = y
        # don't check if curve equation is satisfied when point is at infinity
        if self.x is None and self.y is None:
            return
        if self.y**2 != self.x**3 + a * x + b:
            raise ValueError("({}, {}) is not on the curve".format(x, y))
        # if two points have same x but difffernt y i.e vertical line, additive inverses
        # additive inverses: a number when added (or sign changed) to original number results in zero
        if self.x == x and self.y != y:
            return self.__class__(None, None, self.a, self.b)

    def __eq__(self, other):
        return (
            self.x == other.x
            and self.y == other.y
            and self.a == other.a
            and self.b == other.b
        )

    def __ne__(self, other):
        return (
            self.x != other.x
            and self.y != other.y
            and self.a != other.a
            and self.b != other.b
        )

    def __add__(self, other):
        if self.a != other.a or self.b != other.b:
            raise TypeError(
                "Points {}, {} are not on the same curve".format(self, other)
            )
        # point at infinity
        if self.x is None:
            return other
        # point at infinity
        if other.x is None:
            return self
