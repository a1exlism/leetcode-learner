import collections
from typing import List


class Solution:
    """
    TIPS: Each k for which some permutation of arr[:k] is equal to sorted(arr)[:k] is where we should cut each chunk.
    """

    def maxChunksToSorted1(self, arr: List[int]) -> int:
        count = 0
        sa = sorted(arr)
        sum_1 = sum_2 = 0
        for i, v in enumerate(arr):
            sum_1 += v
            sum_2 += sa[i]
            if sum_1 == sum_2:
                count += 1
        return count

    def maxChunksToSorted(self, arr):
        aux = []  # stack for chunk maximum
        for v in arr:
            if not aux or aux[-1] <= v:
                aux.append(v)
            else:
                # Re-arrange; keep monotonic
                closest_max = aux.pop()
                while(aux and aux[-1] > v):
                    aux.pop()
                aux.append(closest_max)
        return len(aux)


if __name__ == '__main__':
    s = Solution()
    l = [
        [4, 2, 2, 1, 1],  # 1
        [2, 1, 3, 4, 4],  # 4
        [0, 0, 1, 1, 1],  # 5
        [1, 1, 0, 0, 1]   # 2
    ]
    for nl in l:
        print(s.maxChunksToSorted(nl))
