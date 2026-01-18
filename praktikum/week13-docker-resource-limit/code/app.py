import time

data = []
i = 0

print("Program mulai...")
try:
    while True:
        # Komputasi CPU
        for _ in range(10_000_000):
            i += 1

        # Alokasi memori bertahap
        data.append("A" * 10_000_000)  # ~10 MB
        print(f"Iterasi ke-{len(data)}, penggunaan memori bertambah")
        time.sleep(0.5)

except MemoryError:
    print("MemoryError: Memori tidak cukup!")
