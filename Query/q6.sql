select product_id, product_name, price, city_code, type_id, 'bike' as category
from product_table
where type_id = (
    select type_Id
    from type_table
    where name = 'bike'
)
union 
select Product_Id, Product_name, Price, city_code, type_id, 'car' as category
from product_table
where type_id = (
    select type_Id
    from type_table
    where name = 'car'
)
union 
select Product_Id, Product_name, Price, city_code, type_id, 'mobile' as category
from product_table
where type_id= (
    select type_Id
    from type_table
    where name = 'mobile'
)
union 
select Product_Id, Product_name, Price, city_code, type_id, 'other' as category
from product_table
where type_id= (
    select type_Id
    from type_table
    where name = 'other'
)
union 
select Product_Id, Product_name, Price, city_code, type_id, 'electronics' as category
from product_table
where type_id= (
    select type_Id
    from type_table
    where name = 'electronics'
);