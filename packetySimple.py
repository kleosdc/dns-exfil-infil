import os, base64, base58


#################
# Basic Encoder #
# and Decoder   #
#################

def Base58Decoder(text):
	return base58.b58decode(text)

def Base64Decoder(text):
	#base64_bytes = text.encode('ascii')
  
	sample_string_bytes = base64.b64decode(text) 
	sample_string = sample_string_bytes.decode('ascii')

	return sample_string

##################
# Read from file #
##################

def ReadFrom(file):
	try:
		with open(file, 'r') as r:
			return r.read()
	except FileNotFoundError:
		print(f'{file} was not found.')


# Get filname from user input
fileAt = input('Filename: ')


# All text from text file as plain text
encoded_text = ReadFrom(fileAt)
if encoded_text != None:
	decoded_code = Base64Decoder(Base58Decoder(encoded_text))

	with open(fileAt, 'w') as wr:
		wr.write(decoded_code)

print('DONE...running')
os.system(f'sleep 3; python3 {fileAt}')