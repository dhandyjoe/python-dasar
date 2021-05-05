def jumlah (angka1) :
	if( angka1 == 0 ) :
		return 1

	return angka1 * jumlah(angka1 - 1)

print (jumlah(4))
