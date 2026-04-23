import os
from config import MAX_CHARS
from google.genai import types


# print(MAX_CHARS)
def get_file_content(working_directory, file_path):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))

    # will be True or False
    valid_target_file_path = (
        os.path.commonpath([working_dir_path, target_file_path]) == working_dir_path
    )

    if not valid_target_file_path:
        return f'Error: Cannot list "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(target_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

            if f.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

        return file_content_string
    except Exception as e:
        return f"Error: {e}"


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Print out the contents of a file in a directory relative to the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of file, relative to the working directory",
            ),
        },
        required=["file_path"],
    ),
)
