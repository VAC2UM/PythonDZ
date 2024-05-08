class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def stare(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'E':
            self.state = 'B'
            return 8
        else:
            raise MealyError('stare')

    def erase(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'A'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 7
        else:
            raise MealyError('erase')

    def add(self):
        if self.state == 'A':
            self.state = 'D'
            return 1
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'C':
            self.state = 'E'
        else:
            raise MealyError('add')


def test():
    o = main()
    try:
        o.erase()  # MealyError
    except MealyError:
        pass
    o.stare()  # 0
    try:
        o.add()  # MealyError
    except MealyError:
        pass
    o.erase()  # 2
    o.add()  # 5
    try:
        o.stare()  # MealyError
    except MealyError:
        pass
    o.erase()  # 7

    o = main()
    o.add()  # 1

    o = main()
    o.stare()  # 0
    o.erase()  # 2
    o.stare()  # 3
    o.add()  # 6
    o.stare()  # 8

    o = main()
    o.stare()  # 0
    o.erase()  # 2
    o.erase()  # 4


def main():
    return Mealy()
