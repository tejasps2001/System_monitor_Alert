# System_monitor_Alert
System usage monitor and remote management for Windows and Debian Linux.

A continuously running python script to monitor your system's performance and send alerts if the system overloads.

The default overload thresholds are:
1. CPU > 90%
2. RAM > 90%

When the system crosses either of the thresholds, an email is sent to the user periodically about the system performance. The email generates two lists: CPU-intensive an RAM-intensive programs running and asks the email receiver if they want to safely close any of them. If yes, then the user can send the name of the program(s) through the email. The script safely closes the program(s).

The user email ID, the periodicity of sending the mail and the thresholds can be defined using the command line arguments during the initial execution of the script.

Actions that can be performed by mailing to the script:
1. "Status": Status of the system. The CPU and RAM usage and 2 lists of CPU-intensive an RAM-intensive programs running.
2. "Close **\<Program(s) list\>**": Safely closes the programs specified. The programs names must be seperated by commas. It replies to this mail about the status of the closure operation.
3. "Sleep **\<number of minutes\>"**: Stop the periodic mails to the specified number of minutes. Pinging "Status" stil works.
4. "Stop sleep": Abort the sleep and starts the mailing again.
