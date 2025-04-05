import subprocess

def terminal(command):
    try:
        completed_process = subprocess.run(command, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = completed_process.stdout
        stderr = completed_process.stderr
        return (stdout, stderr)
    except Exception as e:
        return (str(e), None)
