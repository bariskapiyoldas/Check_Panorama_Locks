import getpass
import sys
import paramiko  ###SSH LIBRARY###
from paramiko_expect import \
    SSHClientInteraction  ###TAKES AN ACTION ACCORDING TO INPUT CODE AND PROVIDES STOP THE CODE (expect)###
from re import search

def checkservice(Username,Password):
    # Defined Values
    palo_prompt = ".*> "
    lock_prompt = ".*shared"
    # SSH
    SSH = paramiko.SSHClient()
    SSH.load_system_host_keys()
    SSH.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    # Output File
    file = open("Check_Panorama_Locks.txt", "a")
    # Panorama's
    Panoramas = {"ip address": "hostname"
                 }

    for host in Panoramas:
        print(host)

        SSH.connect(hostname=host, username=Username, password=Password, port=22)
        with SSHClientInteraction(SSH) as command:
            command.expect(palo_prompt, timeout=15)

            if palo_prompt == command.last_match:
                print(host, "###########Connection to Palo was established.###########")

                command.send("show commit-locks")
                command.expect(palo_prompt)
                locker = command.current_output_clean
                locker = locker.splitlines()
                command.send("exit")
                locked_by_line = locker[4]
                locked_by_and_time = locked_by_line[8:70]

                if search(lock_prompt, locked_by_line):
                    print(locked_by_and_time)
                    print("Locked")
                    file.write(str(Panoramas[host])+ " : " + "LOCKED BY" + " => " + locked_by_and_time + "\n")
                else:
                    print("Unlocked")
                    file.write(str(Panoramas[host]) + " : " + "UNLOCKED\n")

            else:
                print(
                    "##########Connection to Palo was NOT established, Please check your network connection and try again.###########")
                file.write(host + " : " + "Please check your User and Pass connection!!!\n")

if __name__ == '__main__':

    print('\n' + '#' * 180)
    print('\nThis tool is prepared to detect forgotten Locks in Panorama.'
          '\nAfter running the tool, it will create a .txt file named "Check_Panorama_Locks" '
          'in the folder with the .exe file, you can see the results here.\n')
    print("Important Reminder: You need to delete the .txt file before running each time!! ")
    print('\n' + '#' * 180)
#input variables
    Username = input("Please Enter Your Username:")
    Password = getpass.getpass(prompt="Please Enter Your Password:")

    print('\n' + '#' * 180)

    checkservice(Username,Password)

sys.exit()

##barka##