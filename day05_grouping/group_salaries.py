
import os
from day04_json import json_io
from day02_collections import read_csv
import copy

def summarise_by_department(rows:list[dict])->dict:
    #1. Group the rows
    group = {}
    for row in rows:
        dept = row.get("Department", "Unknown")
        if not dept:
            dept = "Unknown"
        if dept not in group:
            group[dept] = []
        group[dept].append(row)

    report= {}
    for dept, dept_rows in group.items():
       report[dept] = json_io.summarise(dept_rows)
    return report


if __name__ == "__main__":
    messy_data = os.path.join(os.path.dirname(__file__), "..", "day04_json", "messy_data.csv")
    rows = read_csv.read_csv_dict(messy_data)

    report = summarise_by_department(rows)
    print(f"{report}")

    for dept in sorted(report):
        val = report[dept]
        print(f"{dept:>12} total = {val['total_salary']} avrg= {val['average_salary']} count={val['count']}")

    #Check for change in values
    before= copy.deepcopy(rows[0])
    report=summarise_by_department(rows)
    print("Before", before)
    print("After", rows[0])
    print("Unchanged", before==rows[0])

