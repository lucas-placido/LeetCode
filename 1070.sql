SELECT 
    PRODUCT_ID,
    YEAR AS FIRST_YEAR,
    QUANTITY,
    PRICE
FROM(    
    SELECT 
        PRODUCT_ID,
        YEAR,
        QUANTITY,
        PRICE,
        DENSE_RANK() OVER(
            PARTITION BY PRODUCT_ID
            ORDER BY YEAR ASC
        ) AS RANKING
    FROM SALES ) SUB
WHERE RANKING = 1    

-- OR 

SELECT 
    product_id, 
    year as first_year, 
    quantity,
    price
FROM Sales
WHERE (product_id, year) in (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
    )