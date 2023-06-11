SELECT 
    U.USER_ID AS buyer_id,     
    U.JOIN_DATE AS join_date,
    SUM(
        IF(YEAR(ORDER_DATE) = 2019, 1, 0)) AS orders_in_2019    
FROM USERS U
LEFT JOIN ORDERS O
    ON U.USER_ID = O.BUYER_ID 
GROUP BY 
    U.USER_ID, 
    U.JOIN_DATE