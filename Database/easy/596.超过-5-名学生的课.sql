# @lc app=leetcode.cn
# [596]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
SELECT
  class
FROM
  courses
GROUP BY
  class
HAVING
  COUNT(DISTINCT student) >= 5;
# @lc code=end
