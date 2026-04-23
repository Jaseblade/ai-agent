import os
from google.genai import types


def write_file(working_directory, file_path, content):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))

    # will be True or False
    valid_target_file_path = (
        os.path.commonpath([working_dir_path, target_file_path]) == working_dir_path
    )

    if not valid_target_file_path:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    if os.path.isdir(target_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    # ensure all parent directories exist
    os.makedirs(os.path.dirname(target_file_path), exist_ok=True)

    try:
        with open(target_file_path, "w") as file:
            file.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write (or overwrite) content to the file specified within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of file, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="String-based content to be written to the specified file",
            ),
        },
        required=["file_path", "content"],
    ),
)
