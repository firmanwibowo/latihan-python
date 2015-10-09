username = input("masukan nama user name :")
password = input("masukan password :")
password = int(password)

username_from_db = "firman"
password_from_db = int(123)

if username  == username_from_db:
	if password == password_from_db:
		print ("selamat anda berhasil login")
	else:
		print ("anda tidak berhasil login")
	
