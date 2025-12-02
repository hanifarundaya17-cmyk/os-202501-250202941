
# Laporan Praktikum Minggu [X]
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menghitung *waiting time* dan *turnaround time* untuk algoritma FCFS dan SJF.  
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.  
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.  
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.  
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.  

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
---
## Ringkasan Teori Penjadwalan CPU (FCFS & SJF) 

1.  **Tujuan Penjadwalan dan *Context Switch***: Penjadwalan CPU adalah tugas inti **Kernel** untuk memaksimalkan utilisasi CPU. Proses penjadwalan melibatkan penghentian satu proses dan memulai proses lain (atau *thread*), yang dikenal sebagai ***Context Switch***. Setiap *Context Switch* memiliki **biaya *overhead*** (*system call* atau *interrupt*) karena *state* (keadaan) proses lama harus disimpan dan *state* proses baru harus dimuat.

2.  **Kriteria Pengambilan Keputusan (*Scheduling Criteria*)**: Algoritma penjadwalan dievaluasi berdasarkan kriteria yang menjadi fokus percobaan:
    * **Waktu Tunggu (*Waiting Time*)**: Total waktu yang dihabiskan proses dalam antrian siap (*ready queue*).
    * **Waktu *Turnaround* (*Turnaround Time*)**: Total waktu dari kedatangan hingga selesai (*completion*).
    * **Throughput**: Jumlah proses yang selesai per unit waktu.

3.  **FCFS: Kesederhanaan dan Efek *Convoy***: FCFS adalah algoritma non-preemptif yang paling sederhana, memilih proses berdasarkan **waktu kedatangan** saja. **Kelemahan teoretis utamanya** adalah **Efek *Convoy***: jika proses yang sangat panjang tiba dan dieksekusi duluan, semua proses pendek di belakangnya harus menunggu, menghasilkan **Rata-rata Waktu Tunggu yang sangat tinggi**.

4.  **SJF: Optimalitas dan Kebutuhan Prediksi**: SJF adalah algoritma (dapat berupa *preemptif* atau *non-preemptif*) yang secara **teori optimal** karena selalu menghasilkan **Rata-rata Waktu Tunggu yang minimum** untuk *set* proses tertentu. Hal ini dicapai dengan selalu menjalankan proses dengan **waktu *burst* CPU terpendek** terlebih dahulu. Namun, SJF menghadapi masalah implementasi: **OS harus memprediksi secara akurat** waktu *burst* CPU proses berikutnya, yang sulit dilakukan di dunia nyata.

5.  **Mode Operasi (*Kernel Mode* vs. *User Mode*)**: Seluruh fungsi *scheduler* (termasuk implementasi FCFS dan SJF) **berjalan di *Kernel Mode***. Keputusan untuk menjadwalkan ulang (misalnya, setelah suatu proses memanggil *System Call* I/O) adalah fungsi istimewa yang hanya dapat dilakukan oleh Kernel, memastikan keamanan dan pengelolaan sumber daya yang tepat.

---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan. 
1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main 
2. Perintah yang dijalankan.
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
| P1 | P2 | P3 | P4 |
0    6    14   21   24
3. File dan kode yang dibuat.  
praktikum/week5-scheduling-fcfs-sjf/screenshots/
4. Commit message yang digunakan.
git add .
git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
Turnaround Time (TAT) = WT + Burst Time
| P1 | P2 | P3 | P4 |
0    6    14   21   24
praktikum/week5-scheduling-fcfs-sjf/screenshots/
git add .
git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
git push origin main
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
[Screenshot hasil](screenshots/1.png) 
[Screenshot hasil](screenshots/2.png)
[Screenshot hasil](screenshots/3.png)
---

## Analisis
- Jelaskan makna hasil percobaan.  
Hasil percobaan (berupa Rata-rata Waktu Tunggu dan Rata-rata Waktu Turnaround) membuktikan efisiensi CPU Scheduler. Nilai yang terukur memvalidasi teori bahwa SJF (Shortest Job First) selalu optimal karena menghasilkan rata-rata waktu tunggu dan turnaround yang minimum, jauh lebih baik daripada FCFS (First-Come, First-Served) yang sederhana. Semakin rendah rata-rata waktu ini, semakin cepat dan responsif sistem dalam melayani user
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
Hasil ini secara langsung memvisualisasikan kerja Kernel sebagai manajer sumber daya utama. Perbedaan kinerja muncul karena Kernel menjalankan logika penjadwalan yang berbeda (FCFS vs. SJF) di dalam Mode Kernel. Ketika proses user selesai atau memanggil layanan (System Call), kontrol dialihkan ke Kernel, yang kemudian memicu CPU Scheduler. Oleh karena itu, overhead yang terukur dalam hasil juga mencakup biaya yang terkait dengan mekanisme context switch yang diaktifkan oleh System Call tersebut.  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
Linux (Kernel Monolitik) cenderung memberikan hasil SJF yang lebih murni dan cepat secara absolut. Overhead context switch-nya lebih kecil, menghasilkan AWT dan ATT yang lebih rendah.
Windows (Kernel Hibrida) mungkin menunjukkan variasi kinerja yang lebih besar. Karena adanya lapisan Executive dan mekanisme priority boosting yang ketat (untuk mencegah starvation), kinerja SJF mungkin tidak terlalu jauh berbeda dari FCFS jika dibandingkan dengan Linux murni, sebab Kernel Windows akan cenderung menaikkan prioritas proses yang lama menunggu.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1.  **SJF Menghasilkan Kinerja Optimal:** Praktikum memvalidasi teori bahwa **Shortest Job First (SJF)** adalah algoritma penjadwalan yang **optimal** dalam hal waktu. SJF selalu menghasilkan **Rata-rata Waktu Tunggu (*Waiting Time*)** dan **Rata-rata Waktu *Turnaround*** yang **minimum** dibandingkan dengan FCFS untuk *set* proses yang sama. Hal ini karena SJF secara strategis memproses *job* pendek terlebih dahulu, mengurangi penundaan kumulatif.

