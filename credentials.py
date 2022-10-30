import requests
import re

# define required parameters.
regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


while True:
	#ask mail
	mail = input("Enter your mail: \n")
	if (re.search(regex, mail)):
		break
	else:
		print("Invalid email. Enter again.")

while True:
	phone = input("Enter your phone number: \n")
	for no in phone:
		if len(phone) > 10 or len(phone) < 10: 
			if no not in num:
				print("Invalid number. Try again")
	else:
		break


#	WEBSITE



 #CREATE VIRTUAL ENVIRONMENT- PROJECTENV
 # JUST CREATE A NEW FILE IN THE SAME DIRECTORY AS VENV.