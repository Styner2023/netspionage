# from core.updater import update
from prompt_toolkit import prompt
from core.scanner import scanner_choice

def menu_display():
    return ("""
 ENTER 1 - 5 TO SELECT OPTIONS

 1.  SCANNING                   Scan for IPs, nearby APs, ports, hosts, and more
 2.  RECONNAISSANCE             Gather  information  about nearby MAC addresses
 3.  DETECTION                  Detect for ARP Spoofing and SYN Flood attacks
 4.  UPDATE                     Update to the latest version of netspionage

 5. EXIT                        Exit from netspionage to your terminal
       """)

def prompt_display():  
    print(menu_display())
    while 1:
        user_input = prompt("\n netspionage >> ")
        if len(user_input)==0:
            print("\n")
            continue
        if user_input == "help" or user_input == "options" or user_input == "commands":
            print(menu_display())
            continue

        try:
            choice = int(user_input)
        except ValueError:
            print("\n Invalid Command! Type `help` to see all options")
            continue

        if choice == 1:
            while 1:
                print("\n 1. Network Scanner \n 2. WiFi Scanner \n 3. Port Scanner \n 4. Host Scanner\n")
                resp = input(" SCAN INPUT >> ")
                target = ""
                if resp == "1" or resp == "3":
                    target = input(" IP ADDRESS (Eg: 192.168.1.1/24) >> ")
                print(resp)
                break
            scanner_choice(resp, target)
            continue

        if choice == 2:
            while 1:
                print("\n 1. Choose MAC Address \n 2. Input MAC Address\n")
                resp = input(" RECON INPUT >> ")
                print(resp)
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        if choice == 3:
            while 1:
                print("\n 1. ARP Spoof Attack \n 2. SYN Attack\n")
                resp = input(" DETECT INPUT >> ")
                print(resp)
                break
            # shodan_host(ip)
            # censys_ip(ip)
            continue

        elif choice == 4:
            while 1:
                break
            # update()
            continue

        elif choice == 5:
            exit('\n Till next time!')

        else:
            pass

try:
    prompt_display()
except KeyboardInterrupt:
    quit('\n Till next time!')