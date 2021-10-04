

def subs(s):
    """ 列举所有子串 """
    l = []
    slen = len(s)
    for i in range(slen):
        for j in range(i+1, slen+1):
            # 这里注意 slen+1, 因为 s[i:j] 左闭右开
            l.append(s[i: j])
    return l
