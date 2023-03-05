#!/usr/bin/python

import os

# define the file paths and constants
input_file = 'fmk/new-firmware.bin'
output_file = 'fmk/new-firmware1.bin'
log_file = 'fmk/logs/binwalk.log'
byte_to_insert = b'\x4c'
bytes_to_remove = 28
bytes_to_keep = -27

# read the input file and modify the firmware data
with open(input_file, 'rb') as f:
    image_data = f.read()
    
modified_data = image_data[:-bytes_to_remove] + byte_to_insert + image_data[bytes_to_keep:]

# write the modified firmware data to the output file
with open(output_file, 'wb+') as f:
    f.write(modified_data)

# calculate the CRC of the modified firmware data and log the result
os.system("src/crcalc/crcalc " + output_file + " " + log_file)

