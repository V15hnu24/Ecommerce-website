select A.city_name,AVG(Price) as AvgPrice, Count(*) as Number
from (select product_id,price,city_code from 
product_table 
where type_id=(
select type_id
from type_table
where name='bike')
) as P join area_table A 
on P.city_code=A.area_id
Group By
A.city_name
having 
AVG(Price)>1000
Order by A.city_name

