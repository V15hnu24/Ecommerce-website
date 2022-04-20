
select temp.user_id,temp.Selling_amount,IFNULL(Bought_amount, 0 ) as Bought_amount FROM ( 
select P.seller_id as user_id, SUM(P.price) as Selling_Amount, SUM(S.price) as Bought_amount 
from product_table P left join sold_product S 
on P.product_id=S.product_id 
Group by  
P.seller_id 
Order by 
P.seller_id 
) as temp
