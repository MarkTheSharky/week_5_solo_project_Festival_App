DROP TABLE IF EXISTS festivals;
DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS users_festivals;


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
    country_id INT REFERENCES countries(id)
);

CREATE TABLE users_festivals (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id),
    festival_id INT REFERENCES festivals(id)
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
INSERT INTO countries (name, country_code) VALUES ('Swedan', 'SE');
INSERT INTO countries (name, country_code) VALUES ('United Kingdom', 'UK');
INSERT INTO countries (name, country_code) VALUES ('Serbia', 'RS');

INSERT INTO festivals (name, country_id) VALUES ('Benicassim', 26);
INSERT INTO festivals (name, country_id) VALUES ('Exit Festival', 29);
INSERT INTO festivals (name, country_id) VALUES ('T In The Park', 28);
INSERT INTO festivals (name, country_id) VALUES ('Lollapalooza', 11);

INSERT INTO users (first_name, last_name, age) VALUES ('Mark', 'Burns', 33);
INSERT INTO users (first_name, last_name, age) VALUES ('Heather', 'MacSween', 33);
INSERT INTO users (first_name, last_name, age) VALUES ('Stewart', 'McGowan', 33);
INSERT INTO users (first_name, last_name, age) VALUES ('Matt', 'Mclister', 33);
INSERT INTO users (first_name, last_name, age) VALUES ('Kerr', 'McAndrew', 33);