import Connect
import random
from View import View
from datetime import datetime, date, time


#Dictionary with DB table names and them identifiers
tables = {
    1: 'client',
    2: 'contract',
    3: 'employee',
    4: 'orders',
    5: 'post_status',
    6: 'status_payment',
    7: 'tariff',
    8: 'tariff_description',
    9: 'typeof',
}
class Model:
    # Method that checks valid of the number of table that user input and returns it
    @staticmethod
    def validTable():
        incorrect = True
        while incorrect:
            table = input('Choose table number => ')
            if table.isdigit():
                table = int(table)
                if table >= 1 and table <= 9:
                    incorrect = False
                else:
                    print('Incorrect input, try again.')
            else:
                print('Incorrect input, try again.')
        return table

    #Method that prints all table of DB
    @staticmethod
    def showAllTables():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        for table in range(1,10):
            table_name = '''"''' + tables[table] + '''"'''
            print(tables[table])

            show = 'select * from public.{}'.format(table_name)

            print("SQL query => ", show)
            cursor.execute(show)
            records = cursor.fetchall()
            obj = View(table, records)
            obj.show()
        cursor.close()
        Connect.closeConnect(connect)

    #Method that prints one table
    @staticmethod
    def showOneTable():
        View.list()
        connect = Connect.makeConnect()
        cursor = connect.cursor()

        table = Model.validTable()

        table_name = '''"''' + tables[table] + '''"'''
        print(tables[table])

        show = 'select * from public.{}'.format(table_name)

        print("SQL query => ", show)
        print('')
        cursor.execute(show)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        cursor.close()
        Connect.closeConnect(connect)

