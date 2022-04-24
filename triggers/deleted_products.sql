create trigger deleted_products
after delete
on product_table
for each row
insert into deleted_products values(old.product_id, old.product_name, old.price, old.city_code, old.type_id, old.seller_id);