SELECT 
    ID,
    SUM(CT) AS NUM
FROM (
    SELECT 
        requester_id AS ID, 
        COUNT(requester_id) AS CT
    FROM RequestAccepted
    GROUP BY requester_id

    UNION ALL
    
    SELECT 
        accepter_id AS ID,
        COUNT(accepter_id) AS CT
    FROM RequestAccepted
    GROUP BY accepter_id
) sub
GROUP BY ID
ORDER BY NUM DESC
LIMIT 1