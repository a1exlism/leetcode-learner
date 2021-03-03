# ATTENTION: RE-TRAIN THIS
# TIPS: Always base type: [count, string]
from typing import Tuple


class Solution:
    @staticmethod
    # TIPS: iteration
    # def decodeString(self, s: str) -> str:
    def decodeString1(s: str) -> str:
        aux = []
        c = 0
        res = ''  # tmp string
        for v in s:
            if v.isdigit():
                c = c * 10 + int(v)
            elif v.isalpha():
                res += v
            elif v == '[':
                aux.append([c, res])
                c = 0
                res = ''  # ATTENTION: RESET
            else:
                # print(f'aux_s{aux_s}:aux_c{aux_c}')
                tmp = aux.pop()
                res = tmp[1] + res * tmp[0]
        return res

    @staticmethod
    # TIPS: recurrence
    def decodeString(s: str) -> str:
        def decode(i: int) -> Tuple[int, str]:
            mul = 0
            res = ''
            while(i < len(s)):
                v = s[i]
                if v.isdigit():
                    mul = mul * 10 + int(v)
                elif v.isalpha():
                    res += v
                elif v == '[':
                    # construction of sub-string
                    i, tmp_s = decode(i+1)
                    res = res + tmp_s * mul
                    mul = 0  # ATTENTION new Environment
                else:
                    return i, res
                i += 1
            return res
        return decode(0)


if __name__ == '__main__':
    r1 = Solution.decodeString('2[a]')
    print(r1)  # "aaa"
    r2 = Solution.decodeString('3[a]2[b]')
    print(r2)  # "aaabb"
    r3 = Solution.decodeString('2[a10[c]]')
    print(r3)  # "accccccccccacccccccccc"
    r4 = Solution.decodeString('a2[2[c]]')
    print(r4)  # "acccc"
