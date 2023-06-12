import pandas as pd
import random
import string
from datetime import datetime, timedelta

def random_decimal(precision, scale):
    integer_part = random.randint(0, 10**(precision - scale) - 1)
    decimal_part = random.randint(10**(scale - 1), 10**scale - 1)
    return float(f"{integer_part}.{decimal_part}")

def random_date(start_date="1900-01-01", end_date="2099-12-31"):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    random_date = start + timedelta(days=random.randint(0, (end - start).days))
    return random_date.strftime("%Y-%m-%d")

def mask_account_number(column_name, account_number, data_type, length, extra_params=None):
    if extra_params is None:
        extra_params = {}
    
    column_name = column_name.upper()  # Convert column_name to uppercase
        
    if data_type.upper() in ['CHAR', 'VARCHAR']:
        account_number = str(account_number)
        if column_name == 'GENDER':
            allowed_values = extra_params.get('allowed_values')
            masked_number = random.choice(allowed_values)
        elif column_name in ['FIRST_NAME', 'LAST_NAME']:
            masked_number = ''.join(random.choices(string.ascii_letters, k=length))
        elif column_name == 'FULL_NAME':
            separator = extra_params.get('separator', ' ')
            first_name_length = random.randint(1, length - 1)
            last_name_length = length - first_name_length
            first_name = ''.join(random.choices(string.ascii_letters, k=first_name_length))
            last_name = ''.join(random.choices(string.ascii_letters, k=last_name_length))
            masked_number = f"{first_name}{separator}{last_name}"
        else:
            if len(account_number) == length:
                masked_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
            else:
                masked_number = account_number
    elif data_type.upper() == 'DECIMAL':
        precision, scale = length
        masked_number = random_decimal(precision, scale)
    elif data_type.upper() == 'DATE':
        masked_number = random_date()
    else:
        masked_number = account_number
    return masked_number



def mask_csv(input_file, output_file, columns_to_mask):
    df = pd.read_csv(input_file, sep='|')

    for column_name, (data_type, length, extra_params) in columns_to_mask.items():
        df[column_name] = df[column_name].apply(lambda x: mask_account_number(column_name, x, data_type, length, extra_params))

    df.to_csv(output_file, index=False, sep='|', line_terminator='\n')


if __name__ == "__main__":
    input_file = 'input.csv'
    output_file = 'output.csv'
    
    columns_to_mask = {
    'ACCT': ('VARCHAR', 10, None),
    'ACCTIN': ('VARCHAR', 10, None),
    'DECIMAL_COLUMN': ('DECIMAL', (5, 4), None),
    'DATE_COLUMN': ('DATE', None, None),
    'GENDER': ('VARCHAR', 1, {'allowed_values': ['F', 'M']}),
    'FIRST_NAME': ('VARCHAR', 8, None),
    'LAST_NAME': ('VARCHAR', 8, None),
    'FULL_NAME': ('VARCHAR', 16, {'separator': ' '})
    }



    mask_csv(input_file, output_file, columns_to_mask)
