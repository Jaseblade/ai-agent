import os


def write_file(working_directory, file_path, content):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))
    
    # will be True or False
    valid_target_file_path = os.path.commonpath([working_dir_path, target_file_path]) == working_dir_path

    if not valid_target_file_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    # ensure all parent directories exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    try:
        with open(file_path, "w") as file:
            file.write(content)
    
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {e}'
    