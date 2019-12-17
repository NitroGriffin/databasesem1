CREATE TABLE tariff
( id_tarif integer PRIMARY KEY NOT NULL,
 nameOfTariff character(35) NOT NULL,
 cost money NOT NULL
);

CREATE TABLE tariff_description(
  id_tariff integer NOT NULL,
  FOREIGN KEY (id_tariff) REFERENCES tariff (id_tarif),
  description TEXT NOT NULL,
  mins integer NOT NULL,
  internet_mb integer NOT NULL,
  sms integer NOT NULL,
  mms integer NOT NULL
);

CREATE TABLE post_status(
id_post integer PRIMARY KEY NOT NULL,
CATEGORY VARCHAR(35) NOT NULL);

CREATE TABLE employee(
  id_emp integer PRIMARY KEY NOT NULL,
  sur_name varchar(40) NOT NULL,
  id_post integer NOT NULL,
  FOREIGN KEY (id_post) REFERENCES post_status (id_post)
);


CREATE TABLE client(
  id_client integer PRIMARY KEY NOT NULL,
  surname varchar(40) NOT NULL,
  num_of_pass varchar(15) NOT NULL,
  who_gives varchar(35) NOT NULL
);

CREATE TABLE typeOf(
  id_type integer PRIMARY KEY NOT NULL,
  type varchar(35) NOT NULL
);

CREATE TABLE orders(
  id_client integer NOT NULL,
  id_type integer NOT NULL,
  FOREIGN KEY (id_client) REFERENCES client(id_client),
  FOREIGN KEY (id_type) REFERENCES typeOf(id_type)
);

*
CREATE TABLE contract(
  id_contract integer PRIMARY KEY NOT NULL,
  id_tarif integer NOT NULL,
  num_of_tel varchar(35) NOT NULL,
  dat date not null,
  id_client integer NOT NULL,
  id_emp integer NOT NULL,
  FOREIGN KEY(id_tarif) REFERENCES tariff(id_tarif),
  FOREIGN KEY (id_client) REFERENCES client(id_client),
  FOREIGN KEY (id_emp) REFERENCES employee(id_emp)
);

CREATE TABLE status_payment(
  id_payment integer PRIMARY KEY NOT NULL,
  id_contract integer NOT NULL,
  money money NOT NULL,
  last_date date NOT NULL,
  FOREIGN KEY (id_contract) REFERENCES contract (id_contract)
);