import re
import os

def filter_requirements_file(input_filename='requirements1.txt', output_filename='filtered_requirements.txt'):
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    # Open the output file for writing
    with open(output_filename, 'w') as file:
        for line in lines:
            # Check if the line is in the format 'package==version'
            if re.match(r'^[\w\-_]+==[\d\.]+$', line.strip()):
                file.write(line)

    print(f"{output_filename} has been created with filtered package list.")



# Remove the old requirements.txt file
    if os.path.exists(input_filename):
        os.remove(input_filename)
    print(f"{input_filename} has been removed.")

# Filter the requirements.txt file
filter_requirements_file()