# @lc app=leetcode.cn
# [197]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
SELECT
  b.id
FROM
  Weather AS a
  INNER JOIN Weather AS b ON DATEDIFF(a.recordDate, b.recordDate) = -1
WHERE
  a.Temperature < b.Temperature;
# @lc code=end
