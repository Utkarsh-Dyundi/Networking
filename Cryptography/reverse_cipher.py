#method to encrypt the given string
def encrypt(x,password):
	string=' abcdefghijklmnopqrstuvwxyz1234567890[](){}?!.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	n=len(password)																			
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
	password=translated
	for i in password:
		translated=''
		for c in range(0,len(x)):
			if x[c] in string:
				index=(string.find(x[c])+password.find(i)-c**2)%n2
				translated=translated+string[index]
			else:
				translated=translated+x[c]
		x=translated[::-1]
	return x

#method to decrypt the given string
def decrypt(y,password):
	string=' abcdefghijklmnopqrstuvwxyz1234567890[](){}?!.ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	n=len(string)
	n2=len(password)
	index=0
	translated=''
	for i in password:
		if i in string:
			translated=translated+string[(string.find(i)+n2)%n]
			n2=n2-1
		else:
			translated=translated+i
			n2=n2-1
	password=translated
	for i in password:
		y=y[::-1]
		translated=''
		for c in range(0,len(y)):
			if y[c] in string:
				index=(string.find(y[c])-password.find(i)+c**2)%n
				translated=translated+string[index]
			else:
				translated=translated+y[c]
		y=translated
	return y	
	
def main():
	x=input('type message:->\n')
	password=input('enter the password to encrypt:-> ')
	y_enc=encrypt(x,password)
	print('...encrypted...\n'+y_enc)
	password=input('\nenter the password to decrypt:-> ')
	y_dec=decrypt(y_enc,password)
	print('\n...decrypted...\n'+y_dec)
	
	
main()