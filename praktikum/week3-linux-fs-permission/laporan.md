
# Laporan Praktikum Minggu [X]
Topik:  Manajemen File dan Permission di Linux 

---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menggunakan perintah `ls`, `pwd`, `cd`, `cat` untuk navigasi file dan direktori.
2. Menggunakan `chmod` dan `chown` untuk manajemen hak akses file.
3. Menjelaskan hasil output dari perintah Linux dasar.
4. Menyusun laporan praktikum dengan struktur yang benar.
5. Mengunggah dokumentasi hasil ke Git Repository tepat waktu.
---
## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
Pada praktikum minggu ini, mahasiswa akan mempelajari **pengelolaan file dan direktori menggunakan perintah dasar Linux**, serta konsep **permission dan ownership**.  
Praktikum berfokus pada:
- Navigasi sistem file dengan `ls`, `pwd`, `cd`, dan `cat`.
- Pengaturan hak akses file menggunakan `chmod`.
- Pengubahan kepemilikan file menggunakan `chown`.
- Dokumentasi hasil eksekusi dan pengelolaan repositori praktikum.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan. 
 **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ``` 
2. Perintah yang dijalankan. 
```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ``` 
3. File dan kode yang dibuat.
sudo chown root percobaan.txt
ls -l percobaan.txt  
4. Commit message yang digunakan.
 **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
ls -l
cd /tmp
ls -a
cat /etc/passwd | head -n 5
echo "Hello <NAME><NIM>" > percobaan.txt
ls -l percobaan.txt
chmod 600 percobaan.txt
ls -l percobaan.txt
sudo chown root percobaan.txt
ls -l percobaan.txt
praktikum/week3-linux-fs-permission/screenshots/
git add .
git commit -m "Minggu 3 - Linux File System & Permission"
git push origin main
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Cuplikan%20layar%202025-10-27%20104150.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
Tentu, berikut adalah ringkasan makna hasil percobaan Manajemen File dan Permission di Linux:

Hasil percobaan **Manajemen File dan *Permission* di Linux** menunjukkan bahwa sistem operasi Linux mengandalkan mekanisme keamanan yang kuat berdasarkan tiga konsep utama:

1.  **Kepemilikan (*Ownership*)**: Setiap file/direktori harus dimiliki oleh satu **Pemilik (*Owner*)** dan satu **Grup (*Group*)**. Pengguna lain yang tidak termasuk di dua kategori tersebut diklasifikasikan sebagai **Lainnya (*Others*)**.
2.  **Izin Akses (*Permissions*)**: Tiga jenis hak akses (**Read/r: Baca, Write/w: Tulis, Execute/x: Eksekusi**) dapat diterapkan secara independen untuk setiap kategori pengguna (*Owner*, *Group*, *Others*).
3.  **Keamanan Sistem**: Percobaan membuktikan bahwa kombinasi *Ownership* dan *Permission* (dimodifikasi dengan `chmod` dan `chown`) adalah kunci untuk **mengontrol akses, melindungi integritas data, dan menjaga keamanan sistem** dalam lingkungan *multi-user*.

**Intinya:** Percobaan menegaskan bahwa Linux menggunakan sistem *permission* yang terperinci untuk menentukan **siapa yang boleh melakukan apa** pada setiap file dan direktori.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
Tentu, inilah ringkasan hubungan antara hasil percobaan *permission* Linux dengan teori OS, tanpa menggunakan tabel.

***

Hasil percobaan yang menunjukkan bagaimana **izin file** (*read*, *write*, *execute*) dan **kepemilikan** (*Owner*, *Group*) diterapkan dan ditegakkan di Linux secara langsung mencerminkan tiga pilar arsitektur Sistem Operasi (OS).

### 1. Peran Kernel (Inti OS) 

Percobaan Anda membuktikan bahwa **Kernel** adalah manajer dan penegak keamanan yang utama. Ketika Anda mengatur *permission* dengan `chmod` atau *ownership* dengan `chown`, Anda memerintahkan Kernel untuk mengubah **metadata** file (yang disimpan di *inode*). Setiap upaya akses (membaca atau mengubah file) akan selalu **diperiksa** oleh Kernel terlebih dahulu. Kernel lah yang berhak menolak atau mengizinkan permintaan, memastikan bahwa aturan *permission* tidak dapat dilanggar.

### 2. Mekanisme System Call 

Semua interaksi dengan file system harus melalui **System Call** (panggilan sistem). Perintah di *shell* seperti `cat` (membaca) atau *system utility* lainnya tidak mengakses disk secara langsung; mereka meminta layanan dari Kernel melalui *System Call* (`open()`, `read()`, dll.). **System Call** berfungsi sebagai **gerbang kendali** (*gatekeeper*). Kernel menggunakan momen *System Call* ini untuk **memvalidasi** *permission* pengguna. Jika *permission* tidak sesuai, *System Call* akan mengembalikan pesan "Permission Denied" ke program pengguna.

### 3. Arsitektur OS (Mode Kernel vs. Mode User) 

Sistem *permission* adalah implementasi arsitektur **Mode *User*** dan **Mode *Kernel***. Program pengguna berjalan di Mode *User* dengan hak terbatas, sementara Kernel berjalan di Mode *Kernel* dengan hak istimewa penuh. *Permission* memastikan bahwa pengguna di Mode *User* **dipaksa** untuk meminta layanan melalui *System Call* untuk mengakses *hardware* atau mengubah data penting. Ini adalah prinsip proteksi yang mencegah program pengguna yang *error* atau berbahaya merusak integritas seluruh sistem.
-
Tentu, inilah ringkasan perbedaan hasil *permission* di lingkungan Linux dan Windows:

Perbedaan utama terletak pada model keamanan file.

Di **Linux**, hasil percobaan selalu menunjukkan model **diskrit** dan **ketat** berdasarkan tiga kategori pengguna (**Owner, Group, Others**) dan tiga izin dasar (**Read, Write, Execute**). Akses dikendalikan oleh string 9 karakter (`-rwxr-xr--`), dan sistemnya **case-sensitive** dengan hierarki file tunggal di bawah `/` (*root*).

Sementara itu, **Windows** menggunakan model **Access Control List (ACL)** yang jauh lebih **granular dan fleksibel**. Hak akses di Windows tidak terbatas pada *rwx* melainkan mencakup izin yang lebih luas (seperti *Full Control* atau *Modify*), dan diterapkan secara eksplisit untuk setiap pengguna atau grup tertentu, bukan berdasarkan tiga kategori umum. Windows juga memiliki struktur file berbasis *drive* (`C:`, `D:`) dan bersifat **case-insensitive**.

Secara singkat, **Linux menawarkan keamanan yang kaku dan sederhana (rwx)**, sedangkan **Windows menawarkan kontrol izin yang sangat terperinci (ACL)**.  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
Berdasarkan seluruh pembahasan mengenai manajemen file dan *permission* di Linux, berikut adalah 2-3 poin kesimpulan utama yang dapat diambil dari praktikum tersebut:

1.  **Sistem Keamanan Berbasis Tiga Dimensi (*Owner-Group-Others*) Adalah Fondasi Linux:** Praktikum menegaskan bahwa Kernel Linux mengimplementasikan model keamanan file yang ketat. Setiap sumber daya dikendalikan oleh **kepemilikan** (satu *Owner* dan satu *Group*) dan tiga jenis hak akses (**Read, Write, Execute**). Model ini berfungsi sebagai mekanisme pertahanan pertama untuk membatasi ruang gerak pengguna, melindungi file sistem, dan menjaga privasi data di lingkungan multi-user.

2.  **Kernel dan System Call Bekerja Sama Menegakkan *Permission*:** Percobaan membuktikan bahwa setiap interaksi file (seperti membaca atau memodifikasi) adalah bukti nyata dari arsitektur OS. Program pengguna harus menggunakan **System Call** untuk meminta akses, dan **Kernel** yang berjalan di *Mode Kernel* bertanggung jawab penuh untuk memvalidasi *permission* tersebut. Jika izin tidak sesuai, Kernel akan menolak permintaan, memastikan integritas sistem tidak terganggu.

3.  ***Permission* adalah Alat Kontrol Akses yang Dinamis dan Wajib Dikelola:** Penggunaan perintah seperti `chmod` (mengubah izin) dan `chown` (mengubah kepemilikan) menunjukkan bahwa hak akses file bukanlah sesuatu yang statis. Pengelola sistem harus secara aktif dan tepat mengatur *permission* untuk memastikan prinsip *Least Privilege* (hak akses seminimal mungkin) diterapkan, sehingga mencegah potensi risiko keamanan seperti modifikasi data yang tidak disengaja atau eksekusi program berbahaya oleh pengguna yang tidak berwenang.

---

## Quiz
1.  Apa fungsi dari perintah `chmod`? 
  **Mode Numerik (Oktal):** Menggunakan angka tiga digit (0-7) di mana setiap digit mewakili hak akses untuk *Owner*, *Group*, dan *Others*. Nilai angka dihitung berdasarkan penjumlahan:
    * **4** = Read (`r`)
    * **2** = Write (`w`)
    * **1** = Execute (`x`)

    *Contoh:*
    * `chmod 755 nama_file`: Memberikan hak penuh (4+2+1=**7**) kepada *Owner*, dan hak baca-eksekusi (4+1=**5**) kepada *Group* dan *Others*.

 **Mode Simbolik (Huruf):** Menggunakan huruf untuk menentukan kategori pengguna (`u`=user/owner, `g`=group, `o`=others, `a`=all) dan simbol operasi (`+` untuk menambah, `-` untuk mengurangi, `=` untuk menetapkan).

    *Contoh:*
    * `chmod g+w nama_file`: **Menambahkan** hak **write** (`w`) untuk **group** (`g`).
    * `chmod a-x nama_file`: **Menghapus** hak **execute** (`x`) untuk **semua** (`a`) pengguna.**  
2. Apa arti dari kode permission `rwxr-xr--`?   
   **Kode *permission* **`rwxr-xr--`** berarti hak akses file tersebut dibagi untuk tiga kategori pengguna utama sebagai berikut:

 **Owner (Pemilik):** Memiliki hak penuh, ditunjukkan oleh **`rwx`** (Read, Write, Execute). Pemilik dapat membaca, memodifikasi, dan menjalankan file tersebut.
 **Group (Grup):** Memiliki hak baca dan eksekusi saja, ditunjukkan oleh **`r-x`** (Read, Execute). Anggota grup dapat melihat isi dan menjalankan file, tetapi tidak dapat mengubahnya.
 **Others (Lainnya):** Hanya memiliki hak baca, ditunjukkan oleh **`r--`** (Read). Semua pengguna lain di sistem hanya dapat melihat isi file, tanpa hak untuk memodifikasi atau menjalankannya.

Secara numerik (oktal), kode ini setara dengan **`754`**.**  
3.  Jelaskan perbedaan antara `chown` dan `chmod`. 
   **Tentu, berikut adalah ringkasan perbedaan antara `chown` dan `chmod` tanpa menggunakan kode:

Perbedaan mendasar antara kedua perintah ini terletak pada fungsinya:

  **`chown` (Change Owner):** Perintah ini digunakan untuk mengubah **kepemilikan** file atau direktori, yaitu menentukan **siapa** yang menjadi pemilik (*Owner*) dan/atau **grup** file tersebut. Perintah ini biasanya memerlukan hak akses administratif (*root*).
  **`chmod` (Change Mode):** Perintah ini digunakan untuk mengubah **izin akses** (*permissions*) file atau direktori, yaitu menentukan **apa** yang dapat dilakukan oleh pemilik, grup, dan pengguna lain (membaca, menulis, atau mengeksekusi). Perintah ini hanya dapat dilakukan oleh pemilik file atau *root*.

Singkatnya, **`chown` mengubah pemilik file,** sedangkan **`chmod` mengubah hak akses file.****  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
kendala laptop harus dibagi sama kakak 
- Bagaimana cara Anda mengatasinya?  
menabung dan membeli laptop
---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
