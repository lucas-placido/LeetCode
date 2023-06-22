SELECT DISTINCT s1.*
FROM STADIUM s1
JOIN STADIUM s2
JOIN STADIUM s3
  ON (s1.ID = s2.ID -1 AND s1.ID = s3.ID -2)
  OR (s1.ID = s2.ID -1 AND s1.ID = s3.ID +1)
  OR (s1.ID = s2.ID +1 AND s1.ID = s3.ID +2)
WHERE 
  s1.PEOPLE >= 100 AND
  s2.PEOPLE >= 100 AND 
  s3.PEOPLE >= 100
ORDER BY VISIT_DATE ASC