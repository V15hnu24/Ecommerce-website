CREATE TABLE type_table(
   type_Id     INTEGER  NOT NULL PRIMARY KEY 
  ,total_items INTEGER  NOT NULL
  ,name        VARCHAR(11) NOT NULL
);
INSERT INTO type_table(type_Id,total_items,name) VALUES (3,1223,'mobile');
INSERT INTO type_table(type_Id,total_items,name) VALUES (2,301,'car');
INSERT INTO type_table(type_Id,total_items,name) VALUES (1,32647,'bike');
INSERT INTO type_table(type_Id,total_items,name) VALUES (4,204,'electronics');
INSERT INTO type_table(type_Id,total_items,name) VALUES (5,6236,'other');
