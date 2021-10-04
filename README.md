# leetcode-learner

直接全文检索，带正则 `[.*KEYWORDS.*]`

## strategy

### tags

- memo 记忆化

### contents

1. 二分 $\to$ 分治
2. 滑动窗口
3. 搜索 BFS, DFS, 回溯
4. 贪心+回溯 $\to$ 动态规划
   - 回溯算法就是个 N 叉树的前后序遍历问题 [ref][fa1]
   - dp ~= 记忆化递归
5. 背包
6. 位运算

### [贪心][91lecture-greddy]

1. 适用场景
   1. 局部最优解能得到整体的最优解
   2. 贪心选择不会影响以后的状态，只与`当前状态`有关
2. 贪心 + 回溯 = 动态规划
3. 贪心算法的`难点`在于如何知道贪心的策略是正确的, 证明方法:
   1. 反证法
   2. 数学归纳法

## 题目归类

- [DP1][dp-1], [DP2][dp-2]
- [Math][math]
- [Memoization][memoization]

[math]: http://www.leetcodecn.com/pages/255f98/#leetcode-%E9%A2%98%E8%A7%A3---%E6%95%B0%E5%AD%A6
[memoization]: https://leetcode-cn.com/tag/memoization/
[dp-1]: https://leetcode-cn.com/tag/dynamic-programming/problemset/
[dp-2]: https://github.com/leetcode-pp/91alg-3/blob/master/lecture/topic-dp.md

<!-- REFER: 91alg -->

[91lecture-greddy]: https://github.com/leetcode-pp/91alg-3/blob/master/lecture/topic-greedy.md

<!-- REFER: fa -->

[fa1]: https://github.com/labuladong/fucking-algorithm/blob/master/%E7%AE%97%E6%B3%95%E6%80%9D%E7%BB%B4%E7%B3%BB%E5%88%97/%E5%AD%A6%E4%B9%A0%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E5%92%8C%E7%AE%97%E6%B3%95%E7%9A%84%E9%AB%98%E6%95%88%E6%96%B9%E6%B3%95.md
