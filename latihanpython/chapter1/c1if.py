print "masukan dua buah angka"
print "dan anda akan check kedua angka tersebut"

angka1 = raw_input("masukan angka pertama:")
angka1 = int(angka1)

angka2 = raw_input("masukan angka kedua:")
angka2 = int(angka2)

if angka1 == angka2:
	print"angka sama dengan", angka1,"AND",angka2
if angka1 != angka2:
	print"angka tidak sama dengan", angka1,"AND",angka2	
if angka1 < angka2:
	print"angka kurang dari", angka1,"AND",angka2
if angka1 > angka2:
	print"angka lebih dari", angka1,"AND",angka2	
if angka1 <= angka2:
	print"angka kurang dari sama dengan", angka1,"AND",angka2
if angka1 >= angka2:
	print"angka lebih dari sama dengan", angka1,"AND",angka2
 
