select DISTINCT(seller_id) from (
select seller_id
from product_table
) AS temp1
where seller_id NOT IN(
SELECT seller_id FROM (select* from
(select DISTINCT(seller_id)
from product_table) AS temp2 cross join (select type_id
from type_table) AS temp3)AS temp4
WHERE (seller_id,type_id) NOT IN
( select seller_id,type_id
from product_table
));

