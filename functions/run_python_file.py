import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        wd_abs = (os.path.abspath(working_directory))
        target_dir = os.path.normpath(os.path.join(wd_abs, file_path))

        # Will be True or False
        valid_target_dir = os.path.commonpath([wd_abs, target_dir]) == wd_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", target_dir]
        if args:
            command.extend(args)

        result = subprocess.run(
            command, 
            cwd = wd_abs,
            capture_output = True, 
            text = True, 
            timeout = 30
            )

        output = []
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            output.append("No output produced")
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        return "\n".join(output)
    
    except Exception as e:
        return f"Error executing files: {e}"