import csv

def read_csv_file(file_path):
    id_number_map = {}
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header row
        for row in reader:
            number, id = row
            if id in id_number_map:
                id_number_map[id].append(number)
            else:
                id_number_map[id] = [number]
    return id_number_map

csv_file_path = 'your_csv_file_path.csv'
id_number_map = read_csv_file(csv_file_path)


import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_bdd_before_scenario(request, feature, scenario):
    # Modify the scenario name based on the ID
    id = scenario.name.split('_')[0]
    if id in id_number_map:
        numbers = ','.join(id_number_map[id])
        scenario.name = f"{numbers}_to be done"

    # Execute the hook
    outcome = yield
