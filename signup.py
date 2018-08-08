import re

class SignUp(object):
   """
   the following class is an example of modeling a signup form
   of a website using object oriented concepts.

   """
   def __init__(self, first_name, last_name, email_address):
       self.first_name = first_name
       self.last_name = last_name
       self.email_address = SignUp.validate_email(email_address)
          
   def combined_name(self, first_name, last_name):
       # Combines first and last name into a single name
       full_names = self.first_name + " " + self.last_name
       return full_names

   @staticmethod
   def validate_email(email_address):
       if re.match(re.compile(r'^.+@[^.].*\.[a-z]{2,10}$', flags=re.IGNORECASE), email_address):
           return email_address

class Rider(SignUp):
    def __init__(self, first_name, last_name, email_address, phone_number):
        super().__init__(first_name, last_name, email_address, phone_number)

class Driver(SignUp):
    def __init__(self, first_name, last_name, email_address, phone_number,  vehicle, number_plate):
        super().__init__(first_name, last_name, email_address, phone_number)
        self.vehicle = vehicle
        self.number_plate = number_plate

