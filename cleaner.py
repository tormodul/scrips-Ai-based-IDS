import json
import csv

# Define the CSV output file name
csv_file_name = 'network_events2.csv'

# Define the fields you want to extract from the JSON data
fields = ['sa', 'da', 'pr', 'sp', 'dp', 'bytes_out', 'num_pkts_out', 'bytes_in', 'num_pkts_in', 'time_start', 'time_end', 'entropy', 'total_entropy']

# Open the JSON file and the CSV file for writing
with open('data1.json', 'r') as json_file, open(csv_file_name, 'w', newline='') as csv_file:
    # Create the CSV writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=fields)
    
    # Write the header row to the CSV file
    csv_writer.writeheader()
    
    # Skip the first line (configuration data)
    next(json_file)
    
    # Iterate over each line in the JSON file
    for line in json_file:
        # Load the JSON object from the current line
        event = json.loads(line)
        
        # Check if the required fields are in the JSON object
        if all(field in event for field in fields):
            # Extract the data and write it to the CSV file
            csv_writer.writerow({field: event[field] for field in fields})
        else:
            # Handle cases where not all fields are present, if necessary
            pass  # For now, just skip any entries that don't match the expected format

print(f"Data has been successfully written to {csv_file_name}")

