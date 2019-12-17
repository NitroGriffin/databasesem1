class View:

    #Initialization of class View
    def __init__(self, table, records):
        self.table = table
        self.records = records

    #Method that prints the list of DB tables
    @staticmethod
    def list():
        print('''
        1 => client
        2 => contract
        3 => employee
        4 => orders
        5 => post_status
        6 => status_payment
        7 => tariff
        8 => tariff_description
        9 => typeof
        ''')

    #Method that prints the list of attributes of the selected table
    @staticmethod
    def attribute_list(table):
        if table == 1:
            print('''
            1 => id_client
            2 => surname
            3 => numb_of_pass
            4 => who_gives
            ''')
        elif table == 2:
            print('''
            1 => id_contact
            2 => id_tarif
            3 => num_of_tel
            4 => dat
            5 => id_client
            6 => id_emp
            ''')
        elif table == 3:
            print('''
            1 => id_emp
            2 => sur_name
            3 => id_post
            ''')
        elif table == 4:
            print('''
            1 => id_client
            2 => id_type
            ''')
        elif table == 5:
            print('''
            1 => id_post
            2 => category
            ''')
        elif table == 6:
            print('''
            1 => id_payment
            2 => id_contract
            3 => money
            4 => last_date
            ''')
        elif table == 7:
            print('''
            1 => id_tarif
            2 => nameoftariff
            3 => cost
            ''')
        elif table == 8:
            print('''
            1 => id_tariff
            2 => description
            3 => mins
            4 => internet_mb
            5 => sms
            6 => mms
            ''')
        elif table == 9:
            print('''
            1 => id_type
            2 => type
            ''')
    #Method that prints content from a selected table
    def show(self):
        print("____________________\n")
        if self.table == 1:
            for row in self.records:
                print("id_client = ", row[0])
                print("surname = ", row[1])
                print("numb_of_pass = ", row[2])
                print("who_gives = ", row[3])
                print("____________________\n")
        elif self.table == 2:
            for row in self.records:
                print("id_contract = ", row[0])
                print("id_tarif = ", row[1])
                print("num_of_tel = ", row[2])
                print("date = ", row[3])
                print("id_client = ", row[4])
                print("id_emp = ", row[5])
                print("____________________\n")
        elif self.table == 3:
            for row in self.records:
                print("id_emp = ", row[0])
                print("surName = ", row[1])
                print("id_post = ", row[2])
                print("____________________\n")
        elif self.table == 4:
            for row in self.records:
                print("id_client = ", row[0])
                print("id_type = ", row[1])

                print("____________________\n")
        elif self.table == 5:
            for row in self.records:
                print("id_post = ", row[0])
                print("category = ", row[1])
                print("____________________\n")
        elif self.table == 6:
            for row in self.records:
                print("id_payment = ", row[0])
                print("id_contract = ", row[1])
                print("money = ", row[2])
                print("last_date = ", row[3])
                print("____________________\n")
        elif self.table == 7:
            for row in self.records:
                print("id_tarif = ", row[0])
                print("nameOfTarif= ", row[1])
                print("cost = ", row[2])
                print("____________________\n")
        elif self.table == 8:
            for row in self.records:
                print("id_tarif = ", row[0])
                print("description = ", row[1])
                print("mins = ", row[2])
                print("internet_mb = ", row[3])
                print("sms = ", row[4])
                print("mms = ", row[5])
                print("____________________\n")
        elif self.table == 9:
            for row in self.records:
                print("id_type = ", row[0])
                print("type = ", row[1])
                print("____________________\n")

    #Method that prints the result of select query
    def showSelect(self):
        for row in self.records:
            print("id_client = ", row[0])
            print("surname= ", row[1])
            print("numb_of_pass = ", row[2])
            print("numb_of_pass = ", row[3])
            print("____________________\n")
