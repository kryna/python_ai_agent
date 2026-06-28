# functions/run_python_file.py

import os
import subprocess


def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        command.extend(args)

        output_string = ""

        completed_process = subprocess.run(
            command, text=True, capture_output=True, timeout=30
        )

        if completed_process.returncode != 0:
            output_string += f"Process exited with code {completed_process.returncode}\n"

        if completed_process.stdout is None and completed_process.stderr is None:
            output_string += "No output produced\n"

        if completed_process.stdout is not None:
            output_string += f"STDOUT: {completed_process.stdout}"
        if completed_process.stderr is not None:
            output_string += f"STDERR: {completed_process.stderr}"

        return output_string

    except Exception as e:
        return f"Error: executing Python file: {e}"
