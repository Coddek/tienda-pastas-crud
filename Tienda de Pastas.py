"""
SISTEMA DE GESTION DE VENTAS PARA UNA CASA DE PASTAS
Descripción General del proyecto: 
Se diseñó un programa para gestionar la venta de comidas en  un local gastronómico.
El programa permite desplegar un menú que habilita al operador seleccionar diferentes funciones 
Estas funciones permiten intervenir en la visualización de los datos (lista de comidas)
El programa esta organizado de manera tal que presenta una lista de productos (comidas), codigo de identificación del producto
nombre, descripción del producto y característica (apto/no apto celíaco).
Aclaración: Para evitar conflictos con el programa, el uso de "tildes"y/o carcateres tales como "ñ" 
se limitó a las secciones que incluían descripciones. """

import os
import colorama

## LISTA-DICCIONARIO DE COMIDAS
# Contiene la información de los productos disponibles (comidas): 
# códido de identificación (id), nombre, descripción y característica "apto/no-apto celíaco".            
TACC = "NO APTO CELIACO"
SIN_TACC = "APTO CELIACO"
lista_de_comidas = [
    {
    "id": 1,
    "nombre_comida":"Ravioles jyq",
    "descrip" : "Pasta rellena de jamón con queso y especias",
    "Apto_celiaco" : TACC
    },
    {
    "id": 2,
    "nombre_comida":"Ñoquis SIN TACC",
    "descrip" : "Ñoquis de papa hechos con harina de almendras",
    "Apto_celiaco" : TACC
    },
    {
    "id": 3,
    "nombre_comida":"Ñoquis Tradicionales",
    "descrip" : "Ñoquis de papa hechos con harina de trigo",
    "Apto_celiaco" : TACC
    },
    {
    "id": 4,
    "nombre_comida":"Tallarines",
    "descrip" : "Tallarines al huevo",
    "Apto_celiaco" : SIN_TACC
    },
    {
    "id": 5,
    "nombre_comida":"Lasagna Vegetariana",
    "descrip" : "Deliciosa receta con champiñones y calabacitas hecha con mucho amor",
    "Apto_celiaco" : SIN_TACC
    }
]

def clear_console():
    if os.name == 'nt':
        os.system('cls')

proximo_id = 6

# FUNCIONALIDADES DISPONIBLES: MENÚ de opciones, LISTAR datos, BUSCAR datos, AGREGAR datos, EDITAR datos, ELIMINAR datos, SALIR DEL PROGRAMA
# Dentro de las funcionalidades de se incluye la VALIDACIÓN DE ENTRADA DE DATOS para minimizar los errores del usuario 

# Función AGREGAR productos: permite agregar nuevos productos a lista-diccionario de comidas
def agregar_comidas(nombre, descripcion, apto_celiaco):
    global proximo_id
    
    comida_nueva = {
        "id": proximo_id,
        "nombre_comida" : nombre,
        "descrip" : descripcion,
        "Apto_celiaco": apto_celiaco
    }
    lista_de_comidas.append(comida_nueva)
    proximo_id += 1

#Función ELIMINAR productos a partir del "nombre" de la comida
def eliminar_str_comida(nombre):
    for comida in lista_de_comidas:
        if(comida["nombre_comida"].lower() == nombre.lower()):
            lista_de_comidas.remove(comida)
            print(colorama.Back.RED + f"Comida: {nombre} eliminada con éxito" + colorama.Back.RESET + " ")
            return

    print(colorama.Back.RED + f"Comida con el nombre {nombre} NO ENCONTRADA" + colorama.Back.RESET + " ")

#Función ELIMINAR productos a partir del "id" de la comida
def eliminar_id_comida(nombre_id):
    validacion_eliminar_id = False # Bandera para verificar si el id se encuentra
    for id in lista_de_comidas:
        if(id["id"] == nombre_id):
            validacion_eliminar_id = True
            print(f"\n Realmente desea eliminar el elemento con id número {nombre_id}?")
            si_o_no = input("Ingrese S para si / Ingrese N para no: ").upper()
            if si_o_no == 'S':
                lista_de_comidas.remove(id)
                print(colorama.Back.GREEN + f"id: {nombre_id} eliminado con éxito" + colorama.Back.RESET + " ")
                break # Salir del bucle una vez que se elimina el elemento
            elif si_o_no == 'N':
                print("Volviendo al menu...")
                break  # Salir del bucle si el usuario decide no eliminar
    if not validacion_eliminar_id:
        print(colorama.Back.RED + f"Número de id {nombre_id} NO ENCONTRADO" + colorama.Back.RESET + " ")
            


