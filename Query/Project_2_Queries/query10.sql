select U.user_id, U.customer_name, U.age 
from user_details U  
where EXISTS( 
	select P.seller_id 
    from product_table P 
    where U.user_id=P.seller_id limit 1) 
 and EXISTS( 
 select S.bought_id 
 from sold_product S 
 where S.bought_id=U.user_id limit 1 
	) 
order by user_id 
