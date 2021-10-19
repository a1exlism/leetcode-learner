# @lc app=leetcode.cn
# [627]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
UPDATE
  Salary
SET
  sex = CASE
    sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
  END;
# @lc code=end