#-----------TASK 1----------Inserting data into DB

    #Method that inserts data into DB
    @staticmethod
    def insert():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                id_client = input("ID = ")
                surname = "'" + input('surname = ') + "'"
                num_of_pass = "'" + input('num_of_pass = ') + "'" 
                who_gives = "'" + input('who_gives = ') +"'"

                insert = 'insert into "client" ("id_client","surname", "num_of_pass", "who_gives") values ({}, {}, {},{})'.format(id_client,surname, num_of_pass, who_gives)

                restart = False
            elif table == 2:
                id_contract = input('id_contract = ')
                id_tarif = input ('id_tarif = ') 
                num_of_tel = "'" + input ('num_of_tel = ') + "'"
                dat = "'" + input('dat = ') +"'"
                id_client = input('id_client = ')
                id_emp = input('id_emp = ')

                insert = 'insert into "contract" ("id_contract", "id_tarif", "num_of_tel", "dat", "id_client", "id_emp") values ({}, {}, {}, {}, {}, {})'.format(id_contract, id_tarif, num_of_tel, dat , id_client, id_emp)

                restart = False
            elif table == 3:
                id_emp = input('id_emp = ')
                sur_name = "'" + input('sur_name = ') + "'"
                id_post = input('id_post = ')

                insert = 'insert into "employee" ("id_emp", "sur_name", "id_post") values ({}, {}, {})'.format(id_emp, sur_name, id_post)

                restart = False
            elif table == 4:
                id_client = input('id_client = ')
                id_type = input('id_type = ')

                insert = 'insert into "orders" ("id_client", "id_type") values ({}, {})'.format(id_client, id_type)

                restart = False
            elif table == 5:
                id_post = input('id_post = ')
                category = "'" + input('category = ') + "'"

                insert = 'insert into "post_status" ("id_post", "category") values ({}, {})'.format(id_post, category)

                restart = False
            elif table == 6:
                id_payment = input('id_payment = ')
                id_contract =input('id_contract = ')
                money = input("money = ")
                last_date ="'" + input("last_date = ")+ "'"

                insert = 'insert into "status_payment" ("id_payment", "id_contract","money","last_date") values ({}, {},{},{})'.format(id_payment, id_contract,money,last_date)

                restart = False
            elif table == 7:
                id_tarif = input('id_tarif = ')
                nameoftariff = "'" + input('nameOfTarif = ') + "'"
                cost =input('cost = ')


                insert = 'insert into "tariff" ("id_tarif", "nameoftariff", "cost") values ({}, {}, {})'.format(id_tarif, nameoftariff, cost)

                restart = False
            elif table == 8:
                id_tariff = input('id_tariff = ')
                description = "'" + input('description = ') + "'"
                mins = input("mins = ")
                internet_mb = input("internet_mb = ")
                sms = input("sms = ")
                mms = input("mms = ")

                insert = 'insert into "tariff_description" ("id_tariff", "description", "mins","internet_mb","sms","mms") values ({}, {}, {},{},{},{})'.format(id_tariff, description, mins, internet_mb, sms, mms)
                restart = False
                
            elif table == 9:
                id_type = input('id_type = ')
                type = "'" + input('type = ') + "'"
                insert = 'insert into "typeof" ("id_type", "type") values ({}, {})'.format(id_type, type)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print('SQl query => ',insert)
        cursor.execute(insert)
        connect.commit()
        print('Data added successfully!')
        cursor.close()
        Connect.closeConnect(connect)

    # ----------TASK 1----------Deleting data from DB

    #Method that deletes data from DB
    @staticmethod
    def delete():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()

            if table == 1:
                clname = "'" + input('Attribute to delete surname = ') + "'"
                delete = 'delete from "client" where "surname"= {}'.format(clname)
                restart = False
            elif table == 2:
                id_contract = "'" + input('Attribute to delete id_contract = ') + "'"
                delete = 'delete from "contract" where "id_contract"=  {}'.format(id_contract)
                restart = False
            elif table == 3:
                dsname = "'" + input('Attribute to delete sur_name = ') + "'"
                delete = 'delete from "employee" where "sur_name"= {}'.format(dsname)
                restart = False
            elif table == 4:
                incorderid = input('Attribute to delete id_client = ')
                delete = 'delete from "orders" where "id_client"= {}'.format(incorderid)
                restart = False
            elif table == 5:
                orid = input('Attribute to delete id_post = ')
                delete = 'delete from "post_status" where "id_post"=  {}'.format(orid)
                restart = False
            elif table == 6:
                psnumber = "'" + input('Attribute to delete id_payment = ') + "'"
                delete = 'delete from "status_payment" where "id_payment"=  {}'.format(psnumber)
                restart = False
            elif table == 7:
                rsname = "'" + input('Attribute to delete nameOfTarif = ') + "'"
                delete = 'delete from "tariff" where "nameoftariff"= {}'.format(rsname)
                restart = False
            elif table == 8:
                trname = "'" + input('Attribute to delete id_tariff = ') + "'"
                delete = 'delete from "tariff_description" where "id_tariff"= {}'.format(trname)
                restart = False
            elif table == 9:
                trname1 = "'" + input('Attribute to delete id_type = ') + "'"
                delete = 'delete from "typeof" where "id_type"= {}'.format(trname1)
                restart = False
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", delete)
        cursor.execute(delete)
        connect.commit()
        print('Data deleted successfully!')
        cursor.close()
        Connect.closeConnect(connect)

