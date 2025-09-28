# minpro2-2025
*Nama : Daffa Arkhabista,\
nim :2509116018,\
Sistem informasi A*

*Bagian awal*\
Program mulai dengan bikin dictionary users berisi username, password, dan role. Jadi ada dua role utama: admin sama pengunjung. Terus ada list informasi_cuaca yang isinya data awal cuaca berupa (suhu, kelembapan, kondisi).

*Fungsi tentukan_kondisi*\
Di sini ada logika buat nentuin kondisi cuaca dari input suhu sama kelembapan. Kalau suhu panas banget tapi kelembapan rendah → cerah. Kalau sedang-sedang → berawan. Kalau dingin atau kelembapan tinggi → hujan. Kalau gak masuk kategori itu → statusnya “tidak diketahui”.

*CRUD utama*

create_data: input suhu + kelembapan → otomatis dihitung kondisi → data baru masuk list.

read_data: nampilin semua isi list informasi_cuaca. Kalau kosong, keluar teks belum ada data.

update_data: pilih data mana yang mau diganti, lalu isi ulang suhu + kelembapan baru, kondisi dihitung lagi, data lama ketimpa.

delete_data: pilih data, lalu langsung dihapus dari list.

*Menu*
Ada dua versi menu sesuai role.

Kalau login sebagai admin, menu punya 5 opsi: create, read, update, delete, dan logout.

Kalau login sebagai pengunjung, menu lebih sederhana, cuma bisa read data cuaca sama keluar (logout).

Menu ini jalan di dalam loop while True, jadi bakal muter terus sampai user pilih keluar.

Login
Login juga pakai loop while True. User masukin username + password, kalau cocok maka akan diarahkan ke menu sesuai role. Kalau salah, muncul teks gagal login. Kalau user ngetik exit, program langsung berhenti.

Error Handling
Di bagian paling bawah ada try–except. Tujuannya supaya program gak langsung crash kalau ada error. Contoh: input angka salah format (ValueError), indeks data gak ada (IndexError), username gak ditemukan (KeyError), atau program dihentikan manual pakai Ctrl+C (KeyboardInterrupt). Jadi alurnya lebih aman.

*flowchart.*




# hasil coding\
<img width="1652" height="890" alt="Screenshot 2025-09-28 184336" src="https://github.com/user-attachments/assets/410db16f-6955-40ab-b715-545ab5caa6ab" />

<img width="1652" height="364" alt="Screenshot 2025-09-28 184404" src="https://github.com/user-attachments/assets/fa5a7416-5da3-4eeb-9905-129cb54e347b" />

<img width="1650" height="910" alt="Screenshot 2025-09-28 184419" src="https://github.com/user-attachments/assets/2d6e7f45-1b39-44d7-a0a9-16651bc244f0" />

<img width="1654" height="752" alt="Screenshot 2025-09-28 184438" src="https://github.com/user-attachments/assets/7c664673-d3a7-478e-a3f9-de1e9daac8c6" />

# hasil terminal
diawal user disuruh memasukan nama dan pasword\
<img width="733" height="133" alt="Screenshot 2025-09-28 184459" src="https://github.com/user-attachments/assets/2208380a-3ed2-47bd-93d8-2aa2d2dca6be" />

tersedia 2 user yang pertama dapa, sebagai admin yang bisa ngedit data-data dalama coding\
<img width="732" height="262" alt="Screenshot 2025-09-28 184511" src="https://github.com/user-attachments/assets/ad118ed0-5e09-41e0-b197-147b131235b8" />

dan yang kedua ada bawahan yang berperan sebagai pengunjung, ini hanya bisa melihat data saja tidak bisa ngedit\
<img width="724" height="212" alt="Screenshot 2025-09-28 184536" src="https://github.com/user-attachments/assets/1efd5c0e-d4f4-404d-ab9c-553d9de8017d" />

pasword untuk kedua user sama yaitu "123" jika salah dalam penulisan nama atau pasw maka disuruh ulang\
<img width="760" height="236" alt="Screenshot 2025-09-28 184600" src="https://github.com/user-attachments/assets/33a1bdf5-bd28-43bc-b326-40de21b29feb" />

untuk menu pertama ada create, disini kita bisa ngebuat data baru dan data tersersebut akan tersimpan\
<img width="686" height="323" alt="Screenshot 2025-09-28 184626" src="https://github.com/user-attachments/assets/3962651c-e116-479f-a3a5-f2882cb6915b" />

untuk menu kedua yaitu read, menu ini hanya bisa melihat data-data yang telah ada\
<img width="677" height="289" alt="Screenshot 2025-09-28 184640" src="https://github.com/user-attachments/assets/5b962122-ae7d-405c-8791-896e4df249a1" />

yang ketiga ada update, disini kita bisa melakukan update pada data yang telah ada/dibuat sebelumnya menjadi data baru\
<img width="668" height="375" alt="Screenshot 2025-09-28 184719" src="https://github.com/user-attachments/assets/b454aa7a-230d-49b8-a86e-e6dee77678ce" />\
setelah melakukan update akan muncul pada read\

menu ke empat ada delete, sesuai nama menu ini digunakan untuk menghapus data yang ada. setelah menghapus data tersebut maka data hilang dan dapat di cek dalam read\
<img width="688" height="588" alt="Screenshot 2025-09-28 184948" src="https://github.com/user-attachments/assets/16369f13-c54c-4bbe-8827-463dad087492" />
