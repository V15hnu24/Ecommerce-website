delimiter //
create trigger Update_negative_zero
before update on product_table
for each row
if new.price < 0 then set new.price = 0; 
end if; //