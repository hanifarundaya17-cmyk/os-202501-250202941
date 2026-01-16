
# Laporan Praktikum Minggu [11]
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Hanif Arundaya Usman  
- **NIM**   : 250202941 
- **Kelas** : 1IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.
1. Deadlock adalah kondisi pada sistem operasi di mana dua atau lebih proses saling menunggu resource yang sedang dipegang proses lain sehingga tidak ada proses yang dapat melanjutkan eksekusi.
2. Deadlock dapat terjadi jika empat kondisi utama terpenuhi secara bersamaan, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.
3. Deadlock detection merupakan pendekatan yang membiarkan deadlock terjadi, kemudian sistem akan menjalankan algoritma khusus untuk mendeteksi proses-proses yang terlibat deadlock.
4. Algoritma deteksi deadlock bekerja dengan cara menganalisis alokasi resource dan permintaan resource untuk menentukan apakah masih terdapat proses yang dapat diselesaikan.
5. Setelah deadlock terdeteksi, sistem operasi perlu melakukan recovery, seperti terminasi proses atau pengambilan kembali resource, agar sistem dapat kembali berjalan normal.
---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
import csv

def detect_deadlock(processes, allocation, request, available):
    n = len(processes)
    work = available.copy()
    finish = [False] * n

    while True:
        found = False
        for i in range(n):
            if not finish[i]:
                if request[i] <= work:
                    work += allocation[i]
                    finish[i] = True
                    found = True
        if not found:
            break

    deadlocked = []
    for i in range(n):
        if not finish[i]:
            deadlocked.append(processes[i])

    return deadlocked


def read_dataset(filename):
    processes = []
    allocation = []
    request = []

    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            processes.append(row['Process'])
            allocation.append(int(row['Allocation']))
            request.append(int(row['Request']))

    return processes, allocation, request


if __name__ == "__main__":
    dataset_file = "dataset_deadlock.csv"
    processes, allocation, request = read_dataset(dataset_file)

    available = 0  # tidak ada resource bebas

    deadlocked_processes = detect_deadlock(
        processes, allocation, request, available
    )

    print("=== HASIL DETEKSI DEADLOCK ===")
    if deadlocked_processes:
        print("Deadlock terdeteksi!")
        print("Proses yang terlibat deadlock:")
        for p in deadlocked_processes:
            print("-", p)
    else:
        print("Tidak terjadi deadlock.")

```
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/Screenshot%202026-01-16%20160446.png)

---

## Analisis
Hasil menunjukkan bahwa seluruh proses berada dalam kondisi deadlock karena:
- Mutual Exclusion
- Hold and Wait
- No Preemption
- Circular Wait


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Algoritma deteksi deadlock mampu mengidentifikasi kondisi ketika proses tidak dapat melanjutkan eksekusi karena saling menunggu resource satu sama lain.

2. Hasil simulasi menunjukkan bahwa deadlock terjadi ketika keempat kondisi deadlock terpenuhi, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait.

3. Pendekatan deteksi deadlock penting digunakan pada sistem operasi karena memungkinkan pemanfaatan resource yang lebih optimal, meskipun memerlukan mekanisme pemulihan setelah deadlock terdeteksi.
---

## Quiz
### 1. Perbedaan prevention, avoidance, dan detection
- Prevention: mencegah salah satu kondisi deadlock
- Avoidance: menghindari deadlock dengan analisis state aman
- Detection: mendeteksi deadlock setelah terjadi

### 2. Mengapa deteksi deadlock diperlukan?
Karena tidak semua sistem dapat mencegah atau menghindari deadlock tanpa
mengorbankan performa.

### 3. Kelebihan dan kekurangan deteksi deadlock
**Kelebihan:**
- Lebih fleksibel
- Utilisasi resource tinggi

**Kekurangan:**
- Deadlock sudah terjadi
- Membutuhkan mekanisme recovery
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
