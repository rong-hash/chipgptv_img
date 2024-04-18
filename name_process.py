import os

# Directory containing the files
directory = 'no_port'

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.startswith("Copy of "):
        # Construct the old file path
        old_file = os.path.join(directory, filename)

        # Create the new file name by removing the prefix "Copy of "
        new_filename = filename.replace("Copy of ", "")

        # Construct the new file path
        new_file = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed "{old_file}" to "{new_file}"')

