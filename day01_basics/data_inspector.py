"""
data_inspector.py - A simple CSV data inspector
Day 1: Python basics for data engineering

This script demonstrates:
- Function definitions (def)
- Context managers (with open)
- Error handling (try/except)
- String formatting (f-strings)
- File I/O (reading/writing CSV)
"""

import csv
import os


def inspect_csv(file_path: str) -> None:
    """
    Reads a CSV file and prints basic info about it.
    
    Args:
        file_path: Path to the CSV file
    """
    print(f"\n{'='*50}")
    print(f"📂 Inspecting: {file_path}")
    print(f"{'='*50}")
    
    if not os.path.exists(file_path):
        print(f"❌ Error: File '{file_path}' not found.")
        return
    
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            rows = list(reader)
            
            if not rows:
                print("⚠️  The CSV file is empty.")
                return
            
            num_rows = len(rows)
            num_cols = len(rows[0])
            
            print(f"✅ Total rows (including header): {num_rows}")
            print(f"✅ Total columns: {num_cols}")
            print(f"✅ Column names: {rows[0]}")
            print(f"\n📋 First 5 rows:")
            print("-" * 40)
            for i, row in enumerate(rows[:5]):
                print(f"  Row {i}: {row}")
            
            print(f"\n📊 File size: {os.path.getsize(file_path):,} bytes")
            
    except PermissionError:
        print(f"❌ Error: Permission denied reading '{file_path}'.")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def create_sample_csv(file_path: str) -> None:
    """Creates a sample CSV file for practice."""
    sample_data = [
        ["Name", "Age", "City", "Salary"],
        ["Alice", "30", "New York", "75000"],
        ["Bob", "25", "London", "62000"],
        ["Charlie", "35", "Tokyo", "85000"],
        ["Diana", "28", "Berlin", "58000"],
        ["Eve", "32", "Paris", "72000"]
    ]
    
    with open(file_path, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    
    print(f"✅ Created sample CSV: {file_path}")


if __name__ == "__main__":
    print("🚀 CSV Data Inspector - Day 1")
    print("Python for Data Engineering\n")
    
    # Create sample data
    sample_file = "sample_data.csv"
    create_sample_csv(sample_file)
    
    # Inspect it
    inspect_csv(sample_file)
