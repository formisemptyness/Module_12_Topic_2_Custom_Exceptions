'''
Program: customer_exceptions.py
Author: Joshua M. McGinley
Last date modified: 11/16/2022


From Module10, copy your Customer class updated with any instructor feedback and remove the address attribute.
Place the code in Module12 project package custom_exceptions, file customer_exceptions.py. Include your directory
for test_custom_exceptions and test_customer_exceptions.py
Make exception for the following attributes:

    customer_id -a number between 1000-9999,  InvalidCustomerIdException
    last_name - alpha characters, InvalidNameException
    first_name -alpha characters, InvalidNameException
    phone_number - 123-123-1234 format, InvalidPhoneNumberFormat

Include driver code that tests the exceptions with try/except

    include calls for
        constructor with invalid customer_id
        constructor with invalid last_name
        constructor with invalid first_name
        constructor with invalid phone_number
        str()

Include unit test to test the code

    setUp()
    tearDown()
    constructor with valid customer_id
    constructor with valid last_name
    constructor with valid first_name
    constructor with valid phone_numbe
    constructor with invalid customer_id
    constructor with invalid last_name
    constructor with invalid first_name
    constructor with invalid phone_number
    str() test(s)
'''

class Customer:
    """Customer class"""

    def __init__(self, cid, lname, fname, pnumber, addy):  # Constructor sets all to no value
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        customer_id_characters = set("1234567890")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        if not phone_number_characters.issuperset(pnumber):
            raise InvalidPhoneNumberFormat
        if not customer_id_characters.issuperset(cid):
            raise InvalidCustomerIdException
        self.customer_id = cid
        self.last_name = lname
        self.first_name = fname
        self.phone_number = pnumber
        self.address = addy

    def __str__(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)

    def change_last_name(self, name):
        self.last_name = name

    def change_first_name(self, name):
        self.first_name = name

    def change_phone_number(self, number):
        self.phone_number = number

    def change_address(self, addy):
        self.address = addy

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

class InvalidCustomerIdException(Exception):
    """InvalidCustomerIdException is derived class of Exception base class"""
    pass

class InvalidNameException(Exception):
    """InvalidNameException is derived class of Exception base class"""
    pass

class InvalidPhoneNumberFormat(Exception):
    """InvalidPhoneNumberFormat is derived class of Exception base class"""
    pass

#Driver code
if __name__== "__main__":
# Valid customer
    customer_one = Customer('123', 'Duck', 'Donald', '(555)555-5555', '123 main street') # all required
    print(str(customer_one))

#Invalid phone
# Wait! try/except needed!
    try:
        customer_two = Customer('123', 'Duck', 'Donald', '(555)555-5555p', '123 main street') # all required
        print(str(customer_two))
    except InvalidPhoneNumberFormat:
        print("Error found, customer not created")


# Invalid customer_id
# try/except needed
    try:
        customer_two = Customer('ABC', 'Duck', 'Donald', '(555)555-5555', '123 main street') # all required
    except InvalidCustomerIdException:
        print("Error found, customer not created")

# Invalid first_name
# try/except needed!
    try:
        customer_two = Customer('123', 'Duck', '2', '(555)555-5555', '123 main street') # all required
    except InvalidNameException:
        print("Error found, customer not created")

# Invalid last_name
# try/except needed!
    try:
        customer_two = Customer('123', '_uck', 'Donald', '(555)555-5555', '123 main street') # all required
    except InvalidNameException:
        print("Error found, customer not created")
