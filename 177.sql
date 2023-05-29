CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      SELECT MAX(rank_table.SALARY) AS getNthHighestSalary
      FROM(
      SELECT SALARY,
        DENSE_RANK() OVER (ORDER BY SALARY DESC) AS RANKING
      FROM EMPLOYEE
      ) AS rank_table
      WHERE RANKING = N
  );
END