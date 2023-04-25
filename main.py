#! python3
#! usr/bin/dev python3

import time
import threading
import subprocess

# Global flag to indicate if download() is finished.
download_finished = False
    
# Try importing third-party modules. If it errors out, install them.

def main():
    while ModuleNotFoundError:
        try:
            # Import third-party modules here.
            pass
        except ModuleNotFoundError as m:
            # Use \r because sometimes progressBar() finishes later
            # than download() and there will be dots in newline.
            print(f'\r{m.name} not found.') 
            install(m.name)
        else:
            print('\rChecking for packages...Present')
            break

def install(moduleName):
    global download_finished
    download_finished = False
    installObj = threading.Thread(target=download, args=[moduleName])
    installObj.start()
    while not download_finished:
        progressBar('Downloading')
    installObj.join()

def download(moduleName):
    global download_finished
    install_cmd = f'pip install {moduleName} -q'
    install = subprocess.run(install_cmd, shell=True)
    if install.returncode == 0:
        print(f'\nInstalled {moduleName}.')
    download_finished = True

def progressBar(text):
    # Hide cursor bar.
    global download_finished
    print('\033[?25l', end="")
    # \r to go back to beginning of the line.
    # \033[K to clear the text from the current position to the EOL.
    print('\r\033[K', end='')
    print(text, end='')
    for i in range(3):
        if download_finished == True:
            break
        print('.', end='', flush=True)
        time.sleep(1)
    # Show the cursor again.
    print('\033[?025h', end='')

if __name__ == '__main__':
    main()