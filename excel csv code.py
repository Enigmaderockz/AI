import csv
import pandas as pd
import os

def read_file(file_path    _, file_extension = os.path.splitext(file_path)
    if file_extension == ".csv":
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            rows = [row for row in reader]
    elif file_extension == ".xlsx":
        df = pd.read_excel(file_path)
        rows = df.to_dict(orient="records")
    else:
        raise ValueError("Unsupported file format")
    return rows

def compare_files(file1: str, file2: str, outfile: str):
    # Read contents of both files into lists
    rows1 = read_file(file1)
    rows2 = read_file(file2)

    # Initialize counters
    num_records = 0
    num_diff_records = 0
    num_blank_diff_records = 0

    # Get headers/fieldnames
    header1 = list(rows1[0].keys())
    header2 = list(rows2[0].keys())

    # Check if both files have same headers/fieldnames
    if header1 != header2:
        raise ValueError("Headers not matching in both files")

    # Check if both files have same number of records
    if len(rows1) != len(rows2):
        raise ValueError("Number of rows not matching in both files")

    # Sort the rows of both files by their values to handle different ordering
    sorted_rows1 = sorted(rows1, key=lambda row: tuple(row.values()))
    sorted_rows2 = sorted(rows2, key=lambda row: tuple(row.values()))

    # Rest of the code remains the same

compare_files("file1.csv", "file2.csv", "output.html")
compare_files("file1.xlsx", "file2.xlsx", "output.html")
