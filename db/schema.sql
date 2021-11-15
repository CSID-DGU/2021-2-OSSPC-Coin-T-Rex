create table if not exists easy_mode (
    user_id integer primary key autoincrement,
    username string not null,
    score string not null
);

create table if not exists hard_mode (
    user_id integer primary key autoincrement,
    username string not null,
    score string not null
);

create table if not exists item (
    item_id integer primary key autoincrement,
    shield integer not null default 0,
    life integer not null default 0,
    slow integer not null default 0,
    coin integer not null default 0,
    shield_price integer not null default 0,
    life_price integer not null  default 0,
    slow_price integer not null default 0
);

create table if not exists skin (
    id integer primary key autoincrement,
    name string not null,
    is_paid integer default 0,
    is_apply integer default 0,
    price integer default 0
);

create table if not exists character (
    id integer primary key autoincrement,
    name string not null,
    is_paid integer default 0,
    is_apply integer default 0,
    price integer default 0
);

insert or ignore into item (item_id, shield, life, slow, coin, shield_price, life_price, slow_price)
                 values (1, 5, 5, 5, 5, 1, 1, 1);

insert or ignore into skin (id, name, is_paid, is_apply, price)
                values(1, "Spring", 0, 0, 1);
insert or ignore into skin (id, name, is_paid, is_apply, price)
                values(2, "Fall", 0, 0, 1);
insert or ignore into skin (id, name, is_paid, is_apply, price)
                values(3, "Winter", 0, 0, 1);

insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(1, "Purple", 0,  0,  1);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(2, "Red", 0, 0, 1);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(3, "Yellow", 0, 0, 1);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(4, "Tux", 0, 0, 1);