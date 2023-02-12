import sys
import os
import argparse

combined_set = set()

parser = argparse.ArgumentParser()
parser.add_argument("-f", '--file', type=argparse.FileType('r'), nargs='+')
parser.add_argument('-o', '--output')

args = parser.parse_args()



for filename in args.file:
  try:
    s = set(filename)
    combined_set.update(s)
  except FileNotFoundError as e:
    print(e)
    print("Please enter a valid filename")


combined_set = ''.join(combined_set)

# write the combined file with no duplicate lines 
output_filename = args.output or "duplicate_free_file.txt"

with open(output_filename, "w") as new_file: 
  new_file.write(combined_set)
