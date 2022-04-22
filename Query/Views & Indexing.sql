show tables;
use manoj;
create view user_details1 as select * from user_details INNER JOIN sold_product on sold_product.buyer_id=user_details.user_id;
select * from user_details1;
select * from sold_product;
create index Email_Index on user_details (customer_email);
show indexes from user_details;

create view area_products as select * from area_table INNER JOIN product_table on product_table.product_id = area_table.area_id ;
select * from area_products;
select * from product_table;
create index Product_index on product_table (product_name);
create index Area_index on product_table (city_code);
show indexes from product_table;
create view category_sale as select product_table.product_id,product_table.product_name,product_table.price,sold_product.buyer_id,sold_product.sell_price,product_table.type_id from product_table Inner join sold_product on sold_product.product_id=product_table.product_id;
select * from category_sale where type_id='5';