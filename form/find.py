#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import shodan
import os
import webbrowser

from colorama import Back, Fore, init
import sys
from tqdm import tqdm
from time import sleep
from form.logo import LogoOne, LogoCero, LogoTwo
init()
def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description("Loading .....".format(k))
        loop.update(1)
    loop.close()
full = 0
def OpcionShoda():
    print("Comenzaremos")
    try:
        Sopcion = int(input(Fore.WHITE + "Coloca el numero de una opcion a ELEGIR\n [ Opers Linux ] > "))
        if Sopcion == 1:
            global full
            full = 1
            SearchShodan()
        elif Sopcion == 2:
            SearchShodan()
            print("1- SI\n2- NO")
            pregunta = int(input("¿Quieres abrir las IP en tu navegador?\n [ OPers Linux ] > "))
            if pregunta == 1:
                Abrirweb()

            else:

                print("PROCESO TERMINADO")




        elif Sopcion == 3:
            print(Fore.WHITE + """
            ############################################
            Te imprimire los posibles FTP VULNERABLES y 
            sin contraseña PARA ACCEDER
            solo coloca el user y dejas en blanco                                  
            la contraseña [USER]: anonymous
            ##############OPers Linux#####################""")
            Carga()
            SearchFtp()

        elif Sopcion == 4:
            print("Lista de Camaras")
            try:
                txt = open("form/funciones.txt", "r")
                for i in txt:
                    print(Fore.WHITE + "______________________________________________________________")

                    print(Fore.RED + i)
                # Descomenta la siguiente linea si quieres que se hagan pausas
                # input (Fore.WHITE + "Da enter para continuar... ")




            except:
                print("Error con el archivo")
    except:
        print(Fore.RED + "[ERROR]", "Debes colocar una opcion valida EJECUTA de nuevo el programa")



def SearchShodan():
    l = open('cookies/API.txt', 'r')
    for i, lineas in enumerate(l):
        if (i) == 0:
            #print(lineas)
            print("".join(lineas.split()))
            print("API EXTRAIDA")
    l.close()
    SHODAN_API = ("".join(lineas.split()))
    api = shodan.Shodan(SHODAN_API)
    busqueda = input("Que quieres BUSCAR\n [ Opers Linux ] > ")



    try:
        f = open('results.txt', 'w')
        # Search Shodan
        results = api.search(busqueda)

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            f.write('%s' % result['ip_str'] + "\n")
            if full == 1:
                print(result['data'])
                f.write('%s' % result['data'] + "\n")
            print('')


    except shodan.APIError as e:
        print('Error: {}'.format(e))




def SearchFtp():
    sites = []
    l = open('cookies/API.txt', 'r')
    for i, lineas in enumerate(l):
        if (i) == 0:
            # print(lineas)
            print("".join(lineas.split()))
            print("API EXTRAIDA")
    l.close()
    SHODAN_API = ("".join(lineas.split()))
    api = shodan.Shodan(SHODAN_API)
    f = open('FTP.txt', 'w')
    results = api.search("port: 21 Anonymous user logged in")
    print("hosts number: " + str(len(results['matches'])))
    for match in results['matches']:
        if match['ip_str'] is not None:
            print(match['ip_str'])
            f.write('%s' % match['ip_str'] + "\n")
            sites.append(match['ip_str'])


def Abrirweb():
    print("Comprobando si los archivos exiten")
    if os.path.isfile('results.txt') == True:
        txt = open('results.txt', 'r')
        for linea in txt:
            url = (linea)
            webbrowser.open(url, new=2, autoraise=True)
            input("Presiona enter para continuar....")
        txt.close()
    else:
        print("El archivo No existe")


