# Laporan Praktikum Minggu [14]
Topik: Penyusunan Laporan Praktikum Format IMRAD
---

## Identitas
- **Nama**  : Hanif Arundaya Usman
- **NIM**   : 250202941
- **Kelas** : 1IKRB

---

## Topik: Simulasi dan Mendeteksi Deadlock Dalam Sistem Operasi 
---

## Pendahuluan (Introduction)
## A. Latar Belakang  
 Deadlock merupakan salah satu permasalahan penting dalam sistem operasi yang terjadi ketika beberapa proses saling menunggu sumber daya yang sedang digunakan oleh proses lain sehingga tidak ada satu pun proses yang dapat melanjutkan eksekusi. Kondisi ini dapat menyebabkan sistem berhenti sebagian atau seluruhnya.
 
 Permasalahan deadlock sering terjadi pada sistem yang menerapkan pemrosesan paralel dan resource sharing. Jika deadlock tidak ditangani dengan baik, sistem dapat mengalami penurunan kinerja, pemborosan sumber daya, bahkan berhenti beroperasi. Oleh karena itu, sistem operasi harus memiliki mekanisme untuk menangani kondisi deadlock agar stabilitas sistem tetap terjaga.

 Salah satu pendekatan dalam penanganan deadlock adalah deadlock detection, yaitu metode yang membiarkan deadlock terjadi kemudian mendeteksinya melalui algoritma tertentu. Pendekatan ini dipilih karena tidak membatasi penggunaan sumber daya secara ketat seperti pada deadlock prevention dan deadlock avoidance. Dengan demikian, deadlock detection menjadi solusi yang relevan untuk sistem yang mengutamakan efisiensi penggunaan sumber daya.
## B. Rumusan Masalah
1. Bagaimana cara mendeteksi terjadinya deadlock pada sistem operasi serta mengidentifikasi proses-proses yang terlibat deadlock menggunakan algoritma deteksi deadlock?
2. Apa penyebab terjadinya deadlock pada sistem operasi berdasarkan hubungan alokasi dan permintaan sumber daya antar proses?
## C. Tujuan  
1. Untuk mengetahui cara mendeteksi terjadinya deadlock pada sistem operasi serta mengidentifikasi proses-proses yang terlibat deadlock menggunakan algoritma deteksi deadlock.
2. Untuk memahami penyebab terjadinya deadlock pada sistem operasi berdasarkan hubungan alokasi dan permintaan sumber daya antar proses.
---
## Metode (Metods)
## A. Lingkungan Uji
Praktikum ini berupa simulasi yang dijalankan dengan sistem operasi windows menggunakan bahasa pemograman python.
## B. Prosedur Eksperimen
1. Menyiapkan lingkungan uji dan perangkat lunak pendukung.
2. Menyusun dataset proses dan resource.
3. Mengimplementasikan algoritma deteksi deadlock.
4. Menjalankan program dengan dataset uji.
5. Menganalisis dan mendokumentasikan hasil eksperimen.
---
## Hasil (Results)
1. Dataset uji
    | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |
   | P4 | R4 | - |

    Keterangan:
- Process      : Menunjukkan identitas atau nama proses yang sedang berjalan di dalam sistem operasi (misalnya P1, P2, P3).
- Allocation   : Menunjukkan resource yang sedang dialokasikan atau dipegang oleh suatu proses pada saat tertentu.
- Request      : Menunjukkan resource yang diminta oleh proses untuk dapat melanjutkan eksekusinya.
Jika bernilai “–”, berarti proses tidak sedang meminta resource lain.
2. Hasik eksekusi program
Program berhasil dijalankan dan menghasilkan output deteksi deadlock. Berikut adalah screenshot hasil eksekusi:
![hasil eksekusi](./screenshots/Screenshot%202026-01-19%20081959.png)
3. Tabel Hasil Deteksi  
Berdasarkan eksekusi program terhadap dataset uji, diperoleh hasil sebagai berikut:

| Process | Allocation | Request |  Status  | Keterangan                               |
| :-----: | :--------: | :-----: | :------: | :--------------------------------------- |
|    P1   |     R1     |    R2   | Deadlock | Menunggu R2 yang sedang dipegang oleh P2 |
|    P2   |     R2     |    R3   | Deadlock | Menunggu R3 yang sedang dipegang oleh P3 |
|    P3   |     R3     |    R1   | Deadlock | Menunggu R1 yang sedang dipegang oleh P1 |
|    P4   |     R4     |    –    |   Aman   | Tidak meminta resource lain              |


---
## Pembahasan (Discussion)

## A. Interpretasi Hasil
Hasil pengujian menunjukkan bahwa proses P1, P2, dan P3 mengalami deadlock karena terjadi circular wait antar proses, sedangkan proses P4 berada dalam kondisi aman. Deadlock terjadi akibat proses saling menunggu resource yang dipegang oleh proses lain, sehingga tidak ada proses yang dapat melanjutkan eksekusi. Hasil ini membuktikan bahwa algoritma deteksi deadlock dapat bekerja dengan baik dalam mengidentifikasi kondisi deadlock.

## B. Analisis Kondisi Deadlock
Deadlock terjadi pada proses P1, P2, dan P3 karena terpenuhinya keempat kondisi deadlock. Resource yang digunakan bersifat mutual exclusion sehingga hanya dapat digunakan oleh satu proses dalam satu waktu. Setiap proses menahan satu resource sambil menunggu resource lain (hold and wait). Resource yang telah dialokasikan tidak dapat diambil secara paksa (no preemption). Selain itu, terdapat siklus permintaan resource (circular wait) antara P1, P2, dan P3.

Sebaliknya, proses P4 tidak mengalami deadlock karena tidak memiliki permintaan resource tambahan dan tidak terlibat dalam siklus permintaan resource.

---
## Kesimpulan
Berdasarkan hasil praktikum, dapat disimpulkan bahwa algoritma deteksi deadlock berhasil mengidentifikasi proses-proses yang mengalami deadlock berdasarkan hubungan alokasi dan permintaan resource. Deadlock terjadi ketika keempat kondisi deadlock terpenuhi secara bersamaan, khususnya adanya circular wait antar proses. Dengan demikian, mekanisme deadlock detection penting untuk membantu sistem operasi mengenali dan menangani kondisi deadlock secara efektif.

## Daftar Pustaka
1. Silberschatz, A., Galvin, P. B., & Gagne, G. Operating System Concepts.
2. Tanenbaum, A. S. Modern Operating Systems.
3. OSTEP – Deadlock Detection.
---
### Quiz
1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?
Karena IMRAD menyusun laporan secara sistematis mulai dari latar belakang, metode, hasil, hingga analisis, sehingga mudah dipahami dan direplikasi.
2. Apa perbedaan antara bagian Hasil dan Pembahasan?
Hasil berisi data atau temuan eksperimen, sedangkan Pembahasan berisi interpretasi dan analisis dari hasil tersebut.
3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?
Karena menunjukkan dasar teori yang digunakan dan menghindari plagiarisme.