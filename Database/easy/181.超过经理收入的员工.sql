# @lc app=leetcode.cn
# [181]
# Tags: [database]
# Difficulty:[easy]
# TIPS: 想的有点久, 一个表当两个表处理
# @lc code=start
select
  sub.Name as `Employee`
from
  Employee as mng,
  Employee as sub
WHERE
  mng.Id = sub.ManagerId
  and mng.Salary < sub.Salary;
# same as INNER JOIN
SELECT
  Name as `Employee`
FROM
  Employee AS sub
  INNER JOIN Employee AS mng ON sub.sub.ManagerId = mng.Id
WHERE
  and sub.Salary > mng.Salary
# @lc code=end
