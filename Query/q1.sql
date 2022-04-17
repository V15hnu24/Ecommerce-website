select product_table.Product_name
from product_table 
where product_table.city_code In (
	select area_Id
    from area_table
    where state_name = 'Karnataka');