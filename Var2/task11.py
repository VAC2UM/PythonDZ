class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def walk(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'B'
            return 2
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'G':
            self.state = 'G'
            return 9
        else:
            raise MealyError('walk')

    def forge(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'F':
            self.state = 'F'
            return 8
        if self.state == 'E':
            self.state = 'A'
            return 6
        else:
            raise MealyError('forge')

    def speed(self):
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 7
        else:
            raise MealyError('speed')


def test():
    o = main()
    try:
        o.forge()
    except MealyError:
        pass
    o.walk()  # 0
    o.walk()  # 2
    try:
        o.speed()
    except MealyError:
        pass
    o.forge()  # 1
    o.walk()  # 3
    try:
        o.walk()
    except MealyError:
        pass
    o.forge()  # 4
    o.speed()  # 5
    o.forge()  # 8
    o.speed()  # 7
    o.walk()  # 9

    o = main()
    o.walk()  # 0
    o.walk()  # 2
    o.forge()  # 1
    o.walk()  # 3
    o.forge()  # 4
    o.forge()  # 6


def main():
    return Mealy()
