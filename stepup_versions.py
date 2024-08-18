import subprocess

def create_requirements_file(filename='requirements1.txt'):
    # Run 'pip freeze' to get the list of installed packages and their versions
    result = subprocess.run(['pip', 'freeze'], capture_output=True, text=True)
    
    if result.returncode != 0:
        print("Error running pip freeze")
        return

    # Write the output to the requirements file
    with open(filename, 'w') as file:
        file.write(result.stdout)
    
    print(f"{filename} has been created with the current packages.")

# Create the requirements.txt file
create_requirements_file()
