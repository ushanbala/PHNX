import os
import re

# Define a mapping of custom commands to Python equivalents
command_map = {
    'String': '',  # To handle variable declarations
    'alert': 'tk.alert',  # Add the alert function mapping
}

# Function to replace 'console()' with 'print()' and format variable declarations
def convert_phnx_to_py(input_file, output_file):
    with open(input_file, 'r') as f:
        phnx_content = f.read()
    # Replace 'console('hello');' with 'print('hello')'

    py_content = phnx_content

    if 'terminal(' in py_content:
        py_content = "from phnxs import terminal\n" + \
                    py_content
    #alert
    if 'alert(' in py_content:
        py_content = "from phnxs import tk\n" + \
                    py_content
    #web app functionality
    if 'web_app(' in py_content:
        py_content = "from phnxs import web_app\n" + \
                    py_content
    if 'talk(' in py_content:
        py_content = "from phnxs import talk\n" + \
                    py_content
    py_content = "import sys\n" + \
                    "import os\n" + \
                    "script_dir = os.path.dirname(os.path.abspath(__file__))\n" + \
                    "project_root = os.path.abspath(os.path.join(script_dir, '..'))\n" + \
                    "sys.path.append(project_root)\n" + \
                    py_content
    # Replace 'String var xmas = "Hello";' with 'xmas = "Hello"'
    #String vars
    py_content = re.sub(r'String var (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'String let (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'String v (\w+) =', r'\1 =', py_content)
    
    #int vars
    py_content = re.sub(r'int var (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'int let (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'int v (\w+) =', r'\1 =', py_content)
    
    #double vars
    py_content = re.sub(r'double var (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'double let (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'double v (\w+) =', r'\1 =', py_content)

    #char vars
    py_content = re.sub(r'char var (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'char let (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'char v (\w+) =', r'\1 =', py_content)

    #boolean vars
    py_content = re.sub(r'bool var (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'bool let (\w+) =', r'\1 =', py_content)
    py_content = re.sub(r'bool v (\w+) =', r'\1 =', py_content)

    # Remove extra whitespace before variable assignments and semicolons
    py_content = py_content.replace(" =", "=").replace(";", "")

    #If else elif
    py_content = py_content.replace("if", "if").replace("elif", "elif").replace("else", "else").replace("{",":").replace("}","")
    
    #public vars
    py_content = py_content.replace("public", "global").replace("String","")
    py_content = py_content.replace("int","")
    #void declare
    py_content = py_content.replace("void", "def")

    #import statement
    py_content = py_content.replace("give_me", "import")

    #alert
    py_content = py_content.replace("alert(", "tk.alert(")

    #comments
    py_content = py_content.replace("btw", "#")

    #terminal command 
    py_content = py_content.replace("terminal(", "terminal.terminal(")

    #web_app function
    py_content = py_content.replace("web_app(", "web_app.web_app(")

    #talk function
    py_content = py_content.replace("talk(", "talk.talk(")

    # Define the console function to match the PHNX code at the beginning
    py_content = "def console(arg):\n    print(arg)\n\n" + py_content

    #intext variable declare
    py_content = py_content.replace("_+", "{").replace("+_", "}")

    #sml to <
    py_content = py_content.replace("sml", "<")

    #grt to >
    py_content = py_content.replace("grt", ">")

    #parsing to int
    py_content = py_content.replace("toINT", "int")




    with open(output_file, 'w') as f:
        f.write(py_content)

