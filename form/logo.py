#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from colorama import Back, Fore, init
from time import sleep
from tqdm import tqdm
init()



def LogoCero():
    os.system("clear")
    print(Fore.RED + """
   ___  ___  __ __ __      __  _____    __     __  __
  /___\/ _ \/__/__/ _\    / /  \_   \/\ \ \/\ /\ \/ /
 //  // /_)/_\/ \/\ \    / /    / /\/  \/ / / \ \  / 
/ \_// ___//_/ _  _\ \  / /__/\/ /_/ /\  /\ \_/ /  \ 
\___/\/   \__\/ \_\__/  \____\____/\_\ \/  \___/_/\_\


                               (0 0) 
                       ---oOO-- (_) ----oOO---    
                     ╔═════════════════════════╗ 
                     ║ Bienvenido by OPERS!..  ║ 
                     ╚═════════════════════════╝ 
                        -------------------
                              |__|__| 
                               || || 
                              ooO Ooo 
                Canal Oficial YouTube:
                        https://www.youtube.com/opersweenlinux
""" + Fore.RESET)



def LogoOne():
    os.system("clear")
    print(Fore.RED + """.....____________________ , ,__
....../ `---___________----_____|] - - - - - - - - ░ ▒▓▓█D 
...../_==o;;;;;;;;_______.:/
.....), ---.(_(__) /
....// (..) ), ----"
...//___//
..//___//
.//___//       
                     Canal Oficial YouTube:
                        https://www.youtube.com/opersweenlinux
                                          
                                          """ + Fore.RESET)



def LogoTwo():
    os.system("clear")
    print(Fore.RED + """
   ___  ___  __ __ __      __  _____    __     __  __
  /___\/ _ \/__/__/ _\    / /  \_   \/\ \ \/\ /\ \/ /
 //  // /_)/_\/ \/\ \    / /    / /\/  \/ / / \ \  / 
/ \_// ___//_/ _  _\ \  / /__/\/ /_/ /\  /\ \_/ /  \ 
\___/\/   \__\/ \_\__/  \____\____/\_\ \/  \___/_/\_\

              Canal Oficial YouTube:
                        https://www.youtube.com/opersweenlinux

	""" + Fore.RESET)


def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description(Fore.BLUE + "Loading .....".format(k) + Fore.RESET)
        loop.update(1)
    loop.close()


def MenuInicial():
    os.system('clear')
    LogoCero()
    sleep(0.7)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoOne()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(1.5)
    sleep(0.60)
    Carga()
    print(Fore.GREEN + "\t\tBienvenido a OPERS-TOOL BY OPERS LINUX\t\t")
    print("\t\t__________________________\t\t")
