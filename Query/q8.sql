select *
from product_table, area_table
where product_table.city_code=area_table.area_Id
and area_table.City_Name=' Belgaum'