
import csv

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "Grade"])
    writer.writerow(["John", 15, "10th"])
    writer.writerow(["Alice", 14, "9th"])
    writer.writerow(["Bob", 16, "11th"])

with open("students.csv", "r", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)