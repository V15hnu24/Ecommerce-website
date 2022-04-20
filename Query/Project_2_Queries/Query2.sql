select temp1.product_id as ID, 
temp1.Askprice, temp1.SoldPrice 
from(select P.product_id,P.price as AskPrice,S.price as SoldPrice 
from product_table P join sold_product S  
on P.product_id = S.product_id 
where  
P.price-S.price<=1000)AS temp1; 
