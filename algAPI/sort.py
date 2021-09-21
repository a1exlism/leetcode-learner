from typing import List


def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]


class Solution:
    def bubble(self, arr):
        _len = len(arr)
        for i in range(0, _len-1):  # bubble n-1
            for j in range(0, _len-1-i):
                if arr[j] > arr[j+1]:
                    swap(arr, j, j+1)

        return arr

    def quick_sort(self, arr):
        def _sort(arr, l, r):
            if l >= r:
                return
            mid = partition(arr, l, r)  # part into 2 part
            _sort(arr, l, mid-1)
            _sort(arr, mid+1, r)

        def partition(arr, l, r):
            middle = arr[l]
            i = l+1
            while(i <= r):
                if arr[i] <= middle:
                    i += 1
                else:
                    swap(arr, i, r)
                    r -= 1
            mid = i-1
            swap(arr, l, mid)
            return mid

        _sort(arr, 0, len(arr)-1)
        return arr


if __name__ == "__main__":
    s = Solution()
    data = [5, 1, 1, 2, 0, 0]
    o1 = s.bubble(data)
    print(o1)

    o2 = data.copy()
    s.quick_sort(o2)
    print(o2)
