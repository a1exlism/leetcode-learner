#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
# Tags: [design | trie]

# @lc code=start


class Trie:
    """ ATTENTION 重复前缀, search 需要判断是否截断 """

    def __init__(self):
        self.dict = {}

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie.  """
        d = self.dict
        for w in word:
            if w not in d:
                d[w] = {'END': False}
            d = d[w]
            # print(self.dict)
        d['END'] = True  # last
        # print(self.dict)

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie.  """
        # print(self.dict)
        d = self.dict
        for w in word:
            if w not in d:
                return False
            d = d[w]
        return d['END']

    def startsWith(self, prefix: str) -> bool:
        """ match prefix """
        d = self.dict
        for w in prefix:
            if w not in d:
                return False
            d = d[w]
        return True


class Trie2:
    """ TIPS: tree mode; link node """

    def __init__(self):
        self.suf = {}  # TIPS: indexed pointer
        self.end = False

    def insert(self, word: str) -> None:
        """ Inserts a word into the trie.  """
        p = self
        last = len(word) - 1
        for i, w in enumerate(word):
            if w not in p.suf:
                p.suf[w] = Trie2()
            p = p.suf[w]
        p.end = True  # 表示 p.parent 是 last one, a-p-p-l-e->({}, True)

    def search(self, word: str) -> bool:
        """ Returns if the word is in the trie.  """
        p = self
        for w in word:
            if w not in p.suf:
                return False
            p = p.suf[w]
        return p.end

    def startsWith(self, prefix: str) -> bool:
        """ match prefix """
        p = self
        for w in prefix:
            if w not in p.suf:
                return False
            p = p.suf[w]
        return True


# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":
    word = 'apple'
    prefix = 'app'
    res = []
    # obj = Trie()
    obj = Trie2()
    obj.insert(word)
    res.append(obj.search(word))
    res.append(obj.startsWith(prefix))

    res.append(obj.search(prefix))  # app
    obj.insert(prefix)
    res.append(obj.search(prefix))
    print(res)
# @lc code=end
