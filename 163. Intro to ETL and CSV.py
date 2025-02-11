import csv

with open("file.csv", newline="", encoding="cp950") as f:
    csv_data = csv.reader(f)
    for row in csv_data:
        print(row)
