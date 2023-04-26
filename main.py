#! python3
#! usr/bin/dev python3

import time
import threading
import subprocess

# Global flag to indicate if download() is finished.
download_finished = False

def install(moduleName):
    """Call the download() and progressBar to install the third party
       modules.

    Args:
        moduleName (_str_): module to download.
    """
    global download_finished
    download_finished = False
    installObj = threading.Thread(target=download, args=[moduleName])
    installObj.start()
    while not download_finished:
        progressBar("Downloading")
    installObj.join()


def download(moduleName):
    """Download the necessary third-party modules from the internet.

    Args:
        moduleName (_str_): module to download.
    """
    global download_finished
    install_cmd = f"pip install {moduleName} -q"
    install = subprocess.run(install_cmd, shell=True)
    if install.returncode == 0:
        print(f"\nInstalled {moduleName}.")
    download_finished = True


def progressBar(text):
    """Run a nice progress indicator when a program is executing
       in another thread.

    Args:
        text (_str_): Display this string as the progress indicator.
    """
    # Hide cursor bar.
    global download_finished
    print("\033[?25l", end="")
    # \r to go back to beginning of the line.
    # \033[K to clear the text from the current position to the EOL.
    print("\r\033[K", end="")
    print(text, end="")
    for i in range(3):
        if download_finished == True:
            break
        print(".", end="", flush=True)
        time.sleep(1)
    # Show the cursor again.
    print("\033[?025h", end="")

def main():
    userinputs = initialise()
    monitoring(userinputs)
    print("Starting monitoring...")
    time.sleep(1)
    print()


def initialise():
    """Create a welcome screen when the script is executed.

    Returns:
        _str_: accept user's choice to decide what the script should do.
    """
    print("Initialising...")
    print()
    print("Welcome to System Monitor Alert.".center(66, "-"))
    print("------------------------------------------------------------------")
    time.sleep(1)
    print("A continuously running python script that monitors your system's")
    print("performance and sends alerts to your email if the system overloads.")
    print("------------------------------------------------------------------")
    time.sleep(1)
    print()

    email = pypi.inputEmail('Enter your email address through which the script \ncan communicate.')
    interval = pypi.inputInt('How often do you want to get informed about your \n \
                             system usage? Enter the duration in minutes.', min=1.0, max=1440)
    cpu = pypi.inputInt('Enter the CPU usage threshold above which you want to \
                         \nreceive messages(inclusive of the threshold).', min=50, max=100)
    ram = pypi.inputInt('Enter the RAM usage threshold above which you want to \
                         \nreceive messages(inclusive of the threshold).', min=50, max=100)
    print()
    
    return email, interval, cpu, ram


if __name__ == "__main__":
    # Automatically download and import third party python modules.
    while ModuleNotFoundError:
        try:
            # Import third-party modules here.
            import pyinputplus as pypi
        except ModuleNotFoundError as m:
            # Use \r because sometimes progressBar() finishes later
            # than download() and there will be dots in newline.
            print(f"\r{m.name} not found.")
            install(m.name)
        else:
            print("\rChecking for packages...Present")
            break
    main()
