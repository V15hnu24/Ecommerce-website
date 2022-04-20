select length(chat),count(*) as length  
from chat_table 
group by 
length(chat) 
order by 
length(chat) 
