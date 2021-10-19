# MySQL Cheat Sheet

copy from [gist][gist]

> Help with SQL commands to interact with a MySQL database

## Database

### Show Databases

```sql
SHOW DATABASES
```

### Create Database

```sql
CREATE DATABASE acme;
```

### Delete Database

```sql
DROP DATABASE acme;
```

### Select Database

```sql
USE acme;
```

## Table

### Create Table

```sql
CREATE TABLE users(
id INT AUTO_INCREMENT,
   first_name VARCHAR(100),
   last_name VARCHAR(100),
   email VARCHAR(50),
   password VARCHAR(20),
   location VARCHAR(100),
   dept VARCHAR(100),
   is_admin TINYINT(1),
   register_date DATETIME,
   PRIMARY KEY(id)
);
```

### Delete / Drop Table

```sql
DROP TABLE tablename;
```

### Show Tables

```sql
SHOW TABLES;
```

## CRUD(Row)

### Insert

- Single row

  ```sql
  INSERT INTO
  users (first_name, last_name, is_admin, register_date)
  VALUES ('Brad', 'Traversy', 1, now());
  ```

- Multiple Rows

  ```sql
  INSERT INTO
    users ( first_name, last_name, is_admin, register_date)
  VALUES
    ('Fred', 'Smith', 0, now()),
    ('Sara', 'Watson', 0, now());
  ```

### \*Select

- base

  ```sql
  SELECT * FROM users;
  SELECT first_name, last_name FROM users;
  ```

- Concatenate Columns

  ```sql
  SELECT CONCAT(first_name, ' ', last_name) AS 'Name', dept FROM users;
  ```

- Distinct
  select all distinct values

  ```sql
  SELECT DISTINCT location FROM users;
  ```

- Range Query

  ```sql
  SELECT * FROM users WHERE age BETWEEN 20 AND 25;
  ```

- Fuzzy Query(Like/Not Like)

  ```sql
  SELECT * FROM users WHERE dept LIKE 'd%';
  SELECT * FROM users WHERE dept LIKE 'dev%';
  SELECT * FROM users WHERE dept LIKE '%t';
  SELECT * FROM users WHERE dept LIKE '%e%';
  # NOT LIKE
  SELECT * FROM users WHERE dept NOT LIKE 'd%';
  ```

- Order By (Sort)

  ```sql
  SELECT * FROM users ORDER BY last_name ASC;
  SELECT * FROM users ORDER BY last_name DESC;
  ```

- Union Select(OR)

  ```sql
  SELECT * FROM users WHERE dept LIKE 'd%'
  UNION
  SELECT * FROM users WHERE dept LIKE '%dev%';
  ```

- symbol escape
  search value contains `%` symbol itself

  ```sql
  SELECT *
  FROM users WHERE column_X LIKE '%\%%'
  ```

### Delete

```sql
DELETE FROM users WHERE id = 6;
```

- refer [Delete][sql-delete]
  两个表做比对删除, 行数目 ≤ row(SELECT), 以下表示为
  仅保留同名 min(id) 的行

  ```sql
  DELETE FROM users AS a, users AS b
  WHERE a.name = b.name AND a.id > b.id;
  ```

### Update

```sql
UPDATE users SET email = 'freddy@gmail.com' WHERE id = 2;
```

## AS alias

### column alias

```sql
SELECT CustomerName, CustomerName, CONCAT(Address,', ',PostalCode,', ',City,', ',Country) AS Address
FROM Customers;
```

### tables alias

```sql
SELECT * FROM users AS u WHERE u.age > 10;
```

## Filter

### Usage Orders

```sql
WHERE > GROUP BY > HAVING > ORDER BY
```

### Where Clause

```sql
SELECT * FROM users WHERE location='Massachusetts';
SELECT * FROM users WHERE location='Massachusetts' AND dept='sales';
SELECT * FROM users WHERE is_admin = 1;
SELECT * FROM users WHERE is_admin > 0;
```

- `IN` 多个 OR 简写

  ```sql
  SELECT * FROM users WHERE dept IN ('design', 'sales');
  SELECT * FROM users WHERE dept not IN (SELECT dept FROM users2);
  ```

### Group By

