# @lc app=leetcode.cn
# [183]
# Tags: [database]
# Difficulty:[easy]
# @lc code=start
# join
SELECT
  Name AS `Customers`
FROM
  Customers AS a
  LEFT JOIN Orders AS b ON a.Id = b.CustomerId
WHERE
  b.CustomerID is NULL;
# warning: 不推荐
SELECT
  Name AS `Customers`
FROM
  Customers
WHERE
  Id not IN (
    SELECT
      CustomerId
    FROM
      Orders
  );;
# @lc code=end