2.  **Kelemahan FCFS: Efek *Convoy***: **First-Come, First-Served (FCFS)** terbukti **tidak efisien** dan memiliki kinerja yang buruk. Praktikum menunjukkan bagaimana proses yang membutuhkan waktu eksekusi yang lama (*burst time* besar) yang datang di awal dapat menyebabkan proses-proses pendek lainnya harus menunggu lama. Kondisi ini disebut **Efek *Convoy***, yang menghasilkan Rata-rata Waktu Tunggu yang sangat tinggi.

3.  **Dilema Implementasi (Realitas vs. Teori)**: Meskipun SJF secara teoretis optimal, implementasinya di dunia nyata sangat sulit. Agar SJF berfungsi, **Kernel** harus tahu atau bisa memprediksi **waktu *burst* CPU** dari setiap proses sebelum dieksekusi. Praktikum menekankan bahwa dalam sistem operasi modern, algoritma murni seperti SJF jarang digunakan karena ketidakpastian ini dan risiko tinggi terjadinya ***starvation*** (proses panjang tidak pernah dieksekusi).

---
## Tugas
1. Hitung *waiting time* dan *turnaround time* dari minimal 2 skenario FCFS dan SJF.  
2. Sajikan hasil perhitungan dalam tabel perbandingan (FCFS vs SJF).  
3. Analisis kelebihan dan kelemahan tiap algoritma.  
Kelebihan,Kelemahan
Optimalitas: Secara teoretis terbukti optimal karena selalu menghasilkan waiting time dan turnaround time minimum.,Kebutuhan Prediksi: Tidak dapat diimplementasikan sepenuhnya di OS nyata karena mustahil Kernel mengetahui durasi burst time CPU yang tepat untuk proses di masa depan.
"Responsif: Proses-proses pendek diselesaikan dengan cepat, meningkatkan kepuasan pengguna (responsiveness).","Starvation: Dalam lingkungan dengan beban kerja tinggi, proses-proses yang sangat panjang mungkin tidak akan pernah mendapat giliran eksekusi karena selalu ada job pendek baru yang datang dan didahulukan."
4. Simpan seluruh hasil dan analisis ke `laporan.md`.  

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?  
Perbedaan utama terletak pada kriteria penjadwalan. FCFS (First-Come, First-Served) menjadwalkan proses berdasarkan waktu kedatangan—proses yang datang pertama dieksekusi pertama, menjadikannya algoritma yang sangat sederhana dan non-preemptif. Sebaliknya, SJF (Shortest Job First) menjadwalkan proses berdasarkan waktu burst CPU terkecil (lama eksekusi), yang berarti ia harus mengetahui atau memperkirakan durasi setiap proses.
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?  
SJF dapat menghasilkan rata-rata waktu tunggu minimum karena logikanya yang optimal: dengan menjalankan pekerjaan terpendek terlebih dahulu, ia memastikan bahwa proses-proses yang cepat selesai dengan cepat. Hal ini membebaskan CPU lebih awal dan secara kolektif mengurangi waktu tunggu untuk semua proses yang tersisa dalam sistem. Meskipun proses yang panjang harus menunggu, total penundaan yang disebabkannya pada proses-proses pendek lebih kecil dibandingkan jika proses pendek harus menunggu satu proses panjang selesai di FCFS
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?  
Kelemahan SJF pada sistem interaktif adalah sulitnya memprediksi waktu burst CPU secara akurat di awal, yang sangat penting untuk menjalankan algoritma ini. Yang lebih parah, SJF berpotensi menyebabkan starvation (kelaparan). Dalam lingkungan interaktif yang selalu ada job pendek baru, proses-proses yang membutuhkan waktu CPU lama mungkin tidak pernah mendapatkan giliran karena selalu ada proses pendek baru yang didahulukan


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Lumayan susah tapi harus dikerjakan
- Bagaimana cara Anda mengatasinya?
sering sering dikerjakan tugasnya   

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
