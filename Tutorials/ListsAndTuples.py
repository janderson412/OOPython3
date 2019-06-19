
def test1():
    print('test 1')
    a = [0, 1, 2, 3, 4, 5]
    b = a[::-1]
    print(a, b)

    c = [100, 101, 102, 103, 104, 105]
    x = a + c
    y = b + c
    print(a, b, c, x, y)


if __name__ == "__main__":
    test1()