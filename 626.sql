-- USING WINDOW FUNCTIONS 
SELECT
    id,
    CASE    
        WHEN id % 2 = 1 THEN LEAD(student, 1, student) OVER(ORDER BY ID)
        ELSE LAG(student) OVER(ORDER BY ID)
    END AS student
FROM Seat

-- OR
SELECT
  IF(id < (SELECT MAX(id) FROM Seat),

    CASE 
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1 
    END,
      
    CASE 
        WHEN id % 2 = 0 THEN id - 1
        ELSE id 
    END) as id,
    student
FROM Seat
ORDER BY id