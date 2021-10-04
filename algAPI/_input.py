def fn():
    data = list(map(int, input().split()))
    print(data)


def fn2():
    while True:
        try:
            line = input()
            if not line:
                break
            data = list(map(int, line.split(' ')))
            print(data)
        except:
            break


if __name__ == "__main__":
    # fn()
    fn2()