#Función EDITAR productos a partir del "nombre" de la comida con opción de filtrar por característica "APTO CELIACO/NO_APTO CELIACO"
def editar_comida_str(nombre):     
    for comida in lista_de_comidas:
        if(comida["nombre_comida"].lower() == nombre.lower()):
            nuevo_nombre = input(colorama.Fore.BLUE + f"Ingrese el nuevo nombre para reemplazar a {comida['nombre_comida']}:" + colorama.Fore.RESET + " ")
            nueva_descripcion = input(colorama.Fore.BLUE + f"Ingrese la nueva descripción para {comida['descrip']}:" + colorama.Fore.RESET + " ")
            print(colorama.Fore.BLUE + f"""
Ingrese nueva característica de celíaco para {comida['Apto_celiaco']}: 
                ###########################
                #    EDITOR DE PRODUCTOS  #
                #  {colorama.Fore.WHITE}1.{colorama.Fore.GREEN} APTO CELIACO{colorama.Fore.BLUE}        #
                #  {colorama.Fore.WHITE}2.{colorama.Fore.RED} NO APTO CELIACO{colorama.Fore.BLUE}     #
                ###########################
                """ + colorama.Fore.RESET)
            validacion_opcion= False
            while validacion_opcion == False: 
                opcion_celiaco = input(colorama.Back.WHITE + "Elija la opción 1 o 2:" + colorama.Back.RESET + " ")
                if opcion_celiaco.isdigit():
                    if opcion_celiaco== "1":
                        nuevo_ap_celiaco = SIN_TACC
                        validacion_opcion= True
                    elif opcion_celiaco == "2":
                        nuevo_ap_celiaco = TACC
                        validacion_opcion= True
                    else:
                        print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")
                        return False
                else:
                    print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")
                    nombre = input(colorama.Back.WHITE + "Ingrese nuevamente un nombre de comida correcto" + colorama.Back.RESET + " ")
            comida["nombre_comida"] = nuevo_nombre
            comida["descrip"] = nueva_descripcion
            comida["Apto_celiaco"] = nuevo_ap_celiaco
            
            print(colorama.Back.GREEN + "Descripción EDITADA con éxito" + colorama.Back.RESET + " ")
            return True
    
    print(colorama.Back.RED + f"Comida con el nombre {nombre} no encontrada" + colorama.Back.RESET + " ")
    return False
 
#Función EDITAR productos a partir del "id" de la comida con opción de filtrar por característica "APTO CELIACO/NO_APTO CELIACO"    
def editar_comida_id(valor_id):
    for comida in lista_de_comidas:
        if (valor_id is not str):
            if(comida["id"] == valor_id):
                nuevo_nombre = input(colorama.Fore.BLUE + f"Ingrese el nuevo nombre para reemplazar a {comida['nombre_comida']}: " + colorama.Fore.RESET + " ")
                nueva_descripcion = input(colorama.Fore.BLUE + f"Ingrese la nueva descripción para {comida['descrip']}: " + colorama.Fore.RESET + " ")
                ##
                print(colorama.Fore.BLUE + f"""
        Ingrese nueva característica de celíaco para {comida['Apto_celiaco']}: 
                    ###########################
                    #    EDITOR DE PRODUCTOS  #
                    #  {colorama.Fore.WHITE}1.{colorama.Fore.GREEN} APTO CELIACO{colorama.Fore.BLUE}        #
                    #  {colorama.Fore.WHITE}2.{colorama.Fore.RED} NO APTO CELIACO{colorama.Fore.BLUE}     #
                    ###########################
                    """ + colorama.Fore.RESET)
                validacion_opcion= False
                while validacion_opcion == False: 
                    opcion_celiaco = input(colorama.Back.WHITE + "Elija la opción 1 o 2:" + colorama.Back.RESET + " ")
                    if opcion_celiaco.isdigit():
                        if opcion_celiaco== "1":
                            nuevo_ap_celiaco = SIN_TACC
                            validacion_opcion= True
                        elif opcion_celiaco == "2":
                            nuevo_ap_celiaco = TACC
                            validacion_opcion= True
                        else:
                            print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")
                            return False
                    else:
                        print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")
                        nombre = input(colorama.Back.WHITE + "Ingrese nuevamente un nombre de comida correcto" + colorama.Back.RESET + " ")
                        
                comida["nombre_comida"] = nuevo_nombre
                comida["descrip"] = nueva_descripcion
                comida["Apto_celiaco"] = nuevo_ap_celiaco
                
                print(colorama.Back.GREEN + "Descripción EDITADA con éxito" + colorama.Back.RESET + " ")
                return True
                print(colorama.Fore.RED + f"Comida con el nombre {nombre} no encontrada" + colorama.Fore.RESET + " ")
        else:
            print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")
    return False
#Función LISTAR productos para visualizar la lista de comidas disponibles, filtrando para ver toda la lista o sólo la lista SIN TACC
#ACLARACION:  SIN TACC y APTO CELIACO son equivalentes,  TACC Y NO APTO CELIACO son equivalentes
def ver_listado():
    validacion_listado = False

    while validacion_listado == False:
    
        opcion_listado = input(colorama.Back.WHITE + "Ingrese la opción:" + colorama.Back.RESET + " ")
        if opcion_listado.isdigit():
            if opcion_listado == "1":
                for i in lista_de_comidas:
                    if i["Apto_celiaco"] == TACC:
                        print(colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX + f"{i['id']} - {colorama.Fore.LIGHTBLUE_EX + i['nombre_comida'].upper()} : " + f"\033[3m{i['descrip']}\033[0m  : {colorama.Fore.RED + i['Apto_celiaco']}" + colorama.Fore.RESET)
                        validacion_listado = True
                    
                    else:
                        print(colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX + f"{i['id']} - {colorama.Fore.LIGHTBLUE_EX + i['nombre_comida'].upper()} : " + f"\033[3m{i['descrip']} \033[0m : {colorama.Fore.GREEN + i['Apto_celiaco']}" + colorama.Fore.RESET)
            
            elif opcion_listado == "2":
                for i in lista_de_comidas:
                    if i["Apto_celiaco"] == SIN_TACC:
                        print(colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX + f"{i['id']} - {colorama.Fore.LIGHTBLUE_EX + i['nombre_comida'].upper()} : " + f"\033[3m{i['descrip']} \033[0m : {colorama.Fore.GREEN + i['Apto_celiaco']}" + colorama.Fore.RESET)
                        validacion_listado = True
            else:
                print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")
        else:
            print(colorama.Back.RED + "OpciÓn incorrecta, intentelo de nuevo!" + colorama.Back.RESET + " ")        

#Funcion GENERICA MOSTRAR LISTADO
def mostrar_listado():
    for i in lista_de_comidas:
        if i["Apto_celiaco"] == TACC:
            print(colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX + f"{i['id']} - {colorama.Fore.LIGHTBLUE_EX + i['nombre_comida'].upper()} : " + f"\033[3m{i['descrip']}\033[0m  : {colorama.Fore.RED + i['Apto_celiaco']}" + colorama.Fore.RESET)
            validacion_listado = True
        
        else:
            print(colorama.Style.BRIGHT + colorama.Fore.LIGHTWHITE_EX + f"{i['id']} - {colorama.Fore.LIGHTBLUE_EX + i['nombre_comida'].upper()} : " + f"\033[3m{i['descrip']} \033[0m : {colorama.Fore.GREEN + i['Apto_celiaco']}" + colorama.Fore.RESET)



    
#Función BUSCAR para buscar productos disponibles por "id" o  "nombre" de la comida
def buscar_comida(codigo):
    # Busca por id si el código es un número
    validacion_buscar = False
    while validacion_buscar == False:
      
        if codigo.isdigit():#pregunta por si es un dígito
            id_busqueda = int(codigo) #convierte el dígito en entero
            for comida in lista_de_comidas:
                if comida["id"] == id_busqueda:
                    validacion_buscar = True
                    print(colorama.Fore.LIGHTBLUE_EX + f"Comida ENCONTRADA: {comida['id']} - {comida['nombre_comida']} : {comida['descrip']} : {comida['Apto_celiaco']}" + colorama.Fore.RESET)
                    return
                
            print(colorama.Back.RED + f"Comida con ID {codigo} NO ENCONTRADO" + colorama.Back.RESET)
            codigo = input(colorama.Fore.LIGHTBLUE_EX + "Ingrese un nuevo código o nombre de comida: " + colorama.Fore.RESET)
            
        else:
            # Busca por nombre si el código NO es un número
            for comida in lista_de_comidas:
                if comida["nombre_comida"].lower() == codigo.lower():
                    validacion_buscar = True
                    print(colorama.Fore.LIGHTBLUE_EX + f"Comida ENCONTRADA: {comida['id']} - {comida['nombre_comida']} : {comida['descrip']} : {comida['Apto_celiaco']}" + colorama.Fore.RESET)
                    return
                
            print(colorama.Back.RED + f"Comida con el nombre {codigo} NO ENCONTRADO" + colorama.Back.RESET)
            codigo = input(colorama.Fore.LIGHTBLUE_EX + "Ingrese un nuevo código o nombre de comida: " + colorama.Fore.RESET)

# AUTENTICACION DEL PROGRAMADOR
# Lista-diccionario para introducir más de un usuario-contraseña
usuarios = [
        {"usuario": "agustin", "contraseña": "123"},
        {"usuario": "Usuario", "contraseña": "0000"},
    ]
            
ejecutar_programa = True
# Función para AUTENTICAR USUARIO-CONTRASEÑA
def autenticar_usuario(user, passw):
    global ejecutar_programa 
    for i in usuarios:
        global ejecutar_programa
        if user.lower() == i['usuario'] and passw.isdigit() and passw == i["contraseña"]:
            ejecutar_programa = True
            return ejecutar_programa

# Visualización del MENÚ DE OPCIONES
def VerOpcionesMenu():
    print(
        f"""
{colorama.Fore.BLUE}#################################################
##------ PROGRAMA DE PASTAS CASERAS -----------##
## {colorama.Fore.WHITE}1.{colorama.Fore.BLUE} Ver listado de comidas                   ##
## {colorama.Fore.WHITE}2.{colorama.Fore.BLUE} Buscar comida                            ##
## {colorama.Fore.WHITE}3.{colorama.Fore.BLUE} Agregar un comida nueva                  ##
## {colorama.Fore.WHITE}4.{colorama.Fore.BLUE} Editar un comida existente               ##
## {colorama.Fore.WHITE}5.{colorama.Fore.BLUE} Eliminar una comida de la lista          ##
## {colorama.Fore.WHITE}6.{colorama.Fore.BLUE} Salir del programa                       ##
#################################################{colorama.Fore.RESET}
"""
    )

#Validación para ingresar al programa principal
ejecutar_autenticacion = False
while ejecutar_autenticacion is False:
    usua = input(colorama.Fore.LIGHTBLACK_EX + colorama.Back.WHITE + "Ingrese el usuario:" + colorama.Fore.RESET + colorama.Back.RESET + " " )
    clave = input(colorama.Fore.LIGHTBLACK_EX + colorama.Back.WHITE + "Ingrese la clave:" + colorama.Fore.RESET + colorama.Back.RESET + " " )
    if autenticar_usuario(usua, clave):
        ejecutar_autenticacion = True
        print(colorama.Fore.WHITE + colorama.Back.LIGHTGREEN_EX + """
\t¡¡BIENVENIDO/A A PASTAS ARGENTINAS!!
""" + colorama.Fore.RESET + colorama.Back.RESET)
    else:
        print(colorama.Fore.WHITE + colorama.Back.RED + """
Usuario y/o contraseña incorrecto!
Vuelva a intentarlo.
""" + colorama.Fore.RESET + colorama.Back.RESET)

#########----ESTRUCTURA PRINCIPAL DEL PROGRAMA-----

