# Versoin: 1.0
# Author: evilfeonix
# Name: wordlist generator
# Date: 16 - DECEMBER - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


######  Note that the creators of this tool are not responsible for any misuse or damage caused by its usage!.
######  Always use this for legal activity (responsibly).


from datetime import datetime
import os, sys, time, socket, argparse
from itertools import permutations, combinations


stop="\033[0m"
red="\033[91;1m"
blue="\033[94;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"


notice=f"{blue}[{stop}!{blue}]{red} "
success=f"{purple}[{stop}√{purple}]{green} "
first= f"{green}[{stop}01{green}]{purple} "
second= f"{green}[{stop}02{green}]{purple} "


def internet():
    try:
        s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    

def banner():
    logo=f"""{green}
  (^_^)          {stop}  Coded by - evilfeonix  {green}          (^_^){purple} 
===========================================================
=  {green}  __        __            _        ____      v[{stop}1.0{green}]   {purple} =
=  {green}  \ \      / /__  _ __ __| |      / ___| ___ _ __     {purple} =
=  {red}   \ \ /\ / / _ \| '__/ _` |_____| |  _ / _ \ '_ \\    {purple} =
=  {red}    \ V  V / (_) | | | (_| |_____| |_| |  __/ | | |   {purple} =
=  {green}     \_/\_/ \___/|_|  \__,_|      \____|\___|_| |_|   {purple} =
=  {green}                 {stop} www.evilfeonix.com                  {purple} =
==========================================================={stop}"""
    return logo


def message(iniList):
    os.system("clear || cls")
    print(banner())
    
    if not len(passwords) >=1:
        time.sleep(2)
        print(f"{notice}Ops!,{stop}")
        print(f"{notice}Look like `{iniList}` file is empty.{stop}")
        print(f"{notice}You gotta provide atlease 2 words, in order to generate password.{stop}")
        os.sys.exit()


    file = f"wordlist {datetime.now()}"
    file = file.replace(" ", "_")
    file = file.replace(":", "-")

    dir = os.path.join('WordLists')
    if not os.path.exists(dir):
        os.makedirs(dir)

    location = os.path.join(dir, f"{file}.txt")
    with open(location, "w") as pswd:
        for password in passwords:
            pswd.write("".join(password) + "\n")
        
    
    time.sleep(1)
    print(f"{success}Congratulation!,{stop}")
    print(f"{success}{len(passwords)} Passwords Successfully Generated.{stop}")
    print(f"{success}Passwords Successfully Saved: {location}{stop}")
    os.sys.exit()
        

def wordGen(iniList, minLen, maxLen):
    for a in range(0, len(info)):
        comb = combinations(info, a+1)
        for setword in list(comb):
            pwdLen = 0
            for b in setword:
                pwdLen+=len(b)
            if minLen <= pwdLen <= maxLen :
                perm = permutations(setword) 
                for c in list(perm):
                    pwd = ("")
                    for d in range(0,len(c)):
                        pwd+=c[d]
                    if pwd in passwords:continue 
                    else:passwords.append(pwd)
                    
    message(iniList)


def information(iniList, minLen, maxLen):
    try:
        with open(iniList, "r") as lines:
            pass

    except:
        os.system("clear || cls")
        print(banner())
        time.sleep(2)
        
        print(f"{notice}Ops!,{stop}")
        print(f"{notice}Look like `{iniList}` file is missing.{stop}")
        print(f"{notice}You gotta create the missing file, in order to avoid this error.{stop}")
        os.sys.exit()

    with open(iniList, "r") as lines:
        for line in lines:
            line = line.strip("\n")
            info.append(line)

    wordGen(iniList, minLen, maxLen)

    
def main():
    parser=argparse.ArgumentParser(
        description="a python-based program that generates a list of password (wordlist)."
    )
    
    parser.add_argument(
        '--iniList',
        default="config.ini",
        help='Path to the initial word list')
        
    parser.add_argument(
        "--minLen", default=4,
        help="minimum length of password")
        
    parser.add_argument(
        "--maxLen", default=14,
        help="maximum length of password")
        
    argument = parser.parse_args()

    iniList = argument.iniList
    maxLen = argument.maxLen
    minLen = argument.minLen
    
    
    
    os.system("clear || cls")
    print(banner())
    net=internet()

    if not net:
        time.sleep(2)
        print(f"\n{notice}Please check your internet connection{stop}")
        os.sys.exit()

    try:
        time.sleep(1)
        print(f"""\n\t{first}Generate WordList\n\t{second}Exit WORD-GEN\n""")
        opt=input(f"""{green}[{stop}WORD-GEN {green}]{blue}~~~{purple} """)

        if opt in["1","01","a","A"]:
            information(iniList, minLen, maxLen)

        elif opt in["2","02","b","B"]:
            time.sleep(2)
            print(f"\n{notice}Thanks for using WordList Generator.{stop}")
            os.sys.exit()

        else:
            time.sleep(2)
            print(f"\n{notice}Invali Option!{stop}")
            main()

    except KeyboardInterrupt:
        time.sleep(2)
        print(f"\n\n{notice}User Requested an Interrupt!{stop}")
        print(f"{notice}Program Running Down!{stop}...")
        os.sys.exit()


info=[]
passwords=[]

if __name__ == "__main__":
    main()
