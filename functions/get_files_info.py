import os

def get_files_info(working_directory, directory="."):
    output=""
    if directory == ".":
        output = "Results for current directory:\n"
    else: 
        output = f"Results for '{directory}' directory:\n"
    try:
        #get absolute path of working_directory
        working_dir_abs = os.path.abspath(working_directory)
        #construct full path to target directory
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        # check if target_dir is within absolute working_directory
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if valid_target_dir == False:                                     
            return f'{output} Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'{output} Error: "{directory}" is not a directory'
        target_dir_contents = os.listdir(target_dir)
        
        for item in target_dir_contents:
            item_path = os.path.join(target_dir, item)
            name = item
            file_size = os.path.getsize(item_path)
            is_dir = os.path.isdir(item_path)
            output += f"- {name}: file_size={file_size} bytes, is_dir={is_dir}\n"
        return output
    except Exception as e:
        return f"Error: {e}"