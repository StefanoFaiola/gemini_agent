import os
from config import MAX_CHARS

from google.genai import types

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Retrieves the content (at most {MAX_CHARS} characters) of a specified file within the working directory",
    parameters=types.Schema(
        required=["filepath"],
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to read, relative to the working directory",
            ),
        },
    ),
)


def get_file_content(working_directory, filepath):
    try:
        wd_abs = (os.path.abspath(working_directory))
        target_dir = os.path.normpath(os.path.join(wd_abs, filepath))

        # Will be True or False
        valid_target_dir = os.path.commonpath([wd_abs, target_dir]) == wd_abs

        if not valid_target_dir:
            return f'Error: Cannot list "{filepath}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{filepath}" is not a file'
        with open(target_dir, "r") as f:
            content = f.read(MAX_CHARS)
            if f.read(1):
                content += f'[...File "{filepath}" truncated at {MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error listing files: {e}"
    