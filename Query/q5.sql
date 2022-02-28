update product_table
set price = price*1.5
where type = (
    select type_Id
    from type_table
    where name = 'bike'
);