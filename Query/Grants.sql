show grants for root@localhost;

GRANT SELECT ON TABLE user_details TO root@localhost;
GRANT  create, select on table product_table to root@localhost;
grant update on table user_details to root@localhost;
grant delete on table product_table to root@localhost;
GRANT ALTER on Table description_table to root@localhost;

revoke create, select on table product_table from root@localhost;