
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
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?   
   **Jawaban:**  
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?   
   **Jawaban:**  
3. Mengapa algoritma Priority dapat menyebabkan *starvation*? 
   **Jawaban:**  

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
