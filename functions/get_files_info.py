import os
from google.genai import types


def get_files_info(working_directory, directory="."):

    working_dir_path = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_path, directory))

    # will be True or False
    valid_target_dir = (
        os.path.commonpath([working_dir_path, target_dir]) == working_dir_path
    )

    if not valid_target_dir:
        return f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'    Error: "{directory}" is not a directory'

    file_info_str = ""

    for item in os.scandir(target_dir):
        try:
            if file_info_str:
                file_info_str += "\n"

            file_info_str += f"  - {item.name}: file_size={item.stat().st_size} bytes, is_dir={item.is_dir()}"

        except Exception as e:
            return f"    Error: {e}"

    return file_info_str


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
