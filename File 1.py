#Storing Data
brand = "Mikroflight"
usern = "MKRFLGHT2024"
passw = "01112024"

#Login Page Program
while True:
    print(f"\nLogin/Signup Page Administrator Maskapai {brand}:")
    print(f"1. Login")
    print(f"2. Keluar")

    opt1 = str(input(f"Masukkan pilihan (1-2): "))
            
    if opt1 == "1":
        print("\n=== LOGIN ===")
        if usern == "":
            print("Belum ada akun yang terdaftar. Silakan signup terlebih dahulu")
        else:
            intUsern = input("Masukkan username: ")
            intPassw = input("Masukkan password: ")
            
            if intUsern == usern and intPassw == intPassw:
                print(f"Login berhasil!")
                print(f"\nSelamat datang di Program {brand}! {intUsern}")
                print(f"\nMenu:")
                print(f"1. Input Data Customer untuk Pembelian")
                print(f"2. Pembayaran Tiket")
                print(f"3. Generate Kode Resi")
                print(f"4. Cetak Tiket Customer")
                print(f"5. Jadwal Penerbangan")
                print(f"6. Logout")

                #Menu ke Program Maskapai
                while True:

                    opt2 = str(input(f"Masukkan pilihan (1-6): "))

                    if opt2 == "1":
                        #Page Input data kustomer untuk membeli tiket (setelahnya ada page untuk konfirmasi data) [Natasya]
                        a=1

                    elif opt2 == "2":
                        #Page untuk pembayaran tiket yang nantinya berfungsi sebagai pembagian Kelas dan Tingkat Prioritas [Julius]
                        a=1

                    elif opt2 == "3":
                        #Page untuk Generate kode Resi setelah pembayaran GA-{Tahun}{Kota Asal}{Kota Akhir}{tingkat prioritas}{Nomor Urut[00x]} [Tonata]
                        a=1

                    elif opt2 == "4":
                        #Page untuk Cetak Tiket Konsumen menggunakan kode Resi [Jassemine]
                        a=1

                    elif opt2 == "5":
                        #Page untuk Pembagian Kelas dan Jadwal Penerbangan Tiket Berdasarkan Kode Resi Tiket [Felix]
                        a=1

                    elif opt2 == "6":
                        print(f"Kembali ke Menu Login...")
                        break
                    
                    else:
                        print(f"Menu tersebut tidak ada dalam pilihan. Silahkan coba lagi.")
                        

            else:
                print(f"Username atau password salah!")
                
    elif opt1 == "2":
        print(f"Program berakhir.")
        break

    else:
        print(f"Menu tersebut tidak ada dalam pilihan. Silahkan coba lagi.")