-- 보호소에 들어올 당시에는 중성화 되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물의 아이디와 생물 종, 이름을 조회하는 아이디 순으로 조회


SELECT ANIMAL_ID, ANIMAL_TYPE, NAME
FROM ANIMAL_OUTS
WHERE (SEX_UPON_OUTCOME NOT LIKE 'Intact%')
    AND ANIMAL_ID IN (
        SELECT ANIMAL_ID
        FROM ANIMAL_INS
        WHERE SEX_UPON_INTAKE LIKE 'Intact%')
        
ORDER BY ANIMAL_ID ASC;