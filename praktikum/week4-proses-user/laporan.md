
# Laporan Praktikum Minggu [X]
Topik: Manajemen Proses dan User di Linux
---

## Identitas
- **Nama**  : Hanif Arundaya Usman 
- **NIM**   : 250202941
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep proses dan user dalam sistem operasi Linux.  
2. Menampilkan daftar proses yang sedang berjalan dan statusnya.  
3. Menggunakan perintah untuk membuat dan mengelola user.  
4. Menghentikan atau mengontrol proses tertentu menggunakan PID.  
5. Menjelaskan kaitan antara manajemen user dan keamanan sistem.  

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
- Membuat dan mengatur proses (process management).  
- Mengelola user, group, serta hak akses pengguna.  
- Menampilkan, menghentikan, dan mengontrol proses yang sedang berjalan.  
- Menghubungkan konsep user management dengan keamanan sistem operasi.


---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan. 
- Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/ 
2. Perintah yang dijalankan. 
whoami
id
groups
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
git add .
git commit -m "Minggu 4 - Manajemen Proses & User"
git push origin main 
3. File dan kode yang dibuat.
praktikum/week4-proses-user/  
4. Commit message yang digunakan.
 git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
whoami
id
groups
ps aux | head -10
top -n 1
sleep 1000 &
ps aux | grep sleep
kill <PID>
pstree -p | head -20
git add .
git commit -m "Minggu 4 - Manajemen Proses & User"
git push origin main
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Cuplikan%20layar%202025-11-01%20105220.png)

---

## Analisis
- Jelaskan makna hasil percobaan.
Hasil praktikum menunjukkan bahwa Linux menjalankan setiap program sebagai proses yang teridentifikasi oleh PID. Proses ini diatur secara hierarkis, berakar pada PID 1 (systemd/init). Kemampuan untuk memonitor status dan mengakhiri proses secara selektif (dengan kill menggunakan PID) atau massal (dengan killall menggunakan nama) menegaskan bahwa user memiliki kontrol granular terhadap lingkungan eksekusi. Selain itu, perbedaan kemampuan antara user biasa dan user root (melalui sudo) memperjelas bahwa sistem menggunakan model kepemilikan dan hak istimewa untuk menegakkan keamanan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
Semua hasil praktikum di atas adalah manifestasi dari tugas Kernel sebagai jantung OS. Kernel bertindak sebagai pengelola sumber daya utama yang bertanggung jawab atas penjadwalan proses dan alokasi memori. Perintah shell yang kita gunakan (seperti kill) pada dasarnya adalah panggilan ke System Call yang berfungsi sebagai gerbang aman dari User Mode ke Kernel Mode. Arsitektur Linux yang monolitik memungkinkan interaksi Kernel dengan manajemen proses menjadi sangat efisien karena semua layanan inti berada dalam satu ruang alamat.  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?
Akar Proses: Linux memiliki PID 1 (systemd) yang jelas sebagai ancestor semua proses. Windows memiliki rantai boot yang lebih terfragmen (smss.exe $\rightarrow$ wininit.exe).Kontrol: Linux menonjolkan kontrol command line yang detail (berdasarkan PID) yang ideal untuk server. Windows lebih mengutamakan GUI (Task Manager) dan API CreateProcess() yang berbeda dari model fork()/exec() di Linux.Keamanan: Linux bergantung pada hak istimewa root dan kepemilikan file, sedangkan Windows menggunakan sistem ACL (Access Control List) yang lebih kompleks untuk mengontrol akses.  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Struktur dan Kontrol Sistem Berpusat pada PID 1 (init/systemd): Praktikum ini menegaskan bahwa sistem operasi Linux memiliki hierarki yang kaku, di mana proses init atau systemd selalu menjadi proses induk (PID 1) dari semua proses lainnya. Dengan menguasai manajemen proses menggunakan perintah seperti ps, top, kill, dan killall, kita dapat memantau kesehatan sistem, mengidentifikasi proses yang malfunction, dan menghentikannya secara spesifik (dengan PID melalui kill) atau massal (dengan nama melalui killall).
2. Keamanan dan Administrasi Berbasis Hak Istimewa (root): Praktikum ini menyoroti pentingnya model keamanan berlapis Linux melalui manajemen user. Pengguna root memiliki hak istimewa tak terbatas yang memungkinkannya melakukan semua konfigurasi dan administrasi sistem. Untuk menjaga stabilitas dan keamanan, semua tugas administratif kritis harus dijalankan dengan hak istimewa ini (biasanya melalui sudo) dan bukan oleh pengguna biasa. Ini membatasi potensi kerusakan sistem dari kesalahan atau malware yang dijalankan oleh user reguler.
3. Memahami Proses Booting dan Startup Layanan: Penguasaan konsep init/systemd menunjukkan bahwa proses booting modern diatur oleh sistem inisialisasi yang canggih. Melalui alat seperti systemctl (untuk systemd), administrator dapat mengelola dan mengotomatiskan startup layanan (daemon) penting, memastikan bahwa aplikasi seperti server web atau database berjalan secara otomatis dan efisien segera setelah sistem boot selesai.
---

## Quiz
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux? 
Proses init atau systemd adalah proses pertama (PID 1) yang dijalankan kernel Linux setelah booting. Fungsinya sangat sentral, yaitu sebagai manajer sistem utama. Ia bertanggung jawab untuk menginisialisasi seluruh sistem, mengelola layanan (daemon) agar berjalan otomatis dan paralel saat boot, dan bertindak sebagai induk yang mengawasi serta membersihkan proses anak yang berhenti (reaper). Intinya, ia memastikan sistem beroperasi dengan baik setelah kernel dimuat. 
2. Apa perbedaan antara `kill` dan `killall`?  
Perbedaan utama antara kill dan killall terletak pada cara mereka menargetkan proses. Perintah kill bersifat spesifik karena ia mengakhiri proses berdasarkan PID (Process ID) atau nomor identifikasi uniknya. Sebaliknya, perintah killall bersifat lebih luas karena ia mengakhiri semua instance proses yang sesuai dengan Nama Proses yang diberikan. Keduanya, secara default, mengirimkan sinyal pengakhiran yang lembut, yaitu SIGTERM.
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?
Pengguna root memiliki hak istimewa tertinggi di Linux karena ia adalah administrator sistem atau superuser. Hak istimewa ini memberikan kontrol mutlak dan akses tak terbatas ke semua file, direktori, dan sumber daya. Akses ini mutlak diperlukan untuk melaksanakan tugas-tugas administratif kritis di seluruh sistem, seperti instalasi perangkat lunak, modifikasi konfigurasi sistem, dan manajemen pengguna. Model ini juga berfungsi sebagai lapisan keamanan yang mencegah pengguna biasa secara tidak sengaja atau sengaja merusak komponen sistem yang vital.


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
tugas nyaa agak susah
- Bagaimana cara Anda mengatasinya?  
dikerjakan dan ikuti dengan baik materinya
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
