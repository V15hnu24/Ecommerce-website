CREATE TABLE IF NOT EXISTS deleted_products(
product_id INTEGER,
product_name VARCHAR(400),
price DECIMAL(10,3),
city_code INTEGER,
type_id INTEGER,
seller_id INTEGER,
primary key(product_id),
Foreign key (type_id) references type_table(type_id),
Foreign key (city_code) references area_table(area_id),
Foreign key (seller_id) references user_details(user_id)
);