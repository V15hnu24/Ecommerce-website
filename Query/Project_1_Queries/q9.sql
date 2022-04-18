select DISTINCT customer_name
from user_details
where user_id In
(select buyer_id
from sold_product 
group by buyer_id
HAVING sum(price)>1000
)
