select p.product_code, (p.price * a.sales_amount ) as sales
from product p 
left join
    (select product_id, sum(sales_amount) as sales_amount 
    from offline_sale 
    group by product_id) as a on p.product_id= a.product_id
group by product_code
order by sales desc, product_code asc
