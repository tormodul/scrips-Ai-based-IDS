import json
import csv
import socket
import struct

# Function to convert an IP address from string to an integer
def ip_to_int(ip):
    if ip and isinstance(ip, str):
        try:
            return struct.unpack("!I", socket.inet_aton(ip))[0]
        except socket.error:
            # Handles end cases
            return 0
    else:
        return 0

csv_file_name = 'Ddos2TCP_transformed.csv'

# Open the JSON file and the CSV file for writing
with open('Ddos2TCP.json', 'r') as json_file, open(csv_file_name, 'w', newline='') as csv_file:
    fieldnames = ['avg_ipt', 'bytes_in', 'bytes_out', 'dest_ip', 'dest_port', 'entropy', 'proto',
                  'src_ip', 'src_port', 'time_end', 'time_start', 'total_entropy', 'label', 'duration']
    
    # Create the CSV writer object
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write the header row to the CSV file
    csv_writer.writeheader()
    
    # Skip the first line (configuration data)
    next(json_file)
    
    for line in json_file:
        event = json.loads(line)
        
        row = {
            'bytes_in': event.get('bytes_in', 0),
            'bytes_out': event.get('bytes_out', 0),
            'dest_ip': ip_to_int(event.get('da', '')),  # Convert destination IP
            'dest_port': event.get('dp', 0),
            'entropy': event.get('entropy', 0.0),
            'proto': int(event.get('pr', 0)),
            'src_ip': ip_to_int(event.get('sa', '')),  # Convert source IP
            'src_port': event.get('sp', 0),
            'time_end': int(event.get('time_end', 0)),
            'time_start': int(event.get('time_start', 0)),
            'total_entropy': event.get('total_entropy', 0.0),
            'label': 0,  # Default value for label, to be updated in another script
            'duration': event.get('time_end', 0) - event.get('time_start', 0)
        }
        
        # Calculate avg_ipt (Average Inter-Packet Time) if packets information is available
        packets = event.get('packets', [])
        if packets:
            total_ipt = sum(packet.get('ipt', 0) for packet in packets)
            row['avg_ipt'] = total_ipt / len(packets) if len(packets) > 0 else 0.0
        else:
            row['avg_ipt'] = 0.0
        
        csv_writer.writerow(row)

print(f"Data has been successfully written to {csv_file_name}")
