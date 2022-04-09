CREATE TABLE chat_table(
   chat_id     INTEGER  NOT NULL 
  ,sender_id   INTEGER  NOT NULL
  ,receiver_id INTEGER  NOT NULL
  ,chat        VARCHAR(30) NOT NULL
  ,date        DATE  NOT NULL
  ,time        VARCHAR(8) NOT NULL,
  primary KEY (chat_id),
  Foreign key (sender_id) references user_details(user_id),
  Foreign key (receiver_id) references user_details(user_id)
);
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (1,1,9,'Hi','2020-05-03','14:13:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (2,8,2,'Hello','2021-09-02','12:14:33');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (3,5,8,'Best Price?','2022-04-25','13:06:44');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (4,9,4,'5000 is my budget','2020-05-03','09:08:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (5,6,1,'I want to buy','2021-10-02','09:03:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (6,1,9,'Sold','2022-04-25','09:59:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (7,1,4,'Interested','2020-04-03','23:59:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (8,8,1,'I am willing to buy your phone','2021-09-02','00:00:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (9,3,10,'I will report you','2022-04-15','05:08:00');
INSERT INTO chat_table(chat_id,sender_id,receiver_id,chat,date,time) VALUES (10,1,10,'I want to buy','2022-05-12','06:03:00');
