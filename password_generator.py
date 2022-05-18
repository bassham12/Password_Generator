""" This project is a password generator that will take in data from the user and print out a randomly generated password
    the data that will be taken in are the number of:
        uppercase letters
        lowercase letters
        numeric characters
        special characters
"""





from operator import truediv
from pickle import FALSE, TRUE
import random
from unicodedata import digit
    

'''random_character function passes in three parameters:
    num_char being the number given by the user
    list_coordinated being the list that we want to append to
    start num which is the chosen starting number in the ascii table for each variable we recieve
        in example uppercase letters have a ascii starting number of 65
        where lowercase letters have a ascii starting number of 97
    
    random_character produces a for loop that will loop through the number of times that the user gave
    it will then generate a random integer between the start_num and the start_num + 24
    we then use chr to create a letter from the random integer given 
    we can then append that letter to the list that was passed in the parameters'''

def random_character(num_char, list_coordinated, start_num):
    for i in range(num_char):
        random_num = random.randint(start_num, (start_num + 24))
        letter = chr(random_num)
        list_coordinated.append(letter)


""" generate_password function gets the number of uppercase, lowercase, numeric, and special characters the user enters
    each has a while loop checking if the input is between 1 and 5
    generate_password calls the random_character function to recieve random letters into the designated lists
    we then have a for loop that will get the number of numeric values and set them to a random number 
    then pass it to the numeric_char list
    then for the special characters we randomize the index of the special_char list which contains some special characters
    then we store all the values of each list to the password list
    from there we can randomize values by going through each index and trading its values with a value of a random index
    final_password will set the values of password into a string
    and print the final_password
    
    we will ask the user if they like the new password
    if so it will print "Your new password: " then the final_password
    if they say no then generate_password will call itself
"""

def generate_pasword():
    num_uppers = int(input("Enter the number of uppercase letters you would like: \n"))

    while num_uppers <= 0 or num_uppers >= 6:
        num_uppers = int(input("Enter the number of uppercase letters you would like: \n"))
    else: 
        random_character(num_uppers, upperletters, 65)


    num_lowers = int(input("Enter the number of lowercase letters you would like: \n"))

    while num_lowers <= 0 or num_lowers >= 6:
        num_lowers = int(input("Enter the number of lowercase letters you would like: \n"))
    else:
        random_character(num_lowers, lowerletters, 97)

    num_numerical_char = int(input("Enter the number of numerical characters you would like: \n"))

    while num_numerical_char <= 0 or num_numerical_char >= 6:
        num_numerical_char = int(input("Enter the number of numerical characters you would like: \n"))
    else:
        for i in range(num_numerical_char):
            random_num = random.randint(0, 9)
            numerical_char.append(random_num)

    num_special_char = int(input("Enter number of special characters you would like: \n"))

    while num_special_char <= 0 or num_special_char >= 6:
        num_special_char = int(input("Enter number of special characters you would like: \n"))
    else:
        for i in range(num_special_char):
            letter = random.choice(special_char)
            password.append(letter)

    password.extend(upperletters + lowerletters + numerical_char)

    temp_val = 0

    for i in range(len(password)):
        last_index = len(password) - 1
        random_index = random.randint(0, last_index)
        temp_val = password[i]
        password[i] = password[random_index]
        password[random_index] = temp_val

    final_password = ""

    for i in range(len(password)):
        final_password = final_password + str(password[i])

    print()
    print(f"New Password: {final_password}") 
    print("Do you like your new password?")   
    
    acceptance = input("Enter Y or N: \n")

    if acceptance == "Y" or acceptance == "y":
        print(f"Your new password: {final_password}")
    else: 
        generate_pasword()
    




upperletters = []
lowerletters = []
numerical_char = []
special_char = ["!","@","#","$","%","^","&","*","?"]
password = []
final_password = ""

generate_pasword()



  



