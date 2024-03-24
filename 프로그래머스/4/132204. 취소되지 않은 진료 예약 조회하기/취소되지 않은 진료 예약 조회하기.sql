SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, A.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT as A
LEFT OUTER JOIN PATIENT as P ON A.PT_NO = P.PT_NO
LEFT OUTER JOIN DOCTOR as D ON A.MDDR_ID = D.DR_ID
WHERE A.APNT_YMD LIKE "2022-04-13%" and A.MCDP_CD = 'CS' and A.APNT_CNCL_YN = 'N'
ORDER BY A.APNT_YMD asc
