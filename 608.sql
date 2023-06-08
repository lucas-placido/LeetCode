SELECT DISTINCT
  t1.id,
  CASE
    WHEN t1.p_id IS NULL THEN "Root"
    WHEN t2.id IS NULL THEN "Leaf"
    ELSE "Inner"
  END AS type
FROM TREE t1
LEFT JOIN TREE t2
  ON t1.id = t2.p_id