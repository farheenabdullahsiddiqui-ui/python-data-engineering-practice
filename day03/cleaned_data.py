import csv
import os
from day02_collections import read_csv

def write_csv(file_path:str, rows:list[list[str]])-> None:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
       writer = csv.writer(file)
       writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {file_path}")

def write_csv_dict(file_path: str, rows:list[dict[str,str]])-> None :
    if not rows:
        print("No rows to write")
        return
    fieldnames = list(rows[0].keys())
    with open(file_path, mode= 'w', newline='',encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames) 
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {file_path}")


if __name__ == "__main__":
     print("🚀 CSV Data Writer - Day 3")
     print("Python for Data Engineering\n")
     input_file = os.path.join(os.path.dirname(__file__),"..","day01_basics","sample_data.csv")
     output_file = os.path.join(os.path.dirname(__file__), "out_data.csv" )
     out_dict_file = os.path.join(os.path.dirname(__file__), "out_dict_data.csv")
     print(input_file)
     print(output_file)

     rows = read_csv.read_csv(input_file)
     rows_dict = read_csv.read_csv_dict(input_file)

    # write_csv(output_file, rows)
     write_csv_dict(out_dict_file, rows_dict)




    