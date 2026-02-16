import os
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