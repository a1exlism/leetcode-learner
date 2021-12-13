# readme DP

## 状态转移方程

1. 322.零钱兑换

   - c: coin; S: amount(sum)
   - 转移方程: $f(S)=\min\limits_{0,\dots,n}f(S-c)+1$

2. 5.最长回文子串

   - i, j = substring index, dp[i][j]: `bool`
   - 初始状态: $i==j \to dp[i][j]=\text{True}$
   - 转移方程: $f(i,j)=f(i+1,j-1)\wedge s_i\equiv s_j$
   - 边界: $f(i,i) = \text{True}; f(i,i+1) == s_i\equiv s_{i+1}$
