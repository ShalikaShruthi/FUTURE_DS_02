import os
import csv

folder = r"C:/Users/shali/OneDrive/Desktop/vs programs/II Social Media Campaign Performance Tracker/data"


for file in os.listdir(folder):
    if file.endswith(".csv"):
        file_path = os.path.join(folder, file)

        rows = []

        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)   # store the header
            rows.append(header)

            for row in reader:
                if row[3] == "":
                    row[3] = "Unknown"
                if row[4] == "":
                    row[4] = "Unknown"
                rows.append(row)

        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(rows)

print("Empty cells replaced with 'Unknown'")
