select sender,receiver,chat,time from(
select U.customer_name as sender, U1.customer_name as receiver, C.chat, C.time
from user_details U join (select sender_id,chat,time,receiver_id,date
from chat_table
where sender_id=1 and receiver_id=9 and date='2020-05-03') as C
on U.user_id = C.sender_id
join user_details U1
on U1.user_id = C.receiver_id
union all
select U.customer_name as sender, U1.customer_name as receiver, C.chat, C.time
from user_details U join (select sender_id,chat,time,receiver_id,date
from chat_table
where sender_id=9 and receiver_id=1 and date='2020-05-03') as C
on U.user_id = C.sender_id
join user_details U1
on U1.user_id = C.receiver_id
) as Temp
Order by Temp.time
