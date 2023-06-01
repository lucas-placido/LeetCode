WITH CTE AS (
  SELECT 
    person_id,
    person_name,
    weight,
    turn,
    SUM(weight) OVER (ORDER BY turn) AS running_weight
  FROM Queue
)

SELECT person_name
FROM CTE
WHERE turn = (
    SELECT MAX(turn)
    FROM CTE
    WHERE running_weight <= 1000
);