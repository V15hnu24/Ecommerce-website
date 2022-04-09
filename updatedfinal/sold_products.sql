CREATE TABLE sold_product(
   bought_id  INTEGER  NOT NULL
  ,buyer_id   INTEGER  NOT NULL
  ,product_id INTEGER  NOT NULL
  ,date       DATE  NOT NULL
  ,price      INTEGER  NOT NULL,
  Primary key (bought_id),
  Foreign key (buyer_id) references user_details(user_id),
  Foreign key (product_id) references product_table(product_id)
);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (1,62,12,'2020-05-03',8407);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (2,40,25,'2021-09-02',3573);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (3,87,3845,'2022-04-25',1908);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (4,53,4648,'2020-05-03',2917);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (5,31,504,'2021-10-02',6918);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (6,41,6,'2022-04-25',2354);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (7,50,702,'2020-04-03',4311);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (8,75,8,'2021-09-02',6633);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (9,78,9,'2022-04-15',1809);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (10,63,10,'2022-05-12',4692);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (11,33,1251,'2021-10-02',4741);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (12,31,192,'2022-04-25',9150);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (13,76,5000,'2020-04-03',2297);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (14,72,14,'2021-09-02',2064);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (15,27,1845,'2022-04-25',7815);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (16,42,16,'2021-10-02',6430);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (17,96,1007,'2022-04-25',3665);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (18,94,7000,'2020-04-03',1279);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (19,55,1349,'2021-09-02',7630);
INSERT INTO sold_product(bought_id,buyer_id,product_id,date,price) VALUES (20,71,20,'2022-04-25',9728);
