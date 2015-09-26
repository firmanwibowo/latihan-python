username = raw_input("masukan username :")
password = raw_input("masukan password :")

username_from_db="firman"
password_from_db="144firman"

if username == username_from_db: 
  if password == password_from_db:
    print "user name dan password cocok"
  else:
    print "user password salah"
else:
  print "user name salah"
else:
  print "user name salah" 
 
