SELECT DISTINCT row_count.NUM AS ConsecutiveNums
FROM(
    SELECT 
        NUM, 
        LAG(NUM, 1) OVER() AS preceding,
        LEAD(NUM, 1) OVER() AS following
    FROM LOGS
    ) row_count
WHERE 
    NUM = row_count.preceding
    AND row_count.preceding = row_count.following;