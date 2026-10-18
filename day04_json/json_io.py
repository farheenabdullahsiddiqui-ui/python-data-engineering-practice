import os
from day02_collections import read_csv
import json

def convert_types(rows:list[dict[str,str]])->list[dict]:
    converted = []
    for row in rows:
        values= {}
        for k, v in row.items():
            if k == "Age" :
              values[k] = int(v)
            elif k == "Salary":
              values[k] = float(v)
            else:
              values[k]= v
        converted.append(values)

    return converted

def write_json(file_path:str, rows:list[dict])-> None:
    with open(file_path, mode='w', encoding='utf-8')as file:
      json.dump(rows,file, indent = 2, ensure_ascii=False)
    print(f"Wrote {len(rows)} rows to {file_path}")   

def read_json(file_path:str)-> list[dict]:
   with open (file_path, mode= 'r', encoding='utf-8') as file:
      return json.load(file)
                
if __name__ == "__main__":
    print("🚀 JSON Data Writer - Day 4")
    print("Python for Data Engineering\n")

    cleaned_data_path = os.path.join(os.path.dirname(__file__),"..", "day03","cleaned_data.csv")
    cleaned_data = read_csv.read_csv_dict(cleaned_data_path)
    converted_data = convert_types(cleaned_data)
    print(f"Converted data {converted_data}")

    json_path = os.path.join( os.path.dirname(__file__), "json_data.json")
    write_json(json_path, converted_data)

    print(type(converted_data[0]["Age"]), type(converted_data[0]["Salary"]))

    loaded = read_json(json_path)
    print(type(loaded[0]["Age"]), type(loaded[0]["Salary"]))