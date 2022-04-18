update product_table
set price = price*1.5
where type_id = (
    select type_Id
    from type_table
    where type_table.name = 'bike'
);