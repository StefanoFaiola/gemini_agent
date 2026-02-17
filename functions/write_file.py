import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write content to files in a specified path relative to the working directory and save it.",
    parameters=types.Schema(
        required=["filepath", "content"],
        type=types.Type.OBJECT,
        properties={
            "filepath": types.Schema(
                type=types.Type.STRING,
                description="File path to write content to a file, relative to the working directory (default is the working directory itself)",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write into the file, specified from filepath",
            ),
        },
    ),
)




def write_file(working_directory, filepath, content):
    try:
        wd_abs = (os.path.abspath(working_directory))
        target_dir = os.path.normpath(os.path.join(wd_abs, filepath))

        # Will be True or False
        valid_target_dir = os.path.commonpath([wd_abs, target_dir]) == wd_abs

        if not valid_target_dir:
            return f'Error: Cannot write to "{filepath}" as it is outside the permitted working directory'
        if os.path.isdir(filepath):
            return f'Error: Cannot write to "{filepath}" as it is a directory'
        
        os.makedirs(os.path.dirname(target_dir), exist_ok=True)

        with open(target_dir, "w") as wf:
            wf.write(content)
        return (
            f'Successfully wrote to "{filepath}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error writing files: {e}"