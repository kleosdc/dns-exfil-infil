import pyshark, base64, base58

#################
# Basic         #
# Decoder       #
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

# Path to .pcap file
file_cap = input('File captured: ')

# File output
FILE_OUTPUT = input('Filename output: ')

# Domain Name
DOMAIN_NAME = ''
while DOMAIN_NAME == '':
	DOMAIN_NAME = input('Domain Name (Example: badbaddoma.in): ')
print(f'[+] Domain Name set to {DOMAIN_NAME}')

cap = pyshark.FileCapture(file_cap, keep_packets=False)
des = []

# Filtering for user's domain name from user's .pcap file
print('[+] Filtering for your domain name.')
def print_cap(packet):
	try:
		if packet.dns.qry_name.split('.')[1] == DOMAIN_NAME.split('.')[0]:
			if packet.dns.qry_name.split('.')[0] not in des:
				des.append(packet.dns.qry_name.split('.')[0])
	except AttributeError:
		pass

cap.apply_on_packets(print_cap)

# Removing added 'Encryptor' from packety.py
decText = ''
for qry in des:
	decText += qry[1:-2]

# Writing result to user's output file
with open(FILE_OUTPUT, 'w') as wr:
	wr.write(Base64Decoder(Base58Decoder(decText)))
print(f'[+] Output to {FILE_OUTPUT}')
