DROP TABLE IF EXISTS attendees;
DROP TABLE IF EXISTS festivals;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;


CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country_code VARCHAR(255)
);

CREATE TABLE festivals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    country_id INT REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE attendees (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    festival_id INT REFERENCES festivals(id) ON DELETE CASCADE
);



INSERT INTO countries (name, country_code) VALUES ('Austria', 'AT');
INSERT INTO countries (name, country_code) VALUES ('Belgium', 'BE');
INSERT INTO countries (name, country_code) VALUES ('Bulgaria', 'BG');
INSERT INTO countries (name, country_code) VALUES ('Croatia', 'HR');
INSERT INTO countries (name, country_code) VALUES ('Cyprus', 'CY');
INSERT INTO countries (name, country_code) VALUES ('Czechia', 'CZ');
INSERT INTO countries (name, country_code) VALUES ('Denmark', 'DK');
INSERT INTO countries (name, country_code) VALUES ('Estonia', 'EE');
INSERT INTO countries (name, country_code) VALUES ('Finland', 'FI');
INSERT INTO countries (name, country_code) VALUES ('France', 'FR');
INSERT INTO countries (name, country_code) VALUES ('Germany', 'DE');
INSERT INTO countries (name, country_code) VALUES ('Greece', 'EL');
INSERT INTO countries (name, country_code) VALUES ('Hungary', 'HU');
INSERT INTO countries (name, country_code) VALUES ('Ireland', 'IE');
INSERT INTO countries (name, country_code) VALUES ('Italy', 'IT');
INSERT INTO countries (name, country_code) VALUES ('Latvia', 'LV');
INSERT INTO countries (name, country_code) VALUES ('Lithuania', 'LT');
INSERT INTO countries (name, country_code) VALUES ('Luxembourg', 'LU');
INSERT INTO countries (name, country_code) VALUES ('Malta', 'MT');
INSERT INTO countries (name, country_code) VALUES ('Netherlands', 'NL');
INSERT INTO countries (name, country_code) VALUES ('Poland', 'PL');
INSERT INTO countries (name, country_code) VALUES ('Portugal', 'PT');
INSERT INTO countries (name, country_code) VALUES ('Romania', 'RO');
INSERT INTO countries (name, country_code) VALUES ('Slovakia', 'SK');
INSERT INTO countries (name, country_code) VALUES ('Slovenia', 'SI');
INSERT INTO countries (name, country_code) VALUES ('Spain', 'ES');
INSERT INTO countries (name, country_code) VALUES ('Sweden', 'SE');
INSERT INTO countries (name, country_code) VALUES ('United Kingdom', 'UK');
INSERT INTO countries (name, country_code) VALUES ('Serbia', 'RS');


INSERT INTO festivals (name, country_id) VALUES ('Benicassim', 26);
INSERT INTO festivals (name, country_id) VALUES ('Exit Festival', 29);
INSERT INTO festivals (name, country_id) VALUES ('T In The Park', 28);
INSERT INTO festivals (name, country_id) VALUES ('Lollapalooza', 11);
INSERT INTO festivals (name, country_id) VALUES ('Tomorrowland', 2);
INSERT INTO festivals (name, country_id) VALUES ('Mad Cool Festival', 26);
INSERT INTO festivals (name, country_id) VALUES ('Primavera Sound', 26);
INSERT INTO festivals (name, country_id) VALUES ('Creamfields', 28);
INSERT INTO festivals (name, country_id) VALUES ('Rock am Ring', 11);
INSERT INTO festivals (name, country_id) VALUES ('Rock im Park', 11);
INSERT INTO festivals (name, country_id) VALUES ('Isle of Wight Festival', 28);
INSERT INTO festivals (name, country_id) VALUES ('Ultra Europe', 4);
INSERT INTO festivals (name, country_id) VALUES ('Sziget Festival', 13);
INSERT INTO festivals (name, country_id) VALUES ('Let It Roll', 6);
INSERT INTO festivals (name, country_id) VALUES ('Wireless Festival', 28);
INSERT INTO festivals (name, country_id) VALUES ('Roskilde', 7);
INSERT INTO festivals (name, country_id) VALUES ('Leeds Festival', 28);
INSERT INTO festivals (name, country_id) VALUES ('Reading Festival', 28);
INSERT INTO festivals (name, country_id) VALUES ('Mad Cool Festival', 26);
INSERT INTO festivals (name, country_id) VALUES ('Download Festival', 28);
INSERT INTO festivals (name, country_id) VALUES ('Parklife', 28);
INSERT INTO festivals (name, country_id) VALUES ('Awakenings Festival', 7);
INSERT INTO festivals (name, country_id) VALUES ('Glastonbury Festival', 28);
INSERT INTO festivals (name, country_id) VALUES ('TRNSMT', 28);
INSERT INTO festivals (name, country_id) VALUES ('Super Bock Super Rock', 22);
INSERT INTO festivals (name, country_id) VALUES ('Hellfest Open Air', 10);
INSERT INTO festivals (name, country_id) VALUES ('Rolling Loud', 10);
INSERT INTO festivals (name, country_id) VALUES ('Time Warp DE', 11);
INSERT INTO festivals (name, country_id) VALUES ('Rock en Seine', 10);
INSERT INTO festivals (name, country_id) VALUES ('Afro Nation', 10);
INSERT INTO festivals (name, country_id) VALUES ('Rock in Rio Lisboa', 11);
INSERT INTO festivals (name, country_id) VALUES ('Bilbao BBK Live', 26);
INSERT INTO festivals (name, country_id) VALUES ('Lollapalooza Paris', 10);
INSERT INTO festivals (name, country_id) VALUES ('NOS Alive', 22);
INSERT INTO festivals (name, country_id) VALUES ('Rock Werchter', 2);
INSERT INTO festivals (name, country_id) VALUES ('Rock for People', 6);
INSERT INTO festivals (name, country_id) VALUES ('Lowlands Festival', 20);
INSERT INTO festivals (name, country_id) VALUES ('Azkena Rock Festival', 26);
INSERT INTO festivals (name, country_id) VALUES ('Lollapalooza Berlin', 11);
INSERT INTO festivals (name, country_id) VALUES ('Lollapalooza Sweden', 27);
INSERT INTO festivals (name, country_id) VALUES ('UNTOLD Festival', 23);
INSERT INTO festivals (name, country_id) VALUES ('Wacken Open Air', 11);
INSERT INTO festivals (name, country_id) VALUES ('Bospop', 20);
INSERT INTO festivals (name, country_id) VALUES ('Opener Festival', 21);
INSERT INTO festivals (name, country_id) VALUES ('Les Ardentes', 2);
INSERT INTO festivals (name, country_id) VALUES ('Kappa FuturFestival', 15);


INSERT INTO users (first_name, last_name, age) VALUES ('Mark', 'Burns', 33);
INSERT INTO users (first_name, last_name, age) VALUES ('Alex', 'Rabisse', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Andrew', 'Hunter', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Brian', 'Bell', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Chris', 'Dryden', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('David', 'Taylor', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Harrison', 'Booth', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('James', 'Beedle', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Jan', 'Metelski', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Jenny', 'Bulford', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Katie', 'Jeffree', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Malcolm', 'Holwill', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Nicola', 'Simpson', 30);
INSERT INTO users (first_name, last_name, age) VALUES ('Simon', 'Elsmie', 30);