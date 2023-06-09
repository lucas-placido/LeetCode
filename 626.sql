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