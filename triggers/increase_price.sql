create trigger increase_price
before insert
on product_table
for each row
set new.price = new.price + 1000;
