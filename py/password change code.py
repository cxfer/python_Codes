#!/usr/bin/python3

password = ""
oldpasswd="wanjohi"

def set_password():
	oldpasswd1=input("enter old password: ")
	if oldpasswd==oldpasswd1:
		
		global password
		password = input("Enter your desired password: ")
		confirm_password = input("Confirm your password: ")
		if password == confirm_password:
			print("Password successfully set!")
		else:
			print("Passwords do not match. Please try again.")
			set_password()

set_password()




