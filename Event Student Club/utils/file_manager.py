import csv
import os

class FileManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(FileManager, cls).__new__(cls)
        return cls._instance

    def read_csv(self, filename):
        if not os.path.exists(filename):
            return []

        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def write_csv(self, filename, fieldnames, rows):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
