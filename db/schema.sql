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

CREATE TABLE if NOT EXISTS item(
    id integer primary key autoincrement,
    name string not null,
    count integer not null default 0,
    price integer not null default 0
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

INSERT OR IGNORE INTO item (id, name, count, price) VALUES (1, 'shield', 0, 30);
INSERT OR IGNORE INTO item (id, name, count, price) VALUES (2, 'life', 0, 30);
INSERT OR IGNORE INTO item (id, name, count, price) VALUES (3, 'slow', 0, 30);
INSERT OR IGNORE INTO item (id, name, count, price) VALUES (4, 'coin', 0, 30);
INSERT OR IGNORE INTO skin (id, name, is_paid, is_apply, price)
                VALUES(1, "Spring", 0, 0, 1000);
INSERT OR IGNORE INTO skin (id, name, is_paid, is_apply, price)
                VALUES(2, "Fall", 0, 0, 1000);
INSERT OR IGNORE INTO skin (id, name, is_paid, is_apply, price)
                VALUES(3, "Winter", 0, 0, 1000);

insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(1, "Purple", 0,  0,  500);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(2, "Red", 0, 0, 500);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(3, "Yellow", 0, 0, 500);
insert or ignore into character (id, name, is_paid, is_apply, price)
                            values(4, "Tux", 0, 0, 3000);