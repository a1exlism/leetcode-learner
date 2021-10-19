# @lc app=leetcode.cn
# [595]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
SELECT
  name,
  population,
  area
FROM
  World
WHERE
  population > 25000000
  OR area > 3000000;
# BETTER
SELECT
  name,
  population,
  area
FROM
  World
WHERE
  population > 25000000
UNION
SELECT
  name,
  population,
  area
FROM
  World
WHERE
  area > 3000000;
# @lc code=end
