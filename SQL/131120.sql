SELECT MEMBER_ID, MEMBER_NAME, GENDER, 
       DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') AS DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE MONTH(DATE_OF_BIRTH) = 3 AND GENDER = 'W' AND TLNO IS NOT NULL;

# 재구매가 일어난 상품과 회원 리스트 구하기
# https://school.programmers.co.kr/learn/courses/30/lessons/131536
SELECT USER_ID,	PRODUCT_ID
FROM ONLINE_SALE
GROUP BY USER_ID, PRODUCT_ID
HAVING COUNT(*) > 1
ORDER BY 1,2 desc