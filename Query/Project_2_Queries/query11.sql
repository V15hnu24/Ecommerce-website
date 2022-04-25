select T.type_id,T.name,AVG(P.price),Count(*)
from type_table T
join product_table P
on P.type_id=T.type_id
group by
T.type_id
order by T.type_id