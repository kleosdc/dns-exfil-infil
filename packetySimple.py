import os, base64, base58


#################
# Basic Encoder #
# and Decoder   #
#################

def Base58Decoder(text):
	print('[+] Base58 decoded.')
	return base58.b58decode(text)

def Base64Decoder(text):
	#base64_bytes = text.encode('ascii')
  
	sample_string_bytes = base64.b64decode(text) 
	sample_string = sample_string_bytes.decode('ascii')

	print('[+] Base64 decoded.')
	return sample_string

##################
# Read from file #
##################

def ReadFrom(file):
	try:
		with open(file, 'r') as r:
			print('[+] Reading from file...')
			return r.read()
	except FileNotFoundError:
		print(f'{file} was not found.')


# Get filname from user input
fileAt = input('Filename: ')

# Decodes the data from the file provided by the user
encoded_text = ReadFrom(fileAt)
if encoded_text != None:
	decoded_code = Base64Decoder(Base58Decoder(encoded_text))

	with open(fileAt, 'w') as wr:
		wr.write(decoded_code)
print(f'[+] Done, {fileAt} is decoded.')
