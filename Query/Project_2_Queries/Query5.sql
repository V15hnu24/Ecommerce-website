select P.product_id,A.city_name as City, P.price as Price, P.seller_id as Seller_id, D.short_description as Description 
from product_table P join 
(select area_table.area_id,area_table.city_name 
from area_table  
where area_table.state_name='Karnataka') as A 
on P.city_code=A.area_id 
join (select type_table.type_id 
from type_table 
where name='bike') as T 
on T.type_id=P.type_id 
join (select product_id,short_description 
from description_table 
where short_description LIKE 'bajaj%' 
)as D 
on D.product_id=P.product_id 
where NOT EXISTS( 
	select product_id 
    from sold_product 
    where P.product_id=sold_product.product_id limit 1 
) 


