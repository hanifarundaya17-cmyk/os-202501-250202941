import csv

# Membaca dataset
processes = {}
allocation = {}
request = {}

with open("dataset_deadlock.csv", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        p = row["Process"]
        allocation[p] = row["Allocation"]
        request[p] = row["Request"]

# Membuat Wait-For Graph
wait_for = {}

for p in request:
    if request[p] != "-":
        for other in allocation:
            if allocation[other] == request[p]:
                wait_for[p] = other

# Deteksi siklus (deadlock)
visited = set()
stack = set()
deadlock_processes = set()

def detect_cycle(p):
    if p in stack:
        deadlock_processes.update(stack)
        return
    if p in visited:
        return
    visited.add(p)
    stack.add(p)
    if p in wait_for:
        detect_cycle(wait_for[p])
    stack.remove(p)

for process in wait_for:
    detect_cycle(process)

# Output hasil
print("=== HASIL DETEKSI DEADLOCK ===")
for p in allocation:
    status = "DEADLOCK" if p in deadlock_processes else "AMAN"
    print(f"{p} : {status}")
