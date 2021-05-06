
food = ["burger", "ice tea", "pizza", "fried chicken"]

# Melihat isi list
print(food)

# Panjang list 
print(len(food))

# Access List Items
print(food[2]) 	# indeks ke-2
print(food[-1]) 	# indeks ke-1 dari akhir list
print(food[1:3])	# indeks ke-1 sampai indeks ke-?
print(food[:2])	# sebelum indeks ke-2 akan dipanggil
print(food[1:])	# indeks ke-1 sampai akhir list
print(food[-3:-1])# indeks ke-3 dari belakang sampai indeks ke-? dari belakang

# Mengubah item value
food[0] = "oranye juice"
food[1:2] = ["hotdog", "milo"]
print(food)

# Menambah item value
food.append("aqua") # aqua akan secara otomatis masuk ke akhir list
food.insert(1, "nasi goreng") # pada indeks ke-1 akan berubah menjadi nasi goreng
print(food)

# Menghapus item value
food.remove("aqua") # menghapus menggunakan value
food.pop(1) # menghapus menggunakan indeks
print(food)
# -> food.clear() digunakan untuk menghapus value list

# Sort List
food.sort() # mengurutkan alfabet dari A 
print(food) 
food.sort(reverse= True) # mengurutkan alfabet dari Z
print(food) 
food.reverse() # Dibalik tanpa mengurutkan alfabet
print(food)

# Copy list 
makanan = food.copy()
print(makanan)
