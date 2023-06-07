SELECT 
    d.NAME AS DEPARTMENT,
    e1.NAME AS EMPLOYEE,
    e1.SALARY AS SALARY
FROM EMPLOYEE e1
JOIN DEPARTMENT d 
    ON e1.DEPARTMENTID = d.ID
WHERE (
    SELECT COUNT(DISTINCT e2.SALARY)
    FROM EMPLOYEE e2
    WHERE e2.DEPARTMENTID = e1.DEPARTMENTID 
        AND e2.SALARY > e1.SALARY) < 3
ORDER BY 
    SALARY DESC;