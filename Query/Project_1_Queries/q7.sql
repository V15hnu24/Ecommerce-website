create view sender_ails as
select user_details.customer_name as name , user_details.customer_mobile as phone_number, Age
from user_details
where user_id In (
	select sender_Id
    from chat_table
);

select *
from sender_ails
where Age>20