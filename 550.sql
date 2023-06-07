SELECT 
    ROUND(
        COUNT(DISTINCT b.PLAYER_ID) / 
        COUNT(DISTINCT a.PLAYER_ID) 
    , 2) AS fraction
FROM
    (SELECT
        PLAYER_ID,
        MIN(EVENT_DATE) AS FIRST_DAY
    FROM ACTIVITY
    GROUP BY PLAYER_ID
    ) a
LEFT JOIN ACTIVITY b
    ON a.PLAYER_ID = b.PLAYER_ID 
    AND DATEDIFF(b.EVENT_DATE, a.FIRST_DAY) = 1    