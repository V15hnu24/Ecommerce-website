create trigger deleted_descriptions
after delete
on description_table
for each row
insert into deleted_description_table values(old.product_id, old.short_description, old.long_description);
