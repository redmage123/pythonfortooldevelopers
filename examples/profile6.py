#!/usr/bin/python3


import cProfile

def odd_squares1(n):

    squares_list = []
    for i in range(n):
        if i %2 != 0:
            squares_list.append(i ** 2)
    return squares_list

def odd_squares2(n):

    return [i**2 for i in range(n) if i % 2 != 0]


def main():
    foo = odd_squares2(100000)


if __name__ == "__main__":
    cProfile.run('main()')

