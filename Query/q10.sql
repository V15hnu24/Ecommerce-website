Create view chat_1_10 as 
select chat 
from chat_table
where sender_Id=1 and receiver_Id=10
and date='2022-05-12'

select *
from chat_1_10