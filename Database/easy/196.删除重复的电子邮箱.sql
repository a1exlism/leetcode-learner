# @lc app=leetcode.cn
# [196]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
# TIPS: 逐个比对
DELETE a.*
FROM
  Person AS a,
  Person AS b
WHERE
  a.Email = b.Email
  AND a.Id > b.Id;
# @lc code=end
