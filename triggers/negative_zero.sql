delimiter //
create trigger negative_zero
before insert on product_table
for each row
if new.price < 0 then set new.price = 0; 
end if; //