select DISTINCT customer_name
from user_details
where user_id In
(select buyer_id
from bought_table 
group by buyer_id
HAVING sum(Price)>1000
)
