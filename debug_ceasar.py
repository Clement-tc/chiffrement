import string

def cesar_ciffer(message, key):
	
	if type(key) != int :
		print("la clef doit être un entier")
		return None

	message = str(message)

	list_of_crypted_caracs = []
	for carac in message:
		crypted_index = (string.printable.index(carac) + key) % len(string.printable)
		crypted_carac = string.printable[crypted_index]
		if(crypted_carac=='\r'):
			crypted_carac='\\r'
		list_of_crypted_caracs.append(crypted_carac)
		#print(carac, crypted_index,crypted_carac )
		#print(list_of_crypted_caracs)
	
	crypted_message = "".join(list_of_crypted_caracs)

	return crypted_message

def cesar_decrypt(crypted_message, key):
	return cesar_ciffer(crypted_message, -key)


crypted_message = cesar_ciffer("j'ai envie de manger gratin de pates avec des lardons", 103)
print(crypted_message)
