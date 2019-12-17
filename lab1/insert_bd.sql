--НАПОЛНЕНИЕ таблицы с client
INSERT INTO client VALUES (1, 'volodymyr', '4212', 'KievskiyRayon');
INSERT INTO client VALUES (2, 'petyaKarm', '1523', 'HarkovRaron');
INSERT INTO client VALUES (3, 'antonTibur', '1231', 'ObolonskiyRayon');
INSERT INTO client VALUES (4, 'mishaHavchenko', '4123', 'ShevchenkovskiyRayon');
--ПРОВЕРКА(ВСЕ ОК)
select * from client


--НАПОЛНЕНИЕ таблицы с typeOF
INSERT INTO typeof VALUES (1, 'Месячный');
INSERT INTO typeof VALUES (2, 'Годовый');
 --ПРОВЕРКА
select * from typeof


--НАПОЛНЕНИЕ таблицы с orders
INSERT INTO orders VALUES (1, 1);
INSERT INTO orders VALUES (1, 2);
INSERT INTO orders VALUES (2, 1);
INSERT INTO orders VALUES (3, 1);
INSERT INTO orders VALUES (3, 1);
INSERT INTO orders VALUES (3, 2);
INSERT INTO orders VALUES (4, 2);
 --ПРОВЕРКА
select * from orders


--НАПОЛНЕНИЕ таблицы с employee
INSERT INTO employee VALUES (1, 'DmitriyVolokov',1);
INSERT INTO employee VALUES (2, 'JimmyTrump',2);
INSERT INTO employee VALUES (3, 'AdamSok',1);
INSERT INTO employee VALUES (4, 'OlegBrams',3);
INSERT INTO employee VALUES (5, 'SergiyDobriy',1);
INSERT INTO employee VALUES (6, 'Ajaja',2);
INSERT INTO employee VALUES (7, 'MaksimNavr',1);
 --ПРОВЕРКА
select * from employee



--НАПОЛНЕНИЕ таблицы с post_status
INSERT INTO post_status VALUES (1, 'manager');
INSERT INTO post_status VALUES (2, 'clean_washer');
INSERT INTO post_status VALUES (3, 'CEO');

 --ПРОВЕРКА
select * from post_status;



--НАПОЛНЕНИЕ таблицы с tariff
INSERT INTO tariff VALUES (1, 'Maximum',800);
INSERT INTO tariff VALUES (2, 'Minimum',100);

select * from tariff



--НАПОЛНЕНИЕ таблицы с tariff_description
INSERT INTO tariff_description VALUES (1, 'Повний пакет на всі двізнки мобльні інтернет та інше',1000,25000,300,150);
INSERT INTO tariff_description VALUES (2, 'Мінімум всього необхідного',300,1000,10,5);

 --ПРОВЕРКА
select * from tariff_description


-- --НАПОЛНЕНИЕ таблицы с contract
INSERT INTO contract VALUES (1,1,'+38066123412','2019-12-15',1,1);
INSERT INTO contract VALUES (2,1,'+38066123112','2019-11-12',1,1);
INSERT INTO contract VALUES (3,2,'+38096124312','2019-12-27',2,3);
INSERT INTO contract VALUES (4,2,'+38099123455','2019-09-23',3,1);
INSERT INTO contract VALUES (5,1,'+38067123419','2019-10-14',1,4);
INSERT INTO contract VALUES (6,2,'+38066152412','2019-02-05',2,3);


--  --ПРОВЕРКА
select * from contract



-- --НАПОЛНЕНИЕ таблицы с status_payment
INSERT INTO status_payment VALUES (1,1,100,'2019-12-15');
INSERT INTO status_payment VALUES (2,1,100,'2019-11-15');
INSERT INTO status_payment VALUES (3,2,800,'2019-10-25');
INSERT INTO status_payment VALUES (4,2,800,'2019-09-25');



--  --ПРОВЕРКА
select * from status_payment
