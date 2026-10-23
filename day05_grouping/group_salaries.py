
import os
from day04_json import json_io
from day02_collections import read_csv

def summarise_by_department(rows:list[dict])->dict:
    #1. Group the rows
    groups= {}
    for row in rows:
        dept = row.get("Department","Unknown")
        if not dept:
            dept = "Unknown"

        if dept not in groups:
            groups[dept] = []
        groups[dept].append(row)

    #2. Summarise each group 
    report ={}
    for dept, dept_rows in groups.items():
      report[dept]= json_io.summarise(dept_rows)

    return report


if __name__ == "__main__":
    messy_data = os.path.join(os.path.dirname(__file__), "..", "day04_json", "messy_data.csv")
    rows = read_csv.read_csv_dict(messy_data)

    report = summarise_by_department(rows)
    print(f"{report}")
