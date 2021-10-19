# @lc app=leetcode.cn
# [620]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
SELECT
  *
FROM
  cinema
WHERE
  id & 1
  AND description NOT LIKE '%boring%'
ORDER BY
  rating DESC;
# @lc code=end
