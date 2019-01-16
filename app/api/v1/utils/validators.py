# This class contains functions for data validation
import re
# Python Regular Expression - the functions in this module let you check if a particular string matches a given 
# regular expression (or if a given regular expression matches a particular string, 
# which comes down to the same thing).
# https://docs.python.org/2/library/re.html


"""
Borrowed by self from Code Review Questions - Cycle 36, Question 3

Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
At least 1 letter between [a-z]
At least 1 number between [0-9]
At least 1 letter between [A-Z]
At least 1 character from [$#@]
Minimum length of transaction password: 6
Maximum length of transaction password: 12

Author: Charles M. Njenga

"""

class Validators():
    

    def is_valid_username(self, username):
        #check that the username is a string
        if not isinstance(username,str):
            return False
        elif len(username) < 3:
            # A valid username should have at least 3 characters
            return False
        else:
            return True

    def is_valid_password(self, password):
        password = str(password) # convert input to string to avoid TypeError: object of type 'int' has no len()
        try:            
            if len(password) <6:
                # return "Password should have a minimum of 6 characters", False
                return False
            elif len(password) > 12:
                # message = ("Not valid ! Password Should have maximum of 12 characters")
                return False
            elif re.search(r"\s",password): # \s matches any whitespace character
                # message =  ("Not valid ! It should not contain any spaces")
                return False
            elif not re.search(r"[a-z]",password): #[a-z] will match any lowercase ASCII letter,
                # message =  ("Not valid ! It should contain one lowercase letter between [a-z]")
                return False
            elif not re.search(r"[0-9]",password): # matches any decimal digit
                # message =  ("Not valid ! It should contain at least one number between [0-9]")
                return False
            elif not re.search(r"[A-Z]",password): #[a-z] will match any uppercase ASCII letter,
                # message =  ("Not valid ! It should contain one uppercase letter [a-z]")
                return False
        # elif not re.search("[$#@]",password): # re.search(pattern, string) - search occurence of pattern in string
        #   # message =  ("Not valid ! It should contain at least one of the following special characters [$ # @ ]")
        #   return False
            else:
                # Message: "Password meets the requirements"
                return True

        except Exception as e:
            raise e


    def is_valid_email(self, email):
        if not re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I):
            # Message: "Invalid email address"
            return False
            # abort(400, Message)
        else:
            return True