# @lc app=leetcode.cn
# [175] 组合两个表
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
SELECT
  Person.FirstName,
  Person.LastName,
  Address.City,
  Address.State
FROM
  Person
  LEFT JOIN Address ON Person.PersonId = Address.PersonId;
# 无论 person 是否有地址信息，都需要基于上述两表提供 `person` 的以下信息
  # @lc code=end
