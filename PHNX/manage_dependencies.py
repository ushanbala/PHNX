import subprocess

def install_dependencies():
    print('PHNX started')
    print('Started installing dependencies')
    # Install dependencies from neon.xphnx
    subprocess.call(['pip', 'install', 'pip-tools'])
    subprocess.call(['pip', 'install', '-r', 'neon.xphnx'])

def generate_lock_file():
    # Generate neon_lock.xphnx
    subprocess.call(['pip-compile', '--generate-hashes', '-o', 'neon_lock.xphnx', 'neon.xphnx'])

if __name__ == "__main__":
    install_dependencies()
    generate_lock_file()
