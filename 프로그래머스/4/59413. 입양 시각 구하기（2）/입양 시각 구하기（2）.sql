with recursive rc as
(
    select 0 as n
    union
    select n+1 from rc where n < 23
)


SELECT A.HOUR, SUM(A.COUNT)
FROM
(
    SELECT N as HOUR, 0 as COUNT from rc
    UNION
    SELECT HOUR(DATETIME) as HOUR, COUNT(ANIMAL_ID) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
) A
GROUP BY HOUR
ORDER BY HOUR ASC;