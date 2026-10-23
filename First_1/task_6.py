with open("server.log", "w") as f:
    f.write("10:00 INFO Server started\n")
    f.write("10:01 ERROR DatabaseError connection lost\n")
    f.write("10:02 INFO User login\n")
    f.write("10:03 CRITICAL MemoryError out of memory\n")
    f.write("10:04 CRITICAL DatabaseError timeout\n")
    f.write("10:05 WARNING Slow response\n")

def read_lines(filename):
    """Generator: gives one line at a time (never loads full file)."""
    with open(filename) as f:
        for line in f:
            yield line.strip()

def critical_errors(lines):
    """Generator: gives only ERROR / CRITICAL lines."""
    for line in lines:
        parts = line.split()   # , ...]
        if parts[1] == "ERROR" or parts[1] == "CRITICAL":
            yield parts[2], line       # (error type, full line)

counts = {}
for error_type, line in critical_errors(read_lines("server.log")):
    if error_type in counts:
        counts[error_type] += 1
    else:
        counts[error_type] = 1
    print(line)
    print("   running count:", counts)    

numbers = (x * 2 for x in range(1000000))
print(next(numbers), next(numbers), next(numbers))
