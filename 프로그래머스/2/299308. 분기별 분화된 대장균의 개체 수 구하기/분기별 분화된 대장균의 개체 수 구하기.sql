SELECT 
    CONCAT(QUARTER(DIFFERENTIATION_DATE),'Q') as QUARTER,
    COUNT(*) as ECOLI_COUNT
FROM ECOLI_DATA
GROUP BY QUARTER
ORDER BY QUARTER