#!/bin/bash

# This is handled by the updated cleaner.py script

# Input and output file names
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <CSV_File_Name>"
    exit 1
fi
input_csv="$1"
output_csv="${input_csv%.csv}_with_attack_label_Ddos.csv"

dos2unix "$input_csv"

# adding the label column
# Needs to be fixed
awk -v OFS=',' 'NR==1{print $0,"label"} NR>1{print $0,0}' "$input_csv" > "$output_csv"

echo "Output saved: $output_csv"

