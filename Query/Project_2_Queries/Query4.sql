select U.user_id, Count(*) as NumberofMsgs
from user_details U join chat_table C
on U.user_id=C.sender_id
Group by 
C.sender_id
having 
Count(distinct receiver_id)>1
order by
C.sender_id
