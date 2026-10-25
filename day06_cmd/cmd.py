import argparse
import os
from day02_collections import read_csv
from day03 import cleaned_data
import sys
from day05_grouping import group_salaries

if __name__ == "__main__":
   parser = argparse.ArgumentParser()
   parser.add_argument("input_file")
   parser.add_argument("--output",default=None)
   args= parser.parse_args()

   # Work on the input_file if give
   input_file = args.input_file
   print(f"{input_file}")
   file_path = os.path.join(os.path.dirname(__file__), input_file)
   print(f"{file_path}")

   # Read the input csv file
   data = read_csv.read_csv_dict(file_path)
   
   if not data:
        sys.exit(1)

   else:
        report = group_salaries.summarise_by_department(data)
        print(f"{report}")
        # Read the value of --output
        output_file = args.output

        print(f"{output_file}") 
        # if no --output print on console
        if not output_file:
            print("No output file specified, priting on console")
            print(f"{data}")
        else:
            # Write to csv 
            out_file_path = os.path.join(os.path.dirname(__file__),output_file)
            cleaned_data.write_csv_dict( out_file_path, data)
   
        

