import csv
import os

def read_csv(file_path: str)-> list[list[str]]:
    with open(file_path, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows= list(reader)
        return rows

def read_csv_dict(file_path:str)->list[dict[str,str]]:
    with open(file_path, mode='r', encoding="utf-8") as file:
        dict_reader = csv.DictReader(file)
        dict_data = list(dict_reader)
        return dict_data


if __name__ == "__main__":
     print("🚀 CSV Data Inspector - Day 2")
     print("Python for Data Engineering\n")

     sample_file = os.path.join(os.path.dirname(__file__) ,"..","day01_basics","sample_data.csv")
     print(sample_file)
     data = read_csv(sample_file)
     print(f" File data {data}")
     #Unpacking the list
     head, *rows = data
     print(f" Header - {head}")
     print(f" Length of data {len(data)}")
     print(f" Length of rows  {len(rows)}")
     #Call to dict_reader
     dict_data= read_csv_dict(sample_file)

     for row in dict_data:
        for key, value in row.items():
            print(f"{key} : {value}")
        print("----------------------")
    