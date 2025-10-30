import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory_abs_path = os.path.abspath(working_directory)
        file_abs_path = os.path.normpath(os.path.join(working_directory_abs_path, file_path))

        if not file_abs_path.startswith(working_directory_abs_path):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_abs_path):
            return f'Error: File "{file_path}" not found.'
        if not file_abs_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'

        old_cwd_abs_path = os.path.abspath(os.getcwd())
        os.chdir(working_directory_abs_path)
        response = subprocess.run(["python", file_path, *args], timeout=30, capture_output=True)
        os.chdir(old_cwd_abs_path)

        output = []
        if response.stdout or response.stderr:
            output.append(f"STDOUT: {(response.stdout.decode("utf-8"))}")
            output.append(f"STDERR: {response.stderr.decode("utf-8")}")
        if response.returncode != 0:
            output.append(f"Process exited with code {response.returncode}")
        if not output:
            output.append("No output produced")

        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
