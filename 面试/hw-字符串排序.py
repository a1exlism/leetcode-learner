"""
字符串排序 从小到大 同一个字母大小写按原有顺序 非字母位置不变
假设全部小写字母
"""


def ssort(s: str):
    arr = list(s)
    ca, cz = ord('a'), ord('z')
    inds = []
    chs = []
    for i, x in enumerate(s):
        if ca <= ord(x) and ord(x) <= cz:
            inds.append(i)
            chs.append(x)
    chs.sort(reverse=True)
    for i in inds:
        arr[i] = chs.pop()
    return ''.join(arr)


if __name__ == "__main__":
    data = 'jkdfjgpi23u480jgdjho/s,jfpiou`-923rjkfd'
    output = ssort(data)
    print(output)
