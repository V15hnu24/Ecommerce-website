select U.age,count(*) as Number 
from user_details U 
group by 
U.age 
order by U.age 