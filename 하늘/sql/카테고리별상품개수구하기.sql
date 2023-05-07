
### SQL 문자열 다루기(slice)!! left(컬럼, 숫자) ## 왼쪽에서 두글자까지 slicing

SELECT left(PRODUCT_CODE,2) as CATEGORY ,COUNT(PRODUCT_CODE) AS PRODUCTS
FROM PRODUCT
group by CATEGORY
