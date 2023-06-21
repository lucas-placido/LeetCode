SELECT S.USER_ID AS user_id,
    ROUND(
        AVG(IF(ACTION = 'confirmed', 1, 0)) ,2) AS confirmation_rate
FROM SIGNUPS S
LEFT JOIN CONFIRMATIONS C
    ON S.USER_ID = C.USER_ID
GROUP BY USER_ID    