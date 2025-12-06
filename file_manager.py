import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

class FileManager:
    def read_csv(self, filename):
        path = os.path.join(DATA_DIR, filename)
        if not os.path.exists(path):
            return []
        with open(path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]

    def write_csv(self, filename, fieldnames, rows):
        path = os.path.join(DATA_DIR, filename)
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
