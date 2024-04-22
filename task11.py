class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def link(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'H'
            return 11
        else:
            raise MealyError('link')

    def snap(self):
        if self.state == 'B':
            self.state = 'B'
            return 3
        if self.state == 'C':
            self.state = 'D'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'F'
            return 10
        if self.state == 'A':
            self.state = 'H'
            return 1
        else:
            raise MealyError('snap')

    def spawn(self):
        if self.state == 'B':
            self.state = 'C'
            return 2
        if self.state == 'C':
            self.state = 'G'
            return 5
        if self.state == 'D':
            self.state = 'E'
            return 6
        if self.state == 'F':
            self.state = 'B'
            return 9
        else:
            raise MealyError('spawn')


def test():
    o = main()
    try:
        o.spawn()  # MealyError
    except MealyError:
        pass
    o.link()  # 0
    try:
        o.link()  # MealyError
    except MealyError:
        pass
    o.snap()  # 3
    o.spawn()  # 2
    o.snap()  # 4
    o.spawn()  # 6
    o.snap()  # 7
    o.snap()  # 10
    o.spawn()  # 9
    try:
        o.link()  # MealyError
    except MealyError:
        pass
    o.spawn()  # 2
    o.spawn()  # 5
    o.link()  # 11

    o = main()
    o.link()  # 0
    o.spawn()  # 2
    o.snap()  # 4
    o.spawn()  # 6
    try:
        o.link()  # MealyError
    except MealyError:
        pass
    o.snap()  # 7
    o.snap()  # 10
    o.snap()  # 10
    o.spawn()  # 9
    o.snap()  # 3
    o.spawn()  # 2
    o.spawn()  # 5
    o.link()  # 11


def main():
    return Mealy()


test()
