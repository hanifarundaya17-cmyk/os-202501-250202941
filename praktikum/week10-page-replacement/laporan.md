
# Laporan Praktikum Minggu [10]
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.

---

## Dasar Teori
1. Page Replacement adalah mekanisme sistem operasi untuk mengganti halaman (page) di memori utama ketika terjadi page fault dan kapasitas memori sudah penuh.
2. FIFO (First In First Out) mengganti page yang pertama kali masuk ke memori tanpa memperhatikan frekuensi atau waktu terakhir penggunaan page tersebut.
3. LRU (Least Recently Used) mengganti page yang paling lama tidak digunakan dengan asumsi bahwa page yang sering dipakai di masa lalu kemungkinan akan dipakai lagi.
4. Tujuan utama algoritma page replacement adalah meminimalkan jumlah page fault agar kinerja sistem menjadi lebih optimal.
5. FIFO memiliki implementasi yang sederhana namun dapat mengalami Belady’s Anomaly, sedangkan LRU lebih efisien tetapi membutuhkan pencatatan riwayat penggunaan page.

---

## Langkah Praktikum
1. Menentukan reference string sebagai data uji.
2. Menentukan jumlah frame memori.
3. Mengimplementasikan algoritma FIFO.
4. Mengimplementasikan algoritma LRU.
5. Menjalankan simulasi page replacement.
6. Mencatat jumlah page fault dari masing-masing algoritma.
7. Menganalisis dan membandingkan hasil simulasi.
8. Melakukan commit dan push ke repository GitHub.

---

## Kode / Perintah
def fifo_page_replacement(pages, frames):
    memory = []
    page_faults = 0

    print("=== FIFO Page Replacement ===")
    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            status = "FAULT"
        else:
            status = "HIT"

        print(f"Page {page} -> {memory} ({status})")

    print(f"Total Page Fault (FIFO): {page_faults}\n")
    return page_faults


def lru_page_replacement(pages, frames):
    memory = []
    recent = []
    page_faults = 0

    print("=== LRU Page Replacement ===")
    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent.pop(0)
                memory.remove(lru_page)
                memory.append(page)
            status = "FAULT"
        else:
            recent.remove(page)
            status = "HIT"

        recent.append(page)
        print(f"Page {page} -> {memory} ({status})")

    print(f"Total Page Fault (LRU): {page_faults}\n")
    return page_faults


if __name__ == "__main__":
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    frames = 3

    fifo_faults = fifo_page_replacement(pages, frames)
    lru_faults = lru_page_replacement(pages, frames)

    print("=== Perbandingan ===")
    print(f"FIFO Page Faults : {fifo_faults}")
    print(f"LRU Page Faults  : {lru_faults}")

```
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202026-01-03%20113514.png)

---

## Analisis
### 1. Tabel Perbandingan Algoritma  

| Algoritma | Jumlah Page Fault | Keterangan                              |
| --------- | ----------------- | --------------------------------------- |
| FIFO      | 10                | Menutup halaman berdasarkan waktu masuk tanpa mempertimbangkan pola akses       |
| LRU       | 9                 | Mengganti halaman yang jarang digunakan |


### 2. Analisis Perbedaan Page Fault  
Jumlah page fault yang dihasilkan oleh algoritma FIFO dan LRU dapat berbeda karena strategi penggantian halaman yang digunakan oleh masing-masing algoritma tidak sama.  
### 3. Analisis algoritma mana yang lebih efisien  
Algoritma LRU menghasilkan lebih sedikit kesalahan halaman jika dibandingkan dengan FIFO, sehingga dapat disimpulkan bahwa LRU memiliki efisiensi yang lebih baik. Tingkat efisiensi LRU diperoleh dari kemampuannya dalam menyesuaikan penggantian halaman berdasarkan pola akses proses, meskipun cara kerjanya lebih rumit dibandingkan FIFO.

---

## Kesimpulan
1. Simulasi sebagai Lingkungan Uji yang Aman dan Terukur Simulasi diperlukan untuk menghindari risiko kerusakan sistem pada perangkat keras asli. Dengan simulasi, pengembang dapat mengukur performa algoritma secara presisi, mengulang skenario yang sama (reprodisibilitas), dan menghemat waktu serta biaya dalam fase pengembangan.
2. Keunggulan Komputasi pada Dataset Kompleks Perbedaan utama antara simulasi dan perhitungan manual terletak pada akurasi dan skalabilitas. Pada dataset besar, perhitungan manual hampir mustahil dilakukan tanpa kesalahan, sementara simulasi komputer dapat mengolah ribuan data secara instan, konsisten, dan mampu memvisualisasikan hasilnya melalui grafik atau Gantt Chart secara otomatis.
3. FCFS sebagai Algoritma Paling Sederhana Dari sisi implementasi, First-Come, First-Served (FCFS) adalah yang termudah karena hanya menggunakan struktur antrean sederhana tanpa perlu logika pengurutan prioritas atau interupsi waktu (preemption). Ini menjadikannya algoritma dasar yang paling stabil untuk dipelajari sebelum masuk ke algoritma yang lebih kompleks.

---

## E. Tugas & Quiz
### Tugas
1. Buat program simulasi FCFS atau SJF.  
2. Jalankan program dengan dataset uji.  
3. Sajikan output dalam tabel atau grafik.  
4. Tulis laporan praktikum pada `laporan.md`.
---
### Quiz
Jawab pada bagian **Quiz** di laporan:
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?  
jawaban : Simulasi menjadi sangat penting karena memungkinkan pengujian algoritma secara aman dan efisien. Jika kita menguji algoritma langsung pada sistem operasi yang sedang berjalan, risiko terjadinya kegagalan sistem (crash) sangat tinggi. Selain itu, simulasi memungkinkan kita untuk melakukan reprodisibilitas, yaitu mengulang skenario beban kerja yang sama persis pada berbagai algoritma untuk melihat mana yang paling unggul dalam hal kecepatan respon maupun penggunaan CPU.
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?  
jawaban : Ketika menghadapi dataset yang besar, perhitungan manual menjadi tidak praktis karena risiko kesalahan manusia (human error) yang sangat tinggi, seperti salah menjumlahkan milidetik atau melewatkan urutan proses. Sebaliknya, simulasi komputer menawarkan presisi tinggi dan kecepatan yang jauh melampaui kemampuan manusia; komputer dapat memproses ribuan data proses dalam sekejap tanpa kelelahan, serta mampu menangani logika interupsi yang kompleks secara otomatis.
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
jawaban : Algoritma First-Come, First-Served (FCFS) adalah yang paling mudah diimplementasikan. Hal ini dikarenakan logikanya yang sangat mendasar: proses yang tiba lebih dulu akan dieksekusi lebih dulu hingga selesai. Secara teknis, pengembang hanya perlu menggunakan struktur data antrean (FIFO Queue) sederhana tanpa perlu memikirkan prioritas, sisa waktu eksekusi, atau mekanisme pemotongan waktu (time quantum) yang rumit seperti pada algoritma Round Robin atau SJF.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
lagi lagi terkendala laptop di pakai kakak sehingga mengumpulkan tugas agak telat
- Bagaimana cara Anda mengatasinya?  
membeli laptop

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
