import pyshark, base64, base58

#################
# Basic         #
# Decoder       #
#################

def Base58Decoder(text):
	return base58.b58decode(text)

def Base64Decoder(text):
	#base64_bytes = text.encode('ascii')
  
	sample_string_bytes = base64.b64decode(text) 
	sample_string = sample_string_bytes.decode('ascii')

	return sample_string

file_cap = input('File captured: ')

cap = pyshark.FileCapture(file_cap, keep_packets=False)
des = []

def print_cap(packet):
	try:
		if packet.dns.qry_name.split('.')[1] == 'badbaddoma':
			if packet.dns.qry_name.split('.')[0] not in des:
				des.append(packet.dns.qry_name.split('.')[0])
	except AttributeError:
		pass


cap.apply_on_packets(print_cap)

decText = ''
for qry in des:
	decText += qry[1:-2]

print(decText, '\n', Base64Decoder(Base58Decoder(decText)))
