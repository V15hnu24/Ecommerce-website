CREATE TABLE deleted_description_table(
   product_id        INTEGER  NOT NULL 
  ,short_description VARCHAR(199) NOT NULL
  ,long_description  VARCHAR(177) NOT NULL,
  Foreign key (product_id) references deleted_products(product_id)
);
