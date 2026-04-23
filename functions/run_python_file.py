import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    working_dir_path = os.path.abspath(working_directory)
    target_file_path = os.path.normpath(os.path.join(working_dir_path, file_path))

    # will be True or False
    valid_target_file_path = (
        os.path.commonpath([working_dir_path, target_file_path]) == working_dir_path
    )

    if not valid_target_file_path:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file_path):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if not target_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file_path]

    if args:
        command.extend(args)

    try:
        completed_subprocess = subprocess.run(
            command, capture_output=True, text=True, timeout=30
        )

        output_string = ""

        if completed_subprocess.returncode != 0:
            output_string += (
                f"Process exited with code {completed_subprocess.returncode}"
            )

        if (completed_subprocess.stderr is None) and (
            completed_subprocess.stdout is None
        ):
            output_string += "No output produced"
        else:
            output_string += f"STDOUT: {completed_subprocess.stdout} STDERR: {completed_subprocess.stderr}"

        return output_string
    except Exception as e:
        return f"Error: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run the specified python file, found within the working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File path of file, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Additional arguments provided to the python file to be called",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],
    ),
)
