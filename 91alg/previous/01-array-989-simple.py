from typing import List

if __name__ == '__main__':
    a = [1, 2, 0, 0]
    k = 34999
    # def addToArrayForm(self, A: List[int], K: int) -> List[int]:

    def addToArrayForm(A: List[int], K: int):
        for i in range(len(A)-1, -1, -1):
            K += A[i]
            A[i] = K % 10
            K //= 10
        while(K > 0):
            A.insert(0, K % 10)
            K //= 10
        return A

    print(addToArrayForm(a, k))
