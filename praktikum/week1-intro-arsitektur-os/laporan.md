
# Laporan Praktikum Minggu [X]
Topik: "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941 
- **Kelas** : 1IKRB

---

## Tujuan  
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.


---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/linux%20week1.png)

---

## Analisis
- Jelaskan makna hasil percobaan.
   * uname -a Perintah ini biasanya digunakan untuk menampilkan sistem oprasi yang tersedia.
   * whoami Untuk menampilkan nama pengguna atau adanya pengguna online atau login di terminal.
   * lsmod | head Biasanya digunakan untuk menampilkan daftar modul kernel yang sedang dimuat di sistem linux, tapi cuma 10 baris pertama dari daftar.
   * dmesg | head Perintah ini untuk melihat 10 baris pesan log pertama dan adapun kegunaan utamanya yaitu untuk medapatkan gambaran sekilas mengenai proses booting sistem dan identifikasi hardware.
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
   * Perintah-perintah dasar Linux/Unix berfungsi sebagai antarmuka penting antara pengguna dan Kernel, yang secara efektif mengungkap empat aspek fundamental dari Sistem Operasi (SO):

      * Identitas Inti Sistem (uname -a):
      Fungsi utamanya adalah mengidentifikasi Versi Kernel dan Arsitektur Hardware, yang merupakan fondasi tempat seluruh SO dibangun. Hal ini secara langsung terkait dengan Fungsi Kernel sebagai pengelola hardware utama dan konsep Arsitektur OS.

      * Identitas Pengguna Aktif (whoami):
      Fungsi utamanya adalah memverifikasi ID Pengguna Efektif dari proses yang berjalan. Hal ini mencerminkan peran Kernel dalam Manajemen Proses dan Keamanan (pengaksesan sumber daya), dan merupakan contoh bagaimana System Call digunakan untuk mengambil data keamanan dari Kernel space.

      * Manajemen Perangkat Dinamis (lsmod | head):
      Fungsi utamanya adalah menampilkan Modul Kernel (driver perangkat) yang sedang dimuat. Hal ini menyoroti desain Arsitektur Kernel Modular (seperti pada Linux), yang memungkinkan kernel memuat dan membongkar driver secara dinamis untuk efisiensi dan fleksibilitas dalam Manajemen Perangkat.

      * Riwayat Kesehatan Sistem (dmesg | head):
      Fungsi utamanya adalah melihat pesan log dari Kernel Ring Buffer. Hal ini mendemonstrasikan fungsi Kernel dalam Pencatatan Log (Debugging/Troubleshooting) dan menunjukkan proses Inisialisasi Sistem (deteksi hardware) yang terjadi di awal booting.

    Secara keseluruhan, perintah-perintah ini adalah contoh nyata dari bagaimana System Call memungkinkan program pengguna atau user-space seperti shell untuk meminta dan mendapatkan informasi yang sangat penting dari Kernel, inti dari SO.
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
   * Perbedaan Linux dan Windows, meskipun keduanya adalah sistem operasi modern, memiliki filosofi arsitektur dan diagnostik yang berbeda:
   Linux/Unix-like cenderung menggunakan alat yang berfokus pada Kernel secara langsung dan menyediakan data dalam format teks sederhana, mencerminkan desain yang transparan dan kernel centric.

   Windows menggunakan alat command line yang lebih berorientasi pada sistem atau layanan dan menyimpan data diagnostik di database terpusat seperti Event Log, mencerminkan desain kernel hibrida yang terintegrasi erat dengan layanan yang lebih tinggi.
---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
   1. System Call: Semua perintah ini adalah manifestasi praktis dari System Call, yang menjembatani User-Space (aplikasi/terminal) dengan Kernel-Space (inti SO). 
   2. Arsitektur OS: Perintah seperti lsmod dan dmesg memberikan bukti nyata tentang bagaimana Kernel Linux bekerja (modular dan self-logging).
   3. Perbedaan OS: Kontras dengan Windows menunjukkan perbedaan filosofi desain: Linux cenderung kernel-centric dan transparan, sementara Windows menggunakan mekanisme layanan dan logging yang lebih terpusat.   
---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi.  
   **Jawaban:**
   **Manajemen sumber daya, Antarmuka Pengguna, Manajemen file dan keamanan.**
2. Jelaskan perbedaan antara kernel mode dan user mode. 
   **Jawaban:**
   **Perbedaan antara Kernel Mode dan User Mode adalah konsep fundamental dalam arsitektur sistem operasi (SO) yang mengatur tingkat hak akses dan perlindungan. Keduanya menentukan kode mana yang boleh mengakses hardware dan memori.**
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel. 
   **Jawaban:**
   **Monolihic : FreeBSD, Solaris, Windows NT Kernel, Linux Kernel.**
   **Microkernel : QNX, L4, MINIX, dan Mach.** 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
   **Mengerjakan sampai tidak kenal waktu dan saya mendapatkan pengalaman yang baru.**
- Bagaimana cara Anda mengatasinya?
   **Mengajak teman-teman supaya bisa belajar bareng dan mempunyai ilmu yang baru.**  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
