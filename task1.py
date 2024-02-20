import math


def main(a):
    path_1 = 60*pow((2*pow(a, 3) - 14 * a), 7)
    path_2 = 40 * pow(a, 3) - 1 - pow(a, 2)
    path_3 = 10*pow((22 - a/12), 5)
    path_4 = 70*pow((math.sqrt(a + 67*pow(a, 2) + 1)), 4)
    return ((path_1 - path_2)/path_3) + path_4 - a

# import math


# def path_1(a):
#     return 60*pow((2*pow(a, 3) - 14 * a), 7)


# def path_2(a):
#     return 40 * pow(a, 3) - 1 - pow(a, 2)


# def path_3(a):
#     return 10*pow((22 - a/12), 5)


# def path_4(a):
#     return 70*pow((math.sqrt(a + 67*pow(a, 2) + 1)), 4)


# def main(a):
#     return ((path_1(a) - path_2(a))/path_3(a)) + path_4(a) - a