- 聚合函数 [aggregation](#aggregate-functions)
- group by 字段和 select 字段必须是**同一个**
- code

  ```sql
  SELECT age, COUNT(age) FROM users GROUP BY age;
  ```

- Filter

  ```sql
  SELECT age, COUNT(age) FROM users WHERE age > 20 GROUP BY age;
  SELECT age, COUNT(age) FROM users GROUP BY age HAVING count(age) >=2;
  SELECT age FROM users GROUP BY age HAVING count(DISTINCT age) >=2;
  ```

### Limit

top-10

```sql
SELECT * FROM dept_emp LIMIT 10;
```

## Index

索引 [Index][index]

### Create & Remove

```sql
CREATE INDEX LIndex On users(location);
DROP INDEX LIndex ON users;
```

### New Table With Foreign Key(s)

```sql
CREATE TABLE posts(
id INT AUTO_INCREMENT,
   user_id INT,
   title VARCHAR(100),
   body TEXT,
   publish_date DATETIME DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY(id),
   FOREIGN KEY (user_id) REFERENCES users(id),
   # FOREIGN KEY(post_id) references posts(id)
);
```

## Join

多个数据表中读取数据, joined table indices: `A|B`;
`ON` 类比于 select 中的 `WHERE`;

![sql-join](/imgs/sql-join.jpg)

### Inner Join

$A\cap B$, 获取两个表中字段匹配关系的记录

```sql
SELECT
  users.first_name,
  users.last_name,
  posts.title,
  posts.publish_date
FROM users
INNER JOIN posts
ON users.id = posts.user_id
ORDER BY posts.title;
```

### Left/Right Join

Left: 获取左表所有记录，即使右表 `没有` 对应匹配的记录;
Right 同理

left/right join 之后的 number(rows) = max(#(rowsA), #(rowsB))

```sql
SELECT
  comments.body,
  posts.title
FROM
  comments
  LEFT JOIN posts ON posts.id = comments.post_id
ORDER BY
  posts.title;
```

### Join Multiple Tables

```sql
SELECT
  comments.body,
  posts.title,
  users.first_name,
  users.last_name
FROM
  comments
  INNER JOIN posts on posts.id = comments.post_id
  INNER JOIN users on users.id = comments.user_id
ORDER BY
  posts.title;
```

### Cross Join

全集 $A\cup B$, 笛卡尔积 (Cartesian product), low performance

```sql
SELECT column_name(s)
FROM table1
CROSS JOIN table2;
```

## Functions

### Basic

与 `C` 基本一致;
包括算术/逻辑运算/位运算;
比较运算有点区别: `>=`, `IS NULL`, `BETWEEN AND`;

### Case

```sql
UPDATE
  Salary
SET
  sex = CASE
    sex
    WHEN 'm' THEN 'f'
    # WHEN * TEN *
    ELSE 'm'
  END;
```

### Aggregation

```sql
SELECT COUNT(id) FROM users;
SELECT MAX(age) FROM users;
SELECT MIN(age) FROM users;
SELECT SUM(age) FROM users;
SELECT UCASE(first_name), LCASE(last_name) FROM users;
```

## Alter(Column)

- add

  ```sql
  ALTER TABLE users ADD age VARCHAR(3);
  ```

- Modify

  ```sql
  ALTER TABLE users MODIFY COLUMN age INT(3);
  ```

## Settings

### MySQL Locations

- Mac _/usr/local/mysql/bin_
- Windows _/Program Files/MySQL/MySQL *version*/bin_
- Xampp _/xampp/mysql/bin_

### Add mysql to your PATH

```bash
# Current Session
export PATH=${PATH}:/usr/local/mysql/bin
# Permanantly
echo 'export PATH="/usr/local/mysql/bin:$PATH"' >> ~/.bash_profile
```

On Windows - https://www.qualitestgroup.com/resources/knowledge-center/how-to-guide/add-mysql-path-windows/

### Login

```bash
>$ mysql -u root -p
```

## Users

### Show Users

```sql
SELECT User, Host FROM mysql.user;
```

### Create User

```sql
CREATE USER 'someuser'@'localhost' IDENTIFIED BY 'somepassword';
```

### Grant All Priveleges On All Databases

```sql
GRANT ALL PRIVILEGES ON * . * TO 'someuser'@'localhost';
FLUSH PRIVILEGES;
```

### Show Grants

```sql
SHOW GRANTS FOR 'someuser'@'localhost';
```

### Remove Grants

```sql
REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'someuser'@'localhost';
```

### Delete User

```sql
DROP USER 'someuser'@'localhost';
```

## Reference

database test: https://github.com/datacharmer/test_db

dict1: https://www.w3schools.com/mysql/mysql_in.asp
dict2: https://www.runoob.com/mysql/mysql-union-operation.html
sql-join: https://leetcode-cn.com/problems/customers-who-never-order/solution/tu-jie-sqlmian-shi-ti-cha-zhao-bu-zai-biao-li-de-s/

[gist]: https://gist.githubusercontent.com/bradtraversy/c831baaad44343cc945e76c2e30927b3/raw/2d4ec3c63651d7f42fd6a503bb5d2b4feaadb5fd/mysql_cheat_sheet.md
[index]: https://www.runoob.com/mysql/mysql-index.html
[sql-delete]: https://leetcode-cn.com/problems/delete-duplicate-emails/solution/dui-guan-fang-ti-jie-zhong-delete-he-de-jie-shi-by/