#----------TASK 1----------Updating data in DB

    #Method that updates data in DB
    @staticmethod
    def update():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            if table == 1:
                clname = "'" + input('Attribute to update(where) surname = ') + "'"
                View.attribute_list(1)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_client"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"surname"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"num_of_pass"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"who_gives"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "client" set {} where "surname"= {}'.format(set, clname)
                restart = False
                pass
            elif table == 2:
                crname = input('Attribute to update(where) id_contract = ')
                View.attribute_list(2)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_conract"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_tarif"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"num_of_tel"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"dat"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"id_client"= {}'.format(value)
                        in_restart = False
                    elif num == '6':
                        set = '"id_emp"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "contract" set {} where "id_contract"= {}'.format(set, crname)
                restart = False
                pass
            elif table == 3:
                dsname = "'" + input('Attribute to update(where) sur_name = ') + "'"
                View.attribute_list(3)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_emp"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"sur_name"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"id_post"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "employee" set {} where "sur_name"= {}'.format(set, dsname)
                restart = False
                pass
            elif table == 4:
                incorderid = input('Attribute to update(where) id_client = ')
                View.attribute_list(4)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_client"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_type"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "orders" set {} where "id_client"= {}'.format(set, incorderid)
                restart = False
                pass
            elif table == 5:
                incorderid = input('Attribute to update(where) id_post = ')
                View.attribute_list(5)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_post"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"category"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "post_status" set {} where "id_post"= {}'.format(set, incorderid)
                restart = False
                pass
            elif table == 6:
                orid = input('Attribute to update(where) id_payment= ')
                View.attribute_list(6)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_payment"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"id_contract"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"money"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"last_date"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "status_payment" set {} where "id_payment"= {}'.format(set, orid)
                restart = False
                pass
            elif table == 7:
                psnumber = "'" + input('Attribute to update(where) id_tariff = ') + "'"
                View.attribute_list(7)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_tariff"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"nameoftariff"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"cost"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "tariff" set {} where "id_tarif"= {}'.format(set, psnumber)
                restart = False
                pass
            elif table == 8:
                rsname = "'" + input('Attribute to update(where) id_tariff = ') + "'"
                View.attribute_list(8)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_tariff"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"description"= {}'.format(value)
                        in_restart = False
                    elif num == '3':
                        set = '"mins"= {}'.format(value)
                        in_restart = False
                    elif num == '4':
                        set = '"internet_mb"= {}'.format(value)
                        in_restart = False
                    elif num == '5':
                        set = '"sms"= {}'.format(value)
                        in_restart = False
                    elif num == '6':
                        set = '"mms"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "tariff_description" set {} where "id_tariff"= {}'.format(set, rsname)
                restart = False
                pass
            elif table == 9:
                trname = "'" + input('Attribute to update(where) id_type = ') + "'"
                View.attribute_list(9)
                in_restart = True
                while in_restart:
                    num = input('Number of attribute =>')
                    value = "'" + input('New value of attribute = ') + "'"
                    if num == '1':
                        set = '"id_type"= {}'.format(value)
                        in_restart = False
                    elif num == '2':
                        set = '"type"= {}'.format(value)
                        in_restart = False
                    else:
                        print('\nIncorrect input, try again.')
                update = 'update "typeof" set {} where "id_type"= {}'.format(set, trname)
                restart = False
                pass
            else:
                print('\nIncorrect input, try again.')
        print(tables[table])
        print("SQL query => ", update)
        cursor.execute(update)
        connect.commit()
        print('Data updeted successfully!')
        cursor.close()
        Connect.closeConnect(connect)
        pass

#----------TASK 3----------

    #Method that seletes data from DB
    @staticmethod
    def select():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        print(''' out select based for client 
        ''')

        # ordateL = "'" + input('OrDate: Between ') + "'"
        # print('and')
        # ordateR = "'" + input() + "'"
        # ordelivered = input('OrDelivered: ')
        # rsalltime = input('RsAllTime: ')

        select = 'select * from "client"'

        print("SQL query => ", select)
        cursor.execute(select)
        records = cursor.fetchall()
        obj = View(1, records)
        obj.showSelect()

        print('Data selected successfully!')
        cursor.close()
        Connect.closeConnect(connect)

#----------TASK 4----------

    #Method that runs full text search in DB
    @staticmethod
    def text_search():
        connect = Connect.makeConnect()
        cursor = connect.cursor()
        restart = True
        while restart:
            View.list()
            table = Model.validTable()
            text = "'" + input('Search text = ') + "'"
            incorrect = True
            while incorrect:
                mode = input('''
                1 -- Word is not included
                2 -- Required word entry
                Choose mode = > ''')
                if mode.isdigit():
                    mode = int(mode)
                    if mode >= 1 and mode <= 2:
                        incorrect = False
                    else:
                        print('Incorrect input, try again.')
                else:
                    print('Incorrect input, try again.')

            if mode == 1:
                pass
            elif mode == 2:
                pass
            else:
                print('\nIncorrect input, try again.')

        print(tables[table])
        print('SQL query => ',text_search)
        cursor.execute(text_search)
        records = cursor.fetchall()
        obj = View(table, records)
        obj.show()
        print('Data searched successfully!')
        cursor.close()
        Connect.closeConnect(connect)


