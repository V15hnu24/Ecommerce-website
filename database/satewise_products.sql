create table statewise_products(
	state_code	integer not null AUTO_INCREMENT,
    state varchar(125),
    total_products integer
    ,primary key (state_code)
);