WITH BONUS_INFO AS (
    SELECT EMP_NO, AVG(SCORE) as SCORE
    FROM HR_GRADE
    WHERE YEAR = 2022
    GROUP BY EMP_NO
), HR_BONUS AS (
    SELECT EMP_NO,
        CASE
            WHEN SCORE >= 96 THEN 'S'
            WHEN SCORE >= 90 THEN 'A'
            WHEN SCORE >= 80 THEN 'B'
            ELSE 'C'
        END AS GRADE,
        CASE
            WHEN SCORE >= 96 THEN 20
            WHEN SCORE >= 90 THEN 15
            WHEN SCORE >= 80 THEN 10
            ELSE 0
        END AS BONUS
    FROM BONUS_INFO
)

SELECT e.EMP_NO, e.EMP_NAME, b.GRADE, 
    (b.BONUS/100) * e.SAL as BONUS
FROM HR_EMPLOYEES as e
        JOIN (
            SELECT *
            FROM HR_BONUS
        ) as b on e.EMP_NO = b.EMP_NO
ORDER BY 1 ASC;