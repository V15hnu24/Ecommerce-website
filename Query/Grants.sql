create user Manoj identified by "Manoj@123";
create user  samriddh identified by "1234";
create user vishnu identified by "6789";
create user varun identified by "Varun@123";
create user customer_1 identified by "0123";
create user customer_2 identified by "3456";
create user customer_3 identified by "qwerty@123";
create user customer_4 identified by "asdf@1234";
create user customer_5 identified by "zxcv@1234";
create user owner_1 identified by "owner@123";
GRANT TRIGGER ON table user_details to Manoj;
grant select on * to owner_1;
grant delete on * to owner_1;
grant update on * to owner_1;
grant index on * to owner_1;
grant insert on * to owner_1;
grant delete on * to owner_1;
grant drop on * to owner_1;
GRANT CREATE, SELECT ON TABLE user_details TO Manoj;
GRANT update on table user_details TO Manoj;
grant delete on table user_details TO Manoj;
grant alter on table user_details TO Manoj;
grant delete on table product_table TO Manoj;
grant create,select,update,delete,alter on table product_table to samriddh;
revoke create, select on table product_table from Manoj;
