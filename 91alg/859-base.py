def buddyStrings(A: str, B: str) -> bool:
    if len(A) is not len(B):
        return False
    if A is B:
        return True

    def split(str):
        return [v for v in str]
    A = split(A)
    B = split(B)
    a = b = ''
    c = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            c += 1
            if b == '':
                a = A[i]
                b = B[i]
            else:
                f1 = (A[i] == b and B[i] == a)
    # print(b)
    if (c == 2 and f1):
        return True
    else:
        return False


if __name__ == '__main__':
    sA = "ba"
    sB = "ba"
    print(buddyStrings(sA, sB))
