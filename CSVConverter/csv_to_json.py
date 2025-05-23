import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        reader_csv = csv.DictReader(csv_file)
        data = list(reader_csv)

    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

    print(f"Conversión completada: {json_file_path}")

csv_file_path = "data.csv"
json_file_path = "data.json"
csv_to_json(csv_file_path, json_file_path)
