#Username Prompt
usr = input ('username: ')
#Stores the username as a variable
username = usr
#Prompts password
passwrd = input
#Encrypts password
key = Fernet.generate_key()
encryption_type = Fernet(key)
encrypted_message = encryption_type.encrypt(b + usrname)
print(encrypted_message)
