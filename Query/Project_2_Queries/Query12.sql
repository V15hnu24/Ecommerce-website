select U.user_id, U.customer_name, Count(*)
from user_details U
join chat_table C
on C.sender_id =
U.user_id
Group by 
U.user_id
order by
U.user_id