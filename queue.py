from collections import deque
def simulasi_antrian():
    queue = deque()
    while True:
        print("\n1. tambahkan pelanggan ke antrian")
        print("2. layanin pelanggan")
        print("3. tampilkan antrian")
        print("4. keluar")
        pilihan = input("pilih opsi:")
        if pilihan=="1":
            nama = input("masukan nama pelanggan:")
            queue.append(nama)
            nama = input("masukan nama pelanggan:")
            print(f"pelanggan {nama} ditambahkan ke antrian.")
        elif pilihan=="2": 
            if queue: 
                dilayanin = queue.popleft()
                print(f"pelanggan {dilayanin} sedang dilayanin") 
            else:
                print("antrian kosong")
        elif pilihan=="3": 
            print("keluar saat ini:" ,list (queue)) 
        elif pilihan=="4":
            print("keluar dari program.")
        else:
            print("opsi tidak valid!")   
print (simulasi_antrian())
