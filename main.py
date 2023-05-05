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
    # Get inputs from the user.
    user1 = userInputs()
    time.sleep(1)
    print()
    print("Starting monitoring...")

class userInputs:
    """Represents the set of user inputs for a single managed system.
    """
    def __init__(self):
        """Create a welcome screen when the script is executed.

            Returns:
            tuple: all user inputs: email ID, interval and thresholds.
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

        email = pypi.inputEmail('\033[34mEnter your email address through which the script can communicate.\033[37m\n')

        # Dictionary to convert user choice of interval into minutes.
        intervalConversion = {1: 1, 2: 10, 3: 60, 4: 1440}
        print('\033[34mHow often do you want to get informed about your system usage?\033[37m\n')
        print('1. 1 min')
        print('2. 10 min')
        print('3. 60 min')
        print('4. 24 hours')
        print('5. Custom')
        interval = pypi.inputInt('\033[34mEnter one option(1-5) \033[37m', min=1, max=5)
        if not interval == 5:
            interval = intervalConversion[interval]
        else:
            interval = pypi.inputInt('\033[34mEnter the duration in minutes. \033[37m', min=1.0, max=1440)

        cpu = pypi.inputInt('\033[34mEnter the CPU usage threshold(in %) above which you want to \
                            \nreceive messages(inclusive of the threshold). \033[37m', min=50, max=100)
        ram = pypi.inputInt('\033[34mEnter the RAM usage threshold(in %) above which you want to \
                            \nreceive messages(inclusive of the threshold). \033[37m', min=50, max=100)
        print()

        self.email = email
        self.interval = interval
        self.cpu_threshold = cpu
        self.ram_threshold = ram

# def monitoring(parameters):
    


if __name__ == "__main__":
    # Automatically download and import third party python modules.
    while ModuleNotFoundError:
        try:
            # Import third-party modules here.
            import psutil
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
