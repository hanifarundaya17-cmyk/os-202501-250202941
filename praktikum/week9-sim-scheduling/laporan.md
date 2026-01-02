
# Laporan Praktikum Minggu [9]
Topik: Simulasi Algoritma Penjadwalan CPU


---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941 
- **Kelas** : IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
### 1. Transisi dari Teori ke Implementasi

Mahasiswa beralih dari perhitungan manual (kertas) menuju **otomatisasi komputasional**. Fokus utamanya adalah menerjemahkan logika algoritma ke dalam kode program untuk menghitung metrik efisiensi seperti *Waiting Time* (WT) dan *Turnaround Time* (TAT) secara instan.

### 2. Penerapan Logika Antrean dan Prioritas

Praktikum ini menguji pemahaman struktur data dalam menangani proses:

* **FCFS:** Mengelola proses berdasarkan urutan kedatangan (*Queue*).
* **SJF:** Mengelola proses berdasarkan durasi *burst* terpendek, yang memerlukan logika pengurutan (*sorting*) atau pemilihan dinamis.

### 3. Validasi Data dan Visualisasi Hasil

Selain menjalankan kode, mahasiswa dituntut untuk mampu menyajikan dan menganalisis output program. Hasil eksekusi harus disajikan dalam bentuk **tabel atau grafik (Gantt Chart)** untuk memvalidasi apakah hasil otomatisasi program sudah sesuai dengan konsep teoritis yang dipelajari sebelumnya.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan. 
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main 
2. Perintah yang dijalankan.  
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main
3. File dan kode yang dibuat. 
praktikum/week9-sim-scheduling/
├─ code/
│  ├─ scheduling_simulation.*
│  └─ dataset.csv
├─ screenshots/
│  └─ hasil_simulasi.png
└─ laporan.md 
4. Commit message yang digunakan.
git add .
git commit -m "Minggu 9 - Simulasi Scheduling CPU"
git push origin main

---

## Kode Progam
processes = [
    ("P1", 0, 6),
    ("P2", 1, 8),
    ("P3", 2, 7),
    ("P4", 3, 3),
]

def fcfs(processes):
    time = 0
    result = []

    for p in processes:
        pid, arrival, burst = p
        if time < arrival:
            time = arrival
        waiting = time - arrival
        turnaround = waiting + burst
        time += burst
        result.append((pid, waiting, turnaround))

    return result


print("=== FCFS ===")
for p in fcfs(processes):
    print(p)

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202026-01-02%20165556.png)


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Transformasi Metode Kerja Praktikum ini menandai peralihan dari perhitungan manual yang rentan kesalahan ke otomatisasi menggunakan program. Hal ini memungkinkan pengolahan dataset besar secara cepat, akurat, dan konsisten, yang tidak mungkin dilakukan secara manual.
2. Validasi Konsep melalui Implementasi Melalui simulasi, mahasiswa dapat membuktikan teori algoritma secara langsung. FCFS diuji sebagai algoritma dengan logika antrean paling sederhana, sementara SJF diimplementasikan untuk melihat bagaimana prioritas berdasarkan durasi burst dapat mengoptimalkan rata-rata waktu tunggu (Waiting Time).
3. Visualisasi untuk Analisis Kinerja Simulasi tidak hanya menghasilkan angka, tetapi juga menyediakan data terstruktur untuk pembuatan Gantt Chart. Visualisasi ini sangat penting untuk menganalisis efisiensi penggunaan CPU dan membandingkan performa antar algoritma secara objektif berdasarkan dataset yang diuji.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
Simulasi berfungsi sebagai laboratorium virtual yang aman untuk menguji performa algoritma tanpa risiko merusak sistem asli. Hal ini memungkinkan pengembang untuk mereplikasi skenario beban kerja tertentu secara berulang (reproducible) guna mendapatkan data perbandingan yang objektif.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
Pada dataset besar, perbedaan utamanya terletak pada efisiensi dan presisi. Perhitungan manual sangat rentan terhadap human error dan memakan waktu lama seiring bertambahnya data. Sebaliknya, simulasi komputer menawarkan kecepatan tinggi, akurasi tetap (konsisten), dan kemampuan untuk memvisualisasikan data secara otomatis melalui grafik atau tabel.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
FCFS (First-Come, First-Served) adalah yang paling mudah karena logikanya hanya mengikuti antrean linear (FIFO). Program hanya perlu mengeksekusi proses sesuai urutan kedatangan tanpa perlu melakukan sortir atau evaluasi ulang di tengah jalan. Sebaliknya, SJF lebih kompleks karena memerlukan logika tambahan untuk pengurutan (sorting) atau pemilihan durasi tersingkat setiap kali CPU tersedia.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
