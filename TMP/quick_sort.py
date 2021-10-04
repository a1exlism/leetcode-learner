from typing import List


def swap(arr: List[int], a, b):
    arr[a], arr[b] = arr[b], arr[a]


def qs(arr: List[int], l, r):
    if l >= r:
        return
    mid = partition(arr, l, r)
    qs(arr, l, mid-1)
    qs(arr, mid+1, r)
    return arr


def partition(arr: List[int], l, r):
    middle = arr[l]
    i = l+1
    while i <= r:
        if arr[i] <= middle:
            i += 1
        else:
            swap(arr, i, r)
            r -= 1
    mid = i-1
    swap(arr, l, mid)
    return mid


if __name__ == "__main__":
    data = [8, 5, 2, 3]
    output = qs(data, 0, len(data)-1)
    print(output)
