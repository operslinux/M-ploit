#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from form.logo import *
from form.run import *
def menu():
    print("""
    {0}[{1}1{0}] {2}CONECTAR API SHODAN      {0}[{1}2{0}] {2}VER DISPOSITIVOS CONECTADOS 
    {0}[{1}3{0}] {2}CONECTAR DISPOSITIVO     {0}[{1}4{0}] {2}DESCONECTAR DISPOSITIVO
    {0}[{1}5{0}] {2}ABRIR LA SHELL           {0}[{1}6{0}] {2}TOMAR CAPTURA DE PANTALLA
    {0}[{1}7{0}] {2}INSTALAR UNA APP         {0}[{1}8{0}] {2}LISTAR APPS
    {0}[{1}9{0}] {2}DESINSTALAR UNA APP      {0}[{1}10{0}] {2}CARGAR ARCHIVO
    {0}[{1}11{0}] {2}DESCARGAR ARCHIVO       {0}[{1}12{0}] {2}GRABAR PANTALLA (20 segundos)
                   {0}[{1}13{0}] {2}CERRAR SERVIDOR ADB
    
     
    """.format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))

def existe():
    if os.path.isfile('/usr/bin/adb') == True:
        print("{0}[{1}@{0}] {2}ADB ESTA INSTALADO {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
        sleep(0.5)
    else:
        print("{0}[{1}@{0}] {2}INSTALANDO ADB {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
        sleep(0.5)
        os.system("sudo apt install adb")

def main():
    MenuInicial()
    contador = 0
    while True:

        existe()
        menu()
        try:
            opcion = int(input("{0}[{1}@{0}] {2}COLOCA UNA OPCION {1} {3} >> ".format(Fore.CYAN, Fore.RED,Fore.WHITE, Fore.RESET)))
        except ValueError:
            print("{}[{}ERROR{}] {} COLOQUE UNA OPCION VALIDA {}".format(Fore.CYAN, Fore.RED, Fore.CYAN, Fore.WHITE, Fore.RESET))
            exit()
        if opcion == 1:
            print("{0}[{1}@{0}] {2}CONECTANDO CON SHODAN {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
            ejecucion()

        elif opcion == 2:

            print("{0}[{1}@{0}] {2}DISPOSITIVOS CONECTADOS{3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
            os.system("adb devices")



        elif opcion == 3:
            ip = input("{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET ))
            print("{0}[{1}@{0}] {2}CONECTANDO CON {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET) + ip + " E INICIANDO SERVIDOR...... {0}>> {1}".format(Fore.RED, Fore.RESET ))
            os.system("adb start-server")
            os.system("adb connect " + ip)
            os.system("adb devices")
            #LogoTwo()


        elif opcion == 4:
            os.system("adb start-server")
            ip =input("{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
            print("{0}[{1}@{0}] {2}DESCONECTANDO DISPOSITIVOS {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
            os.system("adb disconnect " + ip)


        elif opcion == 5:
            os.system("adb devices")
            ip = input("{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))
            print("{0}[{1}@{0}] {2}ABRIENDO SHELL REMOTA EN DISPOSITVO {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE, Fore.RESET))

            sleep(10)
            os.system("adb -s " + ip + " shell")
        elif opcion == 6:

            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                      Fore.RESET))
            print(
                "{0}[{1}@{0}] {2}HACIENDO CAPTURA DE PANTALLA {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                        Fore.RESET))

            contador = contador + 1
            captura = "captura" + str(contador)
            os.system("adb -s " + ip + " shell screencap -p /sdcard/" + captura)
            os.system("adb -s " + ip + " pull /sdcard/" + captura)
            sleep(5)
            os.system("adb -s " + ip + " shell rm /sdcard/" + captura)

        elif opcion == 7:
            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                      Fore.RESET))
            ruta = input(
                "{0}[{1}@{0}] {2}COLOCA LA RUTA DE LA APP...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                      Fore.RESET))
            print(
                "{0}[{1}@{0}] {2}INSTALANDO APP {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                 Fore.RESET))
            os.system("adb -s " + ip + " install " + ruta)
            print(
                "{0}[{1}@{0}] {2}APP INSTALADA {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                   Fore.RESET))
        elif opcion == 8:
            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                                      Fore.RESET))
            os.system("adb -s " + ip + " shell pm list packages")

        elif opcion ==9:
            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                         Fore.WHITE,
                                                                                         Fore.RESET))
            nombre = input(
                "{0}[{1}@{0}] {2}COLOCA EL NOMBRE DE LA APP...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                         Fore.WHITE,
                                                                                         Fore.RESET))
            os.system("adb -s " + ip + " uninstall " + nombre)

        elif opcion == 10:
            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                      Fore.WHITE,
                                                                                      Fore.RESET))
            ruta = input(
                "{0}[{1}@{0}] {2}COLOCA LA RUTA DEL ARCHIVO A SUBIR...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                    Fore.WHITE,
                                                                                    Fore.RESET))
            os.system("adb -s " + ip + " push " + ruta + " /sdcard/Download")

        elif opcion == 11:
            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                      Fore.WHITE,
                                                                                      Fore.RESET))
            ruta = input(
                "{0}[{1}@{0}] {2}COLOCA LA RUTA DEL ARCHIVO A DESCARGAR...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                    Fore.WHITE,
                                                                                    Fore.RESET))
            os.system("adb -s " + ip + " pull " + ruta)

        elif opcion == 12:
            os.system("adb devices")
            ip = input(
                "{0}[{1}@{0}] {2}COLOCA LA IP DEL DISPOSITIVO...... {1}>> {3}".format(Fore.CYAN, Fore.RED,
                                                                                      Fore.WHITE,
                                                                                      Fore.RESET))
            os.system("adb -s " + ip + " shell screenrecord --time-limit 20 /sdcard/mivideo.mp4")
            os.system("adb -s " + ip + " pull /sdcard/mivideo.mp4")
            sleep(5)
            os.system("adb -s " + ip + " shell rm /sdcard/mivideo.mp4")

        elif opcion == 13:
            os.system("adb kill-server")
            print(
                "{0}[{1}@{0}] {2}SERVIDOR CERRADO {3} ......".format(Fore.CYAN, Fore.RED, Fore.WHITE,
                                                                   Fore.RESET))



        else:
            print("{}[{}ERROR{}] {} COLOQUE UNA OPCION VALIDA {}".format(Fore.CYAN, Fore.RED, Fore.CYAN, Fore.WHITE,
                                                                         Fore.RESET))
            exit()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        LogoTwo()
        exit()


