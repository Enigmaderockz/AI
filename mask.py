import pandas as pd
import random
import string
from datetime import datetime, timedelta
import csv

# Lists of first and last names for masking
first_names = [
    "John",
    "Emma",
    "Michael",
    "Olivia",
    "William",
    "Sophia",
    "James",
    "Ava",
    "Robert",
    "Isabella",
]
last_names = [
    "Smith",
    "Johnson",
    "Williams",
    "Jones",
    "Brown",
    "Davis",
    "Miller",
    "Wilson",
    "Moore",
    "Taylor",
]

# Function to generate a random decimal number
def random_decimal(precision, scale):
    integer_part = random.randint(0, 10 ** (precision - scale) - 1)
    decimal_part = random.randint(10 ** (scale - 1), 10**scale - 1)
    return float(f"{integer_part}.{decimal_part}")

# Function to generate a random date
def random_date(start_date="1900-01-01", end_date="2099-12-31"):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime("%Y-%m-%d")

# Function to mask account numbers based on column name, data type, and other parameters
def mask_account_number(
    column_name, account_number, data_type, length, extra_params=None
):
    if extra_params is None:
        extra_params = {}

    column_name = column_name.upper()  # Convert column_name to uppercase

    # Masking logic based on data type and column name
    if data_type.upper() in ["CHAR", "VARCHAR"]:
        account_number = str(account_number)
        if column_name == "GENDER":
            allowed_values = extra_params.get("allowed_values")
            masked_number = random.choice(allowed_values)
        elif column_name == "FIRST_NAME":
            masked_number = random.choice(first_names)
        elif column_name == "LAST_NAME":
            masked_number = random.choice(last_names)
        elif column_name == "ANY_NAME":
            separator = extra_params.get("separator", " ")
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            masked_number = f"{first_name}{separator}{last_name}"
        else:
            if len(account_number) == length:
                masked_number = "".join(
                    random.choices(string.ascii_uppercase + string.digits, k=length)
                )
            else:
                masked_number = account_number
    elif data_type.upper() == "DECIMAL":
        precision, scale = length
        masked_number = random_decimal(precision, scale)
    elif data_type.upper() == "DATE":
        masked_number = random_date()
    elif data_type.upper() == "INTEGER":
        if length is not None:
            min_value = 10 ** (length - 1)
            max_value = 10**length - 1
        else:
            min_value = extra_params.get("min_value", 0)
            max_value = extra_params.get("max_value", 2**31 - 1)
        masked_number = random.randint(min_value, max_value)
    else:
        masked_number = account_number
    return masked_number

# Function to mask columns in a CSV file
def mask_csv(input_file, output_file, columns_to_mask):
    df = pd.read_csv(input_file, sep="|")
    #print(f"Input file has {len(df)} records") 

    # Apply masking to each column in columns_to_mask
    for column_name, (data_type, length, extra_params) in columns_to_mask.items():
        if column_name != "FULL_NAME":  # Skip the FULL_NAME column for now
            df[column_name] = df[column_name].apply(
                lambda x: mask_account_number(
                    column_name, x, data_type, length, extra_params
                )
            )

    # Create the FULL_NAME column by concatenating the masked FIRST_NAME and LAST_NAME columns
    df["FULL_NAME"] = df["FIRST_NAME"] + " " + df["LAST_NAME"]

    df.to_csv(output_file, index=False, sep="|")

# Main function to execute the masking process
if __name__ == "__main__":
    input_file = "input.csv"
    output_file = "output.csv"

    # Define columns to mask and their respective data types, lengths, and extra parameters
    columns_to_mask = {
        "ACCT": ("VARCHAR", 10, None),
        "GENDER": ("VARCHAR", 1, {"allowed_values": ["F", "M"]}),
        "ID1": ("INTEGER", 4, None),
        "IDN": ("INTEGER", 2, None),
        "ID2": ("INTEGER", None, None),
        "DECIMAL_COLUMN": ("DECIMAL", (5, 4), None),
        "DATE_COLUMN": ("DATE", None, None),
        "FIRST_NAME": ("VARCHAR", 8, None),
        "LAST_NAME": ("VARCHAR", 8, None),
        "ANY_NAME": ("VARCHAR", 16, {"separator": " "}),
        "FULL_NAME": ("VARCHAR", 45, None),
    }

    mask_csv(input_file, output_file, columns_to_mask)
