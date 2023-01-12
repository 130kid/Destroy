import colorama
from colorama import Fore , Back
import os
import pyfiglet









if __name__ == "__main__":
    print(Fore.YELLOW + pyfiglet.figlet_format("Destroy . py"))
    print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  Information Gathering")
    print(Fore.GREEN + "[ " + Fore.YELLOW + "2" + Fore.GREEN + " ]" + Fore.YELLOW + "  Password Cracking Tools")
    print(Fore.GREEN + "[ " + Fore.YELLOW + "3" + Fore.GREEN + " ]" + Fore.YELLOW + "  Network Hacking Tools")
    print(Fore.GREEN + "[ " + Fore.YELLOW + "4" + Fore.GREEN + " ]" + Fore.YELLOW + "  Spamming Tools")
    print(Fore.GREEN + "[ " + Fore.YELLOW + "5" + Fore.GREEN + " ]" + Fore.YELLOW + "  Web Exploitation Tools")
    print(Fore.GREEN + "[ " + Fore.YELLOW + "6" + Fore.GREEN + " ]" + Fore.YELLOW + "  Reverse & Backdoor")
    n = int(input(Fore.GREEN + "[ " + Fore.YELLOW + "/ " + Fore.GREEN + "]" + Fore.YELLOW + "  Choice : "))

    if n == 1:
      os.system('cls' if os.name=='nt' else 'clear')
      print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  Domain To Ip")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "2" + Fore.GREEN + " ]" + Fore.YELLOW + "  Host Scan")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "3" + Fore.GREEN + " ]" + Fore.YELLOW + "  Sql Scan")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "4" + Fore.GREEN + " ]" + Fore.YELLOW + "  Vulnerability Scan")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "5" + Fore.GREEN + " ]" + Fore.YELLOW + "  Xss scan")
    if n == 2:
      os.system('cls' if os.name=='nt' else 'clear')
      print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  Password Cracker")
    if n == 3:
      os.system('cls' if os.name=='nt' else 'clear')
      print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  DDOS (Tcp Flood)")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "2" + Fore.GREEN + " ]" + Fore.YELLOW + "  Wifi Hacking")
    if n == 4:
      os.system('cls' if os.name=='nt' else 'clear')
      print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  Twitter Post")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "2" + Fore.GREEN + " ]" + Fore.YELLOW + "  Youtube")
    if n == 5:
      os.system('cls' if os.name=='nt' else 'clear')
      print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  File Upload")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "2" + Fore.GREEN + " ]" + Fore.YELLOW + "  shell")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "3" + Fore.GREEN + " ]" + Fore.YELLOW + "  sql")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "4" + Fore.GREEN + " ]" + Fore.YELLOW + "  xss")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "5" + Fore.GREEN + " ]" + Fore.YELLOW + "  commix")
    if n == 6:
      os.system('cls' if os.name=='nt' else 'clear')
      print(Fore.GREEN + "[ " + Fore.YELLOW + "1" + Fore.GREEN + " ]" + Fore.YELLOW + "  Reverse shell")
      print(Fore.GREEN + "[ " + Fore.YELLOW + "2" + Fore.GREEN + " ]" + Fore.YELLOW + "  Remote Attack")
