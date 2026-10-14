import csv
import os

def read_csv(file_Path: str)-> None:
    with open(file_Path, mode='r', encoding="utf-8") as file:
        reader = csv.reader(file)
        rows= list(reader)
        print(rows)


if __name__ == "__main__":
     print("🚀 CSV Data Inspector - Day 2")
     print("Python for Data Engineering\n")

     sample_file = os.path.join(os.path.dirname(__file__) ,"..","day01_basics","sample_data.csv")
     print(sample_file)
     read_csv(sample_file)
       
