#!/bin/bash

output_csv="combined_testset.csv"

# Check if at least one CSV file name is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <CSV_File_Name1> [<CSV_File_Name2> ...]"
    exit 1
fi

# Initialize the output file with the header and the new 'label' column
awk -v OFS=',' 'NR==1{print $0,"label"; exit}' "$1" > "$output_csv"

# Process each CSV file
for input_csv in "$@"
do
    # Check if the file exists
    if [ ! -f "$input_csv" ]; then
        echo "File not found: $input_csv"
        continue
    fi

    # Skip the header and add the 'label' column with default value 0
    awk -v OFS=',' 'NR>1{print $0,0}' "$input_csv" >> "$output_csv"
done

echo "Combined output saved to: $output_csv"
