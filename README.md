# System_monitor_Alert
System usage monitor and remote management for Windows and Debian Linux.

A continuously running python script to monitor your system's performance and send alerts if the system overloads.

The default overload thresholds are:
1. CPU > 90%
2. RAM > 90%

When the system crosses either of the thresholds, an email is sent to the user periodically about the system performance. The email lists all the running programs and asks the email receiver if they want to safely close any of them. If yes, then the user can send the name of the program(s) through the email. The script safely closes the program(s).

The user email ID, the periodicity of sending the mail and the thresholds can be defined using the command line arguments during the initial execution of the script.