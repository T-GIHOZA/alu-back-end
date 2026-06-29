# API

This project is about using Python to get data from a REST API.

The scripts use the JSONPlaceholder API to get users and their todo tasks.
Some scripts print the data and others save it inside CSV or JSON files.

## Files

- `0-gather_data_from_an_API.py` - prints the todo progress of one employee.
- `1-export_to_CSV.py` - saves one employee's tasks in a CSV file.
- `2-export_to_JSON.py` - saves one employee's tasks in a JSON file.
- `3-dictionary_of_list_of_dictionaries.py` - saves all employees' tasks in a JSON file.

## Usage

Run the scripts with `python3`.

Example:

```bash
python3 0-gather_data_from_an_API.py 2
```

Export to CSV:

```bash
python3 1-export_to_CSV.py 2
```

This creates a file named:

```bash
2.csv
```

Export to JSON:

```bash
python3 2-export_to_JSON.py 2
```

This creates:

```bash
2.json
```

Export all employees:

```bash
python3 3-dictionary_of_list_of_dictionaries.py
```

This creates:

```bash
todo_all_employees.json
```

## API Used

```text
https://jsonplaceholder.typicode.com
```

## Requirements

- Python 3
- Use `urllib` to request the API
- Use `json` for JSON data
- Use `csv` for the CSV export
