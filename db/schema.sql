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
    coin integer not null default 0
);

create table if not exists skin (
    id integer primary key autoincrement,
    name string not null,
    is_paid integer default 0,
    is_apply integer default 0
);

create table if not exists character (
    id integer primary key autoincrement,
    name string not null,
    is_paid integer default 0,
    is_apply integer default 0
);

insert or ignore into item values (1, 5, 5, 5, 5);