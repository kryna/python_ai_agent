# functions/get_files_info.py

import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        header = None
        message = None
        if directory == ".":
            header = "Result for current directory:"
        else:
            header = f"Result for {directory} directory:"
        if not valid_target_dir:
            message = f'    Error: Cannot list "{directory}" as it is outside the permitted working directory'
            return "\n".join([header, message])

        if not os.path.isdir(target_dir):
            message = f'    Error: "{directory}" is not a directory'
            return "\n".join([header, message])

        dir_contents = []
        for file in os.listdir(target_dir):
            dir_contents.append(f"- {file}: file_size={os.path.getsize(os.path.normpath(os.path.join(target_dir, file)))} bytes, is_dir={os.path.isdir(os.path.normpath(os.path.join(target_dir, file)))}")
        return "\n".join([header, *dir_contents])

    except Exception as e:
        return f'Error: {e}'
