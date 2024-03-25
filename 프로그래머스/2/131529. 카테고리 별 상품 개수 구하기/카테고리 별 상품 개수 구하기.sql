SELECT left(PRODUCT_CODE, 2) CATEGORY, 
    COUNT(PRODUCT_CODE) PRODUCTS
FROM PRODUCT
GROUP BY (left(PRODUCT_CODE, 2))
ORDER BY 1;