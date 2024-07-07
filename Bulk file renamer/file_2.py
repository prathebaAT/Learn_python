import os

def bulk_rename(directory, prefix, start_number=1):
    # Get the list of files in the directory
    files = os.listdir(directory)
    files.sort()  # Sort files if you want to rename them in a specific order

    # Iterate over the files and rename them
    for index, filename in enumerate(files):
        # Define the new file name
        new_name = f"{prefix}_{start_number + index}{os.path.splitext(filename)[1]}"
        
        # Get the full file path
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} -> {new_file}")

# Define the directory, prefix, and starting number
directory = "C:/Users/atb/Documents/Testcheck/"
prefix = input("Enter the prefix name :")
start_number = int(input("Enter the starting sequence :"))

# Call the function to rename files
bulk_rename(directory, prefix, start_number)
