import manage_dependencies
import compiler
import os
import subprocess
import sys
# Install dependencies and generate lock file
manage_dependencies.install_dependencies()
manage_dependencies.generate_lock_file()

# Define the function to clean the contents of the 'build' folder
def clean_build_folder():
    build_folder = 'build'
    for filename in os.listdir(build_folder):
        file_path = os.path.join(build_folder, filename)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error deleting {file_path}: {e}")

#restrating the server
def restart_script():
    python = sys.executable
    os.execl(python, python, *sys.argv)

# Continuous loop to ask the user for actions
while True:
    user_input = input("Press 'r' to run the build, 'x' to rebuild ,  'q' to quit, 'c' to clean build: ")
    if user_input.lower() == 'r':
        # Specify the path to the 'lib' folder
        lib_folder = 'lib'

        # Loop through the ".phnx" files in the 'lib' folder and convert them
        for filename in os.listdir(lib_folder):
            if filename.endswith('.phnx'):
                input_file = os.path.join(lib_folder, filename)
                output_file = os.path.join('build', os.path.splitext(filename)[0] + '.py')
                compiler.convert_phnx_to_py(input_file, output_file)

        # Specify the path to the 'app.py' file in the 'build' folder
        app_py_path = os.path.join('build', 'app.py')

        if os.path.isfile(app_py_path):
            # Run 'app.py' as a separate process
            subprocess.run(['python3', app_py_path])  # Modify 'python' if needed (e.g., 'python3' on some systems)
        else:
            print("Error: 'app.py' not found in the 'build' folder.")
    elif user_input.lower() == 'q':
        break
    elif user_input.lower() == 'c':
        clean_build_folder()
        print("Build folder cleaned.")
    elif user_input == 'x':
        print('Restarting the server')
        restart_script()
    else:
        print("Invalid input. Press 'r' to run the build, 'x' to rebuild, 'q' to quit, or 'c' to clean build.")
