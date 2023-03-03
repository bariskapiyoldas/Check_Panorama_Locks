# Check Panorama Locks

This Python script is designed to detect forgotten locks in Panorama devices. It utilizes the SSH library paramiko and the library paramiko_expect to execute a show commit-locks command on a list of Panorama devices and then saves the results to a text file named "Check_Panorama_Locks.txt" in the same directory as the script.


# Requirements

Python 3.x

paramiko library

paramiko_expect library


# Usage

Clone the repository to your local machine.
Install required libraries via pip install -r requirements.txt.
Update the Panoramas dictionary in the script with your own devices' IP addresses and hostnames.
Run the script using the command python check_panorama_locks.py.
Enter your username and password for SSH authentication.
The results will be saved to a text file named "Check_Panorama_Locks.txt" in the same directory as the script.

**Note:** You need to delete the "Check_Panorama_Locks.txt" file before running the script each time.

# Disclaimer

This script is provided as-is and without warranty. Use at your own risk.
