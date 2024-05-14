# # Самое популярное решение
# # --------------------------------------
# class MealyError(Exception):
#     def __init__(self, message):
#         super().__init__(message)
#
#
# class Mealy:
#     def __init__(self):
#         self.state = 'A'
#
#     def link(self):
#         if self.state == 'A':
#             self.state = 'B'
#             return 0
#         if self.state == 'F':
#             self.state = 'G'
#             return 8
#         if self.state == 'G':
#             self.state = 'H'
#             return 11
#         else:
#             raise MealyError('link')
#
#     def snap(self):
#         if self.state == 'B':
#             self.state = 'B'
#             return 3
#         if self.state == 'C':
#             self.state = 'D'
#             return 4
#         if self.state == 'E':
#             self.state = 'F'
#             return 7
#         if self.state == 'F':
#             self.state = 'F'
#             return 10
#         if self.state == 'A':
#             self.state = 'H'
#             return 1
#         else:
#             raise MealyError('snap')
#
#     def spawn(self):
#         if self.state == 'B':
#             self.state = 'C'
#             return 2
#         if self.state == 'C':
#             self.state = 'G'
#             return 5
#         if self.state == 'D':
#             self.state = 'E'
#             return 6
#         if self.state == 'F':
#             self.state = 'B'
#             return 9
#         else:
#             raise MealyError('spawn')
#
#
# def test():
#     o = main()
#     try:
#         o.spawn()  # MealyError
#     except MealyError:
#         pass
#     o.link()  # 0
#     o.snap()  # 3
#     o.spawn()  # 2
#     try:
#         o.link()  # MealyError
#     except MealyError:
#         pass
#     o.snap()  # 4
#     o.spawn()  # 6
#     o.snap()  # 7
#     o.snap()  # 10
#     o.link()  # 8
#     o.link()  # 11
#     try:
#         o.snap()  # MealyError
#     except MealyError:
#         pass
#
#     o = main()
#     o.snap()  # 1
#
#     o = main()
#     o.link()  # 0
#     o.snap()  # 3
#     o.spawn()  # 2
#     o.spawn()  # 5
#
#     o = main()
#     o.link()  # 0
#     o.snap()  # 3
#     o.spawn()  # 2
#     o.snap()  # 4
#     o.spawn()  # 6
#     o.snap()  # 7
#     o.spawn()  # 9
#
#
# def main():
#     return Mealy()
#
#
# test()
# # --------------------------------------

class MealyError(Exception):
    def __init__(self, method_name):
        self.method_name = method_name


class StateMachine:
    def __init__(self):
        self.state = 'A'

    state_transitions = {
        'A': {'link': ('B', 0), 'snap': ('H', 1)},
        'B': {'spawn': ('C', 2), 'snap': ('B', 3)},
        'C': {'snap': ('D', 4), 'spawn': ('G', 5)},
        'D': {'spawn': ('E', 6)},
        'E': {'snap': ('F', 7)},
        'F': {'link': ('G', 8), 'spawn': ('B', 9), 'snap': ('F', 10)},
        'G': {'link': ('H', 11)}
    }

    def transition(self, action):
        if self.state == 'H':
            return 'H', None
        if action not in self.state_transitions[self.state]:
            raise MealyError(action)
        new_state, return_value = self.state_transitions[self.state][action]
        self.state = new_state
        return return_value

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


def main():
    return StateMachine()


def test():
    test_exceptions = [
        ('A', 'spawn'),
        ('B', 'link'),
        ('C', 'link'),
        ('D', 'snap'),
        ('D', 'link'),
        ('E', 'spawn'),
        ('E', 'link'),
        ('G', 'spawn'),
        ('G', 'snap'),
        ('H', 'snap'),
        ('H', 'spawn'),
        ('H', 'link')
    ]
    test_result = [
        ('A', 'link', 0, 'B'),
        ('A', 'snap', 1, 'H'),
        ('B', 'spawn', 2, 'C'),
        ('B', 'snap', 3, 'B'),
        ('C', 'snap', 4, 'D'),
        ('C', 'spawn', 5, 'G'),
        ('D', 'spawn', 6, 'E'),
        ('E', 'snap', 7, 'F'),
        ('F', 'link', 8, 'G'),
        ('F', 'spawn', 9, 'B'),
        ('F', 'snap', 10, 'F'),
        ('G', 'link', 11, 'H'),
    ]
    sm = main()
    for start_state, action in test_exceptions:
        sm.state = start_state
        try:
            sm.transition(action)
        except MealyError:
            pass
    for start_state, action, expected_return, expected_state in test_result:
        sm.state = start_state
        assert sm.transition(action) == expected_return
        assert sm.state == expected_state
