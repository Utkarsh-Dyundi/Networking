file_name=input('enter the filename to decrypt:-> ')									#file to be encrypted
file_name2=input('enter the name of temporary file:-> ')								#file that will be created after decryption
file=open(file_name,'r')
file_content2=open(file_name2,'w')
password=input('enter the password:->')													#password for decryption of file


string=' abcdefghijklmnopqrstuvwxyz1234567890[](){}?!.ABCDEFGHIJKLMNOPQRSTUVWXYZ'		#string for indexing other characters
n=len(password)																			#used for creating randomness in result
n2=len(string)
index=0
translated=''
for i in password:
	if i in string:
		translated=translated+string[(string.find(i)+n)%n2]
		n=n-1
	else:
		translated=translated+i
		n=n-1
password=translated+password
print(password)
for file_content in file:
	x=file_content
	for i in password:
		translated=''
		x=x[::-1]
		for c in range(0,len(x)):
			if x[c] in string:
				index=(string.find(x[c])-password.find(i)+c**2)%n2
				translated=translated+string[index]
			else:
				translated=translated+x[c]
		x=translated
	file_content2.write(x)
file_content2.close()
file.close()
