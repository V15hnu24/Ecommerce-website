
CREATE INDEX Prdt_Table ON product_table(city_code,price);

CREATE INDEX ar_tbl ON  area_table(pincode);

CREATE INDEX cht_tbl ON chat_table(sender_id,receiver_id);

CREATE INDEX shrt_desp ON  description_table(short_description);

CREATE INDEX sld_pdt ON  sold_product(buyer_id,product_id);

CREATE INDEX typ_table ON  type_table(total_items);

CREATE INDEX usr_tbl ON  user_details(age,customer_email)

