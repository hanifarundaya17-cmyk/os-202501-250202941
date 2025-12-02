
# Laporan Praktikum Minggu [X]
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma.  


---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. Metrik Kinerja UtamaWaktu Penyelesaian Waktu proses berada dalam sistem (Selesai - Kedatangan).Waktu Tunggu : Total waktu proses menghabiskan di antrian siap.
2. Pengaruh Keadilan vs. EfisiensiRound Robin (RR): Tinggi keadilan  karena setiap proses mendapat giliran yang sama (time quantum). Mengorbankan sedikit efisiensi karena overhead context switch.Priority Scheduling (PS): Tinggi efisiensi dalam menyelesaikan tugas kritis (prioritas tinggi) lebih cepat. Mengorbankan keadilan dan berisiko menyebabkan starvation (kelaparan) pada proses prioritas rendah.
3. Pengaruh Time Quantum
Kecil: Baik untuk keadilan dan respons cepat, tapi buruk untuk throughput (banyak overhead).
Besar: Baik untuk efisiensi (kurang overhead), tapi buruk untuk keadilan dan waktu respons (mirip FCFS).
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
   1. Hitung *waiting time* dan *turnaround time* untuk algoritma RR dan Priority.  
   2. Sajikan hasil perhitungan dan Gantt Chart dalam `laporan.md`.  
   3. Bandingkan performa dan jelaskan pengaruh *time quantum* serta prioritas.  
   4. Simpan semua bukti (tabel, grafik, atau gambar) ke folder `screenshots/`.  

2. Perintah yang dijalankan.  
      | P1 | P2 | P3 | P4 | P1 | P3 | ...
   0    3    6    9   12   15   18  ...

   WT[i] = waktu mulai eksekusi - Arrival[i]
   TAT[i] = WT[i] + Burst[i]

   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
git push origin main
3. File dan kode yang dibuat. 
   praktikum/week6-scheduling-rr-priority/screenshots/
4. Commit message yang digunakan.
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
git add .
git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
git push origin main

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Cuplikan%20layar%202025-12-02%20105743.png)
![Screenshot hasil](screenshots/Cuplikan%20layar%202025-12-02%20110251.png)



---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. RR (Round Robin) unggul dalam keadilan dan responsivitas karena membagi waktu CPU secara merata menggunakan time quantum.
2. PS (Priority Scheduling) unggul dalam efisiensi menyelesaikan tugas kritis (prioritas tinggi) tetapi mengorbankan keadilan dan berisiko menyebabkan starvation.
3. Pilihan antara keduanya adalah trade-off: RR untuk keadilan, PS untuk urgensi/efisiensi tugas tertentu.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?   
   Round Robin  fokus pada kewajaran  dengan membagi waktu CPU menjadi irisan-irisan yang sama time quantum. Semua proses mendapat giliran.Priority Scheduling fokus pada kepentingan dengan memberikan CPU terlebih dahulu kepada proses yang memiliki prioritas tertinggi. 
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?   
   Time Quantum Kecil: Menyebabkan overhead tinggi (sering context switch), sehingga menurunkan efisiensi (throughput).Time Quantum Besar: Menyebabkan waktu respons buruk (sistem menjadi mirip FCFS), sehingga mengurangi kewajaran ($\text{fairness}$).
3. Mengapa algoritma Priority dapat menyebabkan *starvation*? 
   Penyebab Utama: CPU selalu memilih proses dengan prioritas tertinggi.
   Mekanisme Starvation: Jika proses berprioritas tinggi terus berdatangan secara berulang, proses berprioritas rendah akan terus tertunda dan tidak pernah mendapat kesempatan untuk dieksekusi, berapapun lama waktu tunggunya.
   Solusi: Teknik Aging (penuaan), di mana prioritas proses yang menunggu lama akan ditingkatkan secara berkala, digunakan untuk mencegah starvation.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
Maaf sebelumnya pak bahar telat mengumpulkan tugas week 6 dikarenakan laptop di pakai untuk mengerjakan soal sama kakak saya sekali lagi saya memohon minta maaf yang sebesar besarnya
- Bagaimana cara Anda mengatasinya?  
solusinya menurut saya adalah membeli laptop supaya tidak telat mengerjakan tugas 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
