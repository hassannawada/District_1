import csv
import os
class MarksError(Exception):          
    pass
os.makedirs("students", exist_ok=True)
with open("students/a.csv", "w") as f:
    f.write("name,marks\nAli,80\nSara,30\n")
with open("students/b.csv", "w") as f:
    f.write("name,marks\nBilal,abc\nZara,150\nHina,65\n")   
with open("students/c.csv", "wb") as f:
    f.write(b"\xff\xfe\x80garbage")                         

files = ["a.csv", "b.csv", "c.csv", "missing.csv"]          
results = []

for file_name in files:
    try:
        with open("students/" + file_name, "r") as f:
            for row in csv.DictReader(f):
                try:
                    marks = int(row["marks"])                # may raise ValueError
                    if marks < 0 or marks > 100:
                        raise MarksError("Marks must be 0-100")
                except ValueError:
                    print("Invalid marks for", row["name"])
                    continue
                except MarksError as e:
                    print(row["name"], "->", e)
                    continue
                status = "PASS" if marks >= 40 else "FAILED"
                results.append([row["name"], marks, status])
    except FileNotFoundError:
        print(file_name, "is missing")
    except UnicodeDecodeError:
        print(file_name, "is corrupted")
    else:
        print(file_name, "read OK")
    finally:
        print("Done with", file_name)

with open("results.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "marks", "status"])
    writer.writerows(results)

for r in results:
    print(r)
print("Failed students:", [r[0] for r in results if r[2] == "FAILED"])
