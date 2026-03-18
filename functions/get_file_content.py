import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        #get absolute path of working_directory
        working_dir_abs = os.path.abspath(working_directory)
        #construct full path to target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
        # check if target_dir is within absolute working_directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir == False:                                     
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        open_file = open(file_path)
        content = open_file.read(MAX_CHARS)
        content_plus = open_file.read(MAX_CHARS + 1)

        if content_plus > content:
            content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    except Exception as e:
        return f"Error: {e}"