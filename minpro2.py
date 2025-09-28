users = {
    "dapa": {"password": "123", "role": "admin"},
    "bawahan": {"password": "123", "role": "pengunjung"}
}

informasi_cuaca = [
    (32, 55, "Cerah"),
    (25, 70, "Berawan"),
    (18, 85, "Hujan")
]

def tentukan_kondisi(suhu, kelembapan):
    if suhu > 30 and kelembapan <= 60:
        return "Cerah"
    elif 20 <= suhu <= 30 and 60 <= kelembapan <= 80:
        return "Berawan"
    elif suhu < 20 or kelembapan > 80:
        return "Hujan"
    else:
        return "Tidak Diketahui"

def create_data():
    suhu = int(input("Masukkan suhu celcius: "))
    kelembapan = int(input("Masukkan kelembapan (%): "))
    kondisi = tentukan_kondisi(suhu, kelembapan)
    informasi_cuaca.append((suhu, kelembapan, kondisi))
    print("Data berhasil ditambahkan:", informasi_cuaca[-1])

def read_data():
    if not informasi_cuaca:
        print("Belum ada data cuaca.")
    else:
        print("=== Data Cuaca Saat Ini ===")
        for i, data in enumerate(informasi_cuaca, start=1):
            print(f"{i}. Suhu: {data[0]}°C | Kelembapan: {data[1]}% | Kondisi: {data[2]}")

def update_data():
    read_data()
    pilih = int(input("Pilih nomor data yang ingin diupdate: "))
    suhu = int(input("Masukkan suhu baru: "))
    kelembapan = int(input("Masukkan kelembapan baru: "))
    kondisi = tentukan_kondisi(suhu, kelembapan)
    informasi_cuaca[pilih - 1] = (suhu, kelembapan, kondisi)
    print("Data berhasil diupdate:", informasi_cuaca[pilih - 1])

def delete_data():
    read_data()
    pilih = int(input("Pilih nomor data yang ingin dihapus: "))
    removed = informasi_cuaca.pop(pilih - 1)
    print("Data berhasil dihapus:", removed)

def menu(role):
    while True:
        print("\n=== Menu Utama ===")
        if role == "admin":
            print("1. Create Data")
            print("2. Read Data")
            print("3. Update Data")
            print("4. Delete Data")
            print("5. Keluar ke Login")
        elif role == "pengunjung":
            print("1. Read Data")
            print("2. Keluar ke Login")

        pilihan = input("Pilih menu: ")

        if role == "admin":
            if pilihan == "1":
                create_data()
            elif pilihan == "2":
                read_data()
            elif pilihan == "3":
                update_data()
            elif pilihan == "4":
                delete_data()
            elif pilihan == "5":
                print("Keluar dari menu admin, kembali ke login.")
                break
            else:
                print("Pilihan tidak valid.")
        elif role == "pengunjung":
            if pilihan == "1":
                read_data()
            elif pilihan == "2":
                print("Keluar dari menu pengunjung, kembali ke login.")
                break
            else:
                print("Pilihan tidak valid.")

def login():
    while True:
        username = input("\nMasukkan username (atau ketik 'exit' untuk keluar): ").lower()
        if username == "exit":
            print("Program dihentikan.")
            break

        password = input("Masukkan password: ")

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role}")
            menu(role)
        else:
            print("Login gagal. Username atau password salah, coba lagi.")

try:
    login()
except ValueError:
    print("Input harus berupa angka.")
except IndexError:
    print("Nomor data tidak ditemukan.")
except KeyError:
    print("Data login tidak ditemukan.")
except ZeroDivisionError:
    print("Terjadi pembagian dengan nol.")
except (KeyboardInterrupt, EOFError):
    print("\nProgram dihentikan oleh pengguna (ctrl+c atau ctrl+d).")
except Exception as e:
    print("Error tak terduga:", e)
