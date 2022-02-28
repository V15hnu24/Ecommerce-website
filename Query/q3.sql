select price,Product_name
from product_table
where Product_Id IN (
	select description_table.Product_Id as dp
    from description_table
    where Long_description Like '"Edition : Paperback%'
    );