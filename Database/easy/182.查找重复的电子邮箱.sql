# @lc app=leetcode.cn
# [182]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
# 1. Group by & HAVING
SELECT
  Email
FROM
  Person
GROUP BY
  Email
HAVING
  COUNT(Email) > 1;
---
  # 1. SELF JOIN 自连结 (效率太低了!)
SELECT
  DISTINCT a.Email
FROM
  Person AS a
  INNER JOIN Person AS b ON a.Email = b.Email
  AND a.Id <> b.Id;
# @lc code=end
