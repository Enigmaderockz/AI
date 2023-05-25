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
              

 import csv

def compare_csv_files(file1: str, file2: str, outfile: str):
    # ... (the of the code remains the same until the end of the for loop that writes the rows with differences)

            # Close the HTML table
            html += "</table>\n"

            # Add the "Load More" functionality
            load_more_js = '''
            <script>
                function loadMore() {
                    var hiddenRows = document.querySelectorAll(".hidden-row");
                    var loadMoreButton = document.getElementById("load-more-button");
                    var rowsToShow = 100;
                    var rowsShown = 0;

                    for (var i = 0; i < hiddenRows.length && rowsShown < rowsToShow; i++) {
                        hiddenRows[i].classList.remove("hidden-row");
                        rowsShown += 1;
                    }

                    if (hiddenRows.length <= rowsToShow) {
                        loadMoreButton.style.display = "none";
                    }
                }
            </script>
            '''

            load_more_button = '''
            <button id="load-more-button" onclick="loadMore()" style="font-family: Helvetica, sans-serif; font-size: 14px; margin-top: 20px;">Load More</button>
            '''

            html += load_more_js + load_more_button

        # Write the contents of the entire HTML string to the output file
        outfile.write(html)

compare_csv_files("file1.csv", "file2.csv", "output.html")

