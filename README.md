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

*Menu*\
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

hasil terminal
