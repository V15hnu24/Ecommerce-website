select price,product_name
from product_table
where product_id IN (
	select description_table.product_id as dp
    from description_table
    where long_description Like 'Edition : Paperback%'
    );