# Las funcionalidades incluyen la VALIDACIÓN DE ENTRADA DE DATOS para minimizar los errores del usuario 

## MENÚ DE OPCIONES
# Luego de la correcta autenticación, se despliega un menú que permite al usuario optar por diferentes funcionalidades

while(autenticar_usuario(usua, clave) is True):
    input("\nPresione enter para ver el menú de opciones...")
    clear_console()
    VerOpcionesMenu()
    opciones_validas = ["1", "2", "3", "4", "5", "6"]
    validacion_menu = False
    while validacion_menu == False:
        opcion = input(colorama.Fore.LIGHTBLUE_EX + colorama.Back.WHITE + "Elige una opción:" + colorama.Fore.RESET + colorama.Back.RESET + " ")
        if opcion.isdigit() and opcion in opciones_validas:
            validacion_menu = True
            clear_console()
        else:
            print(colorama.Back.RED + "Opción incorrecta. Ingrese una opción válida!!" + colorama.Back.RESET + " ")
     
    match(opcion):
    ## LISTAR DATOS
    # Se despliega un submenú que permite optar por visualizar la lista de todas las comidas disponibles en el local  
    # o únicamente la lista de comidas SIN TACC
        case "1":
            print(colorama.Fore.LIGHTBLUE_EX +  f"""
            ###########################
            #                         #
            #  {colorama.Fore.WHITE}Listado de Comidas{colorama.Fore.LIGHTBLUE_EX}     #
            #                         #
            # {colorama.Fore.WHITE}1.{colorama.Fore.LIGHTBLUE_EX}  Ver Lista Completa  #
            # {colorama.Fore.WHITE}2.{colorama.Fore.LIGHTBLUE_EX}  Ver lista SIN TACC  #
            #                         #
            ###########################
          """+ colorama.Fore.RESET)
            ver_listado()
    ## BUSCAR DATOS
    # Permite al usuario buscar datos específicos por nombre de producto o id        
        case "2":
            
            codigo_busqueda = input(colorama.Fore.BLUE + "Ingrese el nombre o id de la comida a buscar:" + colorama.Fore.RESET + " "  )
            buscar_comida(codigo_busqueda)
    ## AGREGAR DATOS
    # Permite al usuario ingresar nuevos datos (comidas) a la lista y la información relevante asociada (descripción)           
        case "3":
            nombre_comida_nueva = input(colorama.Fore.BLUE + "Ingrese el nombre de la comida nueva:" + colorama.Fore.RESET + " "  )
            descrip_comida_nueva = input(colorama.Fore.BLUE + "Ingrese la descripción de la comida nueva:" + colorama.Fore.RESET + " "  )
    # FILTRAR DATOS:  Habilita al usuario a filtrar los datos según la característica de la comida "APTO/ NO APTO CELIACO"
            print(colorama.Fore.BLUE + f"""
       #### Elija la característica APTO CELIACO o NO APTO ####
    
                ###########################
                #  {colorama.Fore.WHITE}1.{colorama.Fore.GREEN} APTO CELIACO{colorama.Fore.BLUE}        #
                #  {colorama.Fore.WHITE}2.{colorama.Fore.RED} NO APTO CELIACO{colorama.Fore.BLUE}     #
                ###########################
                """ + colorama.Fore.RESET + " ")
            validacion_celiaco = False
            while validacion_celiaco == False:
                opcion_celiaco = input(colorama.Back.WHITE + "Elija la opción 1 o 2:" + colorama.Back.RESET + " ")
                if opcion_celiaco.isdigit():
                    if opcion_celiaco == "1":
                        celiaco_comida_nueva = SIN_TACC
                        validacion_celiaco = True
                    elif opcion_celiaco == "2":
                        celiaco_comida_nueva = TACC
                        validacion_celiaco = True
                    else:
                        print(colorama.Back.RED + "Opción incorrecta, intentelo de nuevo." + colorama.Back.RESET)   
                else:
                    print(colorama.Back.RED + "Opción incorrecta, intentelo de nuevo." + colorama.Back.RESET)
            
            agregar_comidas(nombre_comida_nueva, descrip_comida_nueva, celiaco_comida_nueva)
            
            print(colorama.Back.GREEN + "Comida agregada con éxito!" + colorama.Back.RESET + " "  )
        
    ## EDITAR DATOS
    # Permite al usuario editar datos exitentes, filtrando por id o nombre del producto (comida)    
        case "4":
            mostrar_listado()
            print(colorama.Fore.BLUE + f"""
                ###########################
                #    EDITOR DE PRODUCTOS  #
                #  {colorama.Fore.WHITE}1.{colorama.Fore.BLUE} Buscar por id       #
                #  {colorama.Fore.WHITE}2.{colorama.Fore.BLUE} Buscar por comida   #
                ###########################
                """ + colorama.Fore.RESET + " "  )
            validacion_edicion = False
            while validacion_edicion == False:
              
                id_o_str = input(colorama.Back.WHITE + "Ingrese la opción que desea (1 o 2):" + colorama.Back.RESET + " "  )
                if id_o_str.isdigit():
                    
                    if id_o_str == "1":
                        try:
                            comida_a_editar = int(input(colorama.Back.WHITE + "Ingrese el id de la comida a EDITAR:" + colorama.Back.RESET + " "  ))
                            if editar_comida_id(comida_a_editar):
                                validacion_edicion = True
                            else:
                                print(colorama.Back.RED + "id incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")    
                        except ValueError:
                            print(colorama.Back.RED + "El id debe ser un numero entero" + colorama.Back.RESET + " ")
                    elif id_o_str == "2":
                        comida_a_editar = input(colorama.Back.WHITE + "Ingrese el nombre de la comida a EDITAR:" + colorama.Back.RESET + " "  )
                        if editar_comida_str(comida_a_editar):
                            validacion_edicion = True
                    else:
                        print(colorama.Back.RED + "Opción incorrecto, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")

                else:
                    print(colorama.Back.RED + "Opción incorrecta, intente nuevamente con una opción válida" + colorama.Back.RESET + " ")

    ## ELIMINAR DATOS
    # Permite al usuario eliminar datos de la colección, ingresando el id o nombre del producto
        case "5":
            mostrar_listado()
            print(colorama.Fore.BLUE + f"""
                ###########################
                #    EDITOR DE PRODUCTOS  #
                # {colorama.Fore.WHITE}1.{colorama.Fore.BLUE} Eliminar por id      #
                # {colorama.Fore.WHITE}2.{colorama.Fore.BLUE} Eliminar por comida  #
                ###########################
                """ + colorama.Fore.RESET + " "  )
            id_o_str = input(colorama.Back.WHITE + "Ingrese la opción que desea (1 o 2):" + colorama.Back.RESET + " "  )
            # HACER WHILE PARA ERROR
            validacion_eliminar = False
            while validacion_eliminar == False:
            
                if id_o_str == "1":
                    try:
                        comida_a_eliminar = int(input(colorama.Back.WHITE + "Ingrese el id de la comida a ELIMINAR:" + colorama.Back.RESET + " "  ))
                        eliminar_id_comida(comida_a_eliminar)
                        validacion_eliminar = True
                    except ValueError:
                        print(colorama.Back.RED + "El id debe ser un numero entero" + colorama.Back.RESET + " ")

                elif id_o_str == "2":
                    comida_a_eliminar = input(colorama.Back.WHITE + "Ingrese el nombre de la comida a ELIMINAR:" + colorama.Back.RESET + " "  )
                    eliminar_str_comida(comida_a_eliminar)
                    validacion_eliminar = True
                else:
                    print(colorama.Back.RED + "Ingrese una opcion correcta" + colorama.Back.RESET + " ")
                    id_o_str = input(colorama.Back.WHITE + "Ingrese la opción que desea (1 o 2):" + colorama.Back.RESET + " "  )
            
    ## SALIR DEL PROGRAMA
    # Habilita la salida del programa        
        case "6":
            print(colorama.Back.BLUE + "Saliendo del programa. Hasta la proxima!!" + colorama.Back.RESET + " "  )
            ejecutar_programa = False
            break
        case _:           
            print(colorama.Fore.BLUE + "Selecciona una opción valida" + colorama.Fore.RESET + " "  )



