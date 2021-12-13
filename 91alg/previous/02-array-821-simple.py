from typing import List
if __name__ == '__main__':
    S = "loveleetcode"
    C = 'e'
    # 输出：[3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

    # def shortestToChar(self, S: str, C: str) -> List[int]:

    def shortestToChar(S: str, C: str) -> List[int]:
        def min_diff(pos, l):
            min_v = float('inf')
            for v in l:
                v = abs(v-pos)
                min_v = min(min_v, v)
            # print(min_v)
            return min_v
        l_C = []
        for i, v in enumerate(S):
            if v == C:
                l_C.append(i)
        res = [0]*len(S)
        for i, v in enumerate(S):
            if v != C:
                res[i] = min_diff(i, l_C)
        return res

    print(shortestToChar("loveleetcode", 'e'))

    # official solution
    def shortestToCharOfficial(S: str, C: str) -> List[int]:
        prev = float('-inf')
        ans = []
        # L -> R
        for i, v in enumerate(S):
            if v == C:
                prev = i
            ans.append(i-prev)
        # print(ans)
        # R -> L TIPS: INF
        prev = float('inf')
        for i in range(len(S)-1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev-i)
        return ans

    print(shortestToCharOfficial("loveleetcode", 'e'))
