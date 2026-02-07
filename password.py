#password_checker accepts a password as a parameter

def password_checker(password):

    total = 0
    #We check if the length matches the 8 requirement - if not, return false
    if (len(password)!=8):
        return False
    
    #We check if the password is all numbers/characters via python's built in isalnum function
    if password.isalnum()==False:
        return False
    
    #first and second take on the values of password's first two characters
    first = password[0]
    second = password[1]

    #We check if both first characters are uppercase - if not, we return false
    if (first.isupper() and second.isupper())==False:
        return False
    #we check if the two uppercase characters are equivalent. If so, we return false
    elif first==second:
        return False
    
    #We go through the characters of password and attempt to add them to total as an integer.
    #If an error happens in the case of a non-int character, the for loop continues.
    for i in password:
        try:
            total+=int(i)
        except ValueError:
            pass
    
    #Using the sum of the numbers in password via total, we check if it's even. If not, it returns false
    if (total%2 != 0):
        return False
    
    #in all successful scenarios, it returns a true value
    return True

print(password_checker("AU264bNm"))