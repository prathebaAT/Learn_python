import os
import re

def search_and_replace(directory, search_pattern, replace_pattern, file_extension=None):
    # """
    # Search for specific files in a directory and replace part of their names.

    # :param directory: Directory to search for files
    # :param search_pattern: Pattern to search for in file names
    # :param replace_pattern: Pattern to replace the search pattern with
    # :param file_extension: Only consider files with this extension (optional)
    # """
    # Compile the search pattern into a regex object
    search_regex = re.compile(search_pattern)
    
    # Iterate over the files in the directory
    for filename in os.listdir(directory):
        # Skip files that do not match the specified extension (if any)
        if file_extension and not filename.endswith(file_extension):
            continue
        
        # Check if the file name matches the search pattern
        if search_regex.search(filename):
            # Create the new file name by replacing the search pattern with the replace pattern
            new_filename = search_regex.sub(replace_pattern, filename)
            
            # Get the full paths for the old and new file names
            old_file = os.path.join(directory, filename)
            new_file = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file, new_file)
            print(f"Renamed: {old_file} -> {new_file}")


directory = "" # directory name
search_word = input("enter the search word:")
search_pattern = fr"{search_word}"  
replace_pattern = input("Enter the replace word :")  
file_extension = input("Enter the extension with dot :")  

#
search_and_replace(directory, search_pattern, replace_pattern, file_extension)
