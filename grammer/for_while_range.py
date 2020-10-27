def for_study():
    for x in (1, 2, 3):
        print(x, end=",")
    print()
    for x in "hello":
        print(x, end=",")
    print()


def range_study():
    print(type(range(0, 3)))
    # 0 3 6 9
    for i in range(0, 10, 3):
        print(i, end=" ")
    print()


def while_study():
    n = 1
    while n < 5:
        n += 1
        print(n)


if __name__ == '__main__':
    for_study()
    range_study()
    while_study()
