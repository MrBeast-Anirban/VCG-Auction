import csv
import json

# Function to read bids from CSV file
def read_bids_csv(file_path):
    bidders = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            bidders.append({'slot': row['slot'], 'value': int(row['value'])})
    return bidders

# Function to read bids from JSON file
def read_bids_json(file_path):
    with open(file_path, 'r') as file:
        bidders = json.load(file)
    return bidders
