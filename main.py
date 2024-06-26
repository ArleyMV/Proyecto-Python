#imports
from functions import *
from menu import *
from datos import *

#const
try: 
    BASE_DATOS_USERS = "users.json"
    BASE_DATOS_PRODUCTOS = "productos.json"
    BASE_DATOS_SERVICIOS = "servicios.json"
    BASE_DATOS_VENTAS = "ventas.json"
    datoss = cargar_datos(BASE_DATOS_SERVICIOS)
    datosp = cargar_datos(BASE_DATOS_PRODUCTOS)
    datosu = cargar_datos(BASE_DATOS_USERS)
    datosv = cargar_datos(BASE_DATOS_VENTAS)


    #REPORTE ERRORES
    import traceback
    from datetime import datetime

    def log_error(exception):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        error_message = f"{timestamp}: {str(exception)}\n"
        with open("Errores.txt", "a") as file:
            file.write(error_message)
            traceback.print_exc(file=file)

#|-------------------------------------------------------------------------------------|
#|         !!!!!!!!!!!!!!!!!!!!!!!!   REGLAS DE USO   !!!!!!!!!!!!!!!!!!!!!!!!         |
#|  Para ingresar como Administrador: Usuario =     admin                              |
#|                                    Contraseña =  admin123                           |
#|  Trata de escribir todo en Minusculas                                               |
#|-------------------------------------------------------------------------------------|
    while True:
        menu_principal()
        opc = pedir_opc()
        if opc == 1:
            print("********************************************************")
            usuario= input("Digite el nombre de usuario de Administrador: ").lower()
            contraseña = input("Digite la contraseña del Administrador: ").lower()
            print("********************************************************")
            if usuario == "admin" and contraseña == "admin123": #USUARIO Y CONTRASEÑA ADMIN
                print("¡¡¡Bienvenido ADMINISTRADOR!!!")
                menu_admin()
                opc = pedir_opc()

                #ADMIN
                if opc == 1:
                    datosu = crear_user_admin(datosu)
                elif opc == 2:
                    datosu = eliminar_user(datosu)
                elif opc == 3:
                    datosu = actualizar_user(datosu)
                elif opc == 4:
                    datosp = crear_producto(datosp)
                elif opc == 5:
                    datosp = eliminar_producto(datosp)
                elif opc == 6:
                    datoss = crear_servicio(datoss)
                elif opc == 7:
                    datoss = eliminar_servicio(datoss)
                elif opc == 11:
                    print("¡Hasta la próxima!")
                    break
            else:
                print("¡ERROR!Contraseña o Usuario incorrectos")


        #GLOBAL
        elif opc == 2:
            menu_cliente()
            opc = pedir_opc()
            #CLIENTE
            if opc == 1:
                datosu = crear_user_cliente(datosu)
            elif opc == 2:
                datosv = compra_algo(datosv)
            elif opc == 3:
                datosu = validar_us(datosu)
            elif opc == 11:
                print("¡Hasta la próxima!")
                break
        elif opc == 11:
            print("¡Hasta la próxima!")
            break



    guardar_datos(datosv, BASE_DATOS_VENTAS)
    guardar_datos(datoss, BASE_DATOS_SERVICIOS)
    guardar_datos(datosp, BASE_DATOS_PRODUCTOS)
    guardar_datos(datosu, BASE_DATOS_USERS)

except Exception as e:
    log_error(e)