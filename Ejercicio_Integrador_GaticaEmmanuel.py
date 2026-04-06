

#Autor : Gatica Emmanuel David
#Descripcion: se arma un menu con todos los ejercicios, deberá usted seleccionar a que ejercicio quiere ingresar.

opcion = 0


#Menu Opciones de Ejercicios practicos integradores.
while opcion != 6:
    print("\n========= MENU PRINCIPAL =========")
    print("1. Ejercicio 1: Caja Kiosko")
    print("2. Ejercicio 2: Acceso al Campus y Menú Seguro")
    print("3. Ejercicio 3: Agenda de Turnos con Nombres")
    print("4. Ejercicio 4: Escape Room: La Bóveda")
    print("5. Ejercicio 5: Escape Room: La Arena del Gladiador")
    print("6. Salir")
    print("==================================")

    opcion = input("Ingrese una opcion entre 1 y 6: ")

    while not opcion.isdigit():
        print("Error. Ingrese solo numeros.")
        opcion = input("Ingrese una opcion entre 1 y 6: ")

    while int(opcion) < 1 or int(opcion) > 6:
        print("Error. Opcion fuera de rango.")
        opcion = input("Ingrese una opcion entre 1 y 6: ")

        while not opcion.isdigit():
            print("Error. Ingrese solo numeros.")
            opcion = input("Ingrese una opcion entre 1 y 6: ")

    opcion = int(opcion)

    #Menu Opciones de Ejercicios practicos integradores.
    match opcion:
        case 1:
            print("---------------------------")
            print("\nIngresaste al Ejercicio 1\n")
            print("---------------------------")

            #Ejercicio N° 1 Caja Kiosko

            cliente = input("Ingrese el nombre del Cliente: ").capitalize()

            #Validacion de ingreso cliente correcto.
            while cliente == "" or not cliente.isalpha() :
                print("Error . El nombre del cliente no debe ser o estar vacio, ingrese letras solamente. ")
                cliente = input("Ingrese el nombre del Cliente: ")

            cantidad_inicial = input("Ingrese la cantidad de prodctos a comprar. ")

            #Validacion de cantidad incial indicada.
            while int(cantidad_inicial) <= 0 or not cantidad_inicial.isdigit():
                print("Error . La cantidad debe ser en valores positivos. ")
                cantidad_inicial = int(input("Ingrese nuevamente, la cantidad de productos a comprar. "))

            cantidad = int(cantidad_inicial)

            #Definimos variables antes de utilizarlas.
            pTotalSinDescuento =0
            pTotalConDescuento =0

            for i in range (1 , cantidad +1 ) :
                precio_producto = input(f"Precio Producto {i} : ")

                while not precio_producto.isdigit() :
                    print("Error. El precio del producto no es valido , ingrese nuevamente.")
                    precio_producto = (input(f"Precio Producto {i} : "))
                
                precio = int(precio_producto)

                #usamos lower para formatear ingresos del cliente.
                descuento = input(f"El producto {i} , tiene descuento S/N ?? ").lower()

                while descuento != "s" and descuento != "n" :
                    print(f"Error. Solo debe ingresar S o N - como opcion. ")
                    descuento = input(f"El producto {i} , tiene descuento S/N ?? ").lower()

                pTotalSinDescuento += precio        #El valor que tiene el producto, sin un descuento

                if descuento == "s" :
                    precio_final = precio * 0.90    #Producto con descuento.
                else :
                    precio_final = precio           #Producto sin descuento.

                pTotalConDescuento += precio_final   #El valor que tiene el producto, con un descuento

            ahorroTotal = pTotalSinDescuento - pTotalConDescuento
            promedioProducto = pTotalConDescuento / cantidad        #el promedio por unidad vendida. 

            print("\n--- RESUMEN FINAL ---")
            print(f"Nombre Cliente: {cliente}")
            print(f"Total sin descuentos : ${pTotalSinDescuento}")
            print(f"Total con descuentos : ${pTotalConDescuento}")
            print(f"Ahorro Total final: ${ahorroTotal}")
            print(f"Promedio producto : ${promedioProducto : .2f}")


        case 2:
            print("---------------------------")
            print("\nIngresaste al Ejercicio 2\n")
            print("---------------------------")

            #Ejercicio N° 2 : “Acceso al Campus y Menú Seguro”

            usuario_correcto = "alumno"
            clave_correcta = "python123"
            intento = 0

            usuario = input("Ingrese su nombre usuario: ")
            contraseña = input("Ingrese su contraseña: ")

            while usuario != usuario_correcto or contraseña != clave_correcta :            
                        intento += 1
                        print(f"Ingreso incorrecto. {intento} intento  ")

                        if intento == 3 :
                                print("su cuenta esta bloqueada, hable con el Administrador. ")
                                break

                        usuario = input("Ingrese su nombre de usuario nuevamente: ")
                        contraseña = input("Ingrese su contraseña nuevamente: ")

            #Validacion del ingreso --> mismo usuario y contraseña
            if usuario == usuario_correcto and contraseña == clave_correcta:
                print("\nAcceso concedido - Bienvenido !!")
                opcion = 0

                while opcion != 4 :
                    print("\n----------- Menu de opciones ------------")
                    print("1. Ver estado inscripción ")
                    print("2. Cambiar clave ")
                    print("3. Frase Motivacional")
                    print("4. Salir")
                    print("-----------------------\n")

                    opcion = input("Ingrese una opcion entre el rango 1 a 4 ")

                    #Realizo una validacion para el rango definido, entre 1 a 4.
                    while not opcion.isdigit() :
                            print(f"Ingreso una opcion que no es valida.")
                            opcion = input("Ingrese una opcion entre el rango 1 a 4 :")

                    #Opciones correctas de seleccion
                    if int(opcion) < 1 or  int(opcion) > 4 :
                        print("Opcion fuera de rangao ")        
                        opcion = input("Ingrese una opcion entre el rango 1 a 4 :")

                        #Realizo una validacion para el rango definido, entre 1 a 4.
                        while not opcion.isdigit() :
                            print(f"Ingreso una opcion que no es valida.")
                            opcion = input("Ingrese una opcion entre el rango 1 a 4 :")

                    opcion = int(opcion)

                    if opcion == 1 :
                        print("\nInscripto")
                    
                    elif  opcion == 2 :
                        nueva_clave = input("Ingrese la nueva contraseña: ")
                        confirmar_clave =  input("Confirme la nueva contraseña: ")

                        if len(nueva_clave) <6 :
                            print("Error. La Nueva clave debe tener un minimo de 6 caracteres. ")
                        elif nueva_clave != confirmar_clave :
                            print("Las claves no coinciden , revisar por favor su nueva clave. ")
                        else :
                            pass_new = nueva_clave     
                            print("\nContraseña nueva actualizada correctamente.")
                        
                    elif opcion == 3 :
                        print("\nFrase Motivacional: Hoy no es siempre, sigue adelante!!! ")
                    elif  opcion == 4 :
                        print("\nSaliendo....!! ")
        
        case 3:
            print("---------------------------")
            print("\nIngresaste al Ejercicio 3\n")
            print("---------------------------")

            #Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres

            operador = input("Bienvenido , ingrese su nombre como operador. ")

            #Validacion para ingreso operador.
            while operador == "" or not operador.isalpha() :
                print("Error. Por Favor ingrese nuevamente su nombre ")
                operador = input("Bienvenido , ingrese nuevamente, su nombre como operador (Sin caracteres ni numeros). ")

            opcion = 0 #Definimos las opciones del menu

            #Turnos disponibles agenda dia Lunes
            tLunes1=""
            tLunes2=""
            tLunes3=""
            tLunes4=""

            #Turnos disponibles agenda dia Martes
            tMartes1=""
            tMartes2=""
            tMartes3=""

            #Opciones Menu de opciones
            while opcion != 5 :
                print("\n----------- Menu de opciones ------------")
                print("1. Reservar turno ")
                print("2. Cancelar turno (por nombre) ")
                print("3. Ver agenda del día ")
                print("4. Ver resumen general")
                print("5. Cerrar sistema")    
                print("-----------------------\n")    

                #Ingreso opcion para Menu de opciones.
                opcion = input("Ingrese una 'opcion Valida' entre 1 y  5 : ")

                #Validamos ingreso solo digitos.
                while not opcion.isdigit() :
                    print("Error. Ingreso una opcion invalida.")
                    opcion = input("Ingrese una 'opcion Valida' entre 1 y  5 : ")
                
                #Validacion de rango dias
                while int(opcion) < 1 or int(opcion) > 5:
                    print("Error. Ingreso una opcion menu fuera del rango. ")
                    opcion = input("Ingrese una 'opcion Valida' entre 1 y  5 : ")

                    while not opcion.isdigit() :
                        print("Error. Ingreso una opcion invalida.")
                        opcion = input("Ingrese una 'opcion Valida' entre 1 y  5 : ")
                
                opcion = int(opcion)

                #Opcion "Alta nuevo turno".
                if opcion == 1 :
                    print("\nBienvenido, va a Reservar un turno.")

                    dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Validacion del dia ingresado.
                    while not dia.isdigit() :
                        print("Error. Ingreso una opcion invalida de dia. ")
                        dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Validacion del rango de dias de atencion publico.
                    while int(dia) < 1 or int(dia)> 2 :
                        print("Error. Ingreso una opcion fuera de rango de dias. ")    
                        dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")
                        
                        #Validacion de dia ingresado valido.
                        while not dia.isdigit() :
                            print("Ingreso opcion ivalida de dia. ")
                            dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    dia = int(dia)  #Día ingresado correctamente, para alta turno.

                    #Ingreso de nombre paciente.
                    paciente = input("Ingrese el nombre del paciente. ")

                    #Validacion de paciente con nombre y solo letras. Nombre no vacio.
                    #isalpha() para validar solamente letras.
                    while paciente == "" or not paciente.isalpha() :
                        print("Error. Ingresar nombre sin numeros ni caracteres")
                        paciente = input("Ingrese el nombre del paciente. ")

                    #Eleccion del dia Lunes para turno.
                    if dia == 1 :
                        if paciente == tLunes1 or paciente == tLunes2 or paciente == tLunes3 or paciente == tLunes4 :
                            print("Error . El paciente YA tiene, un turno el dia Lunes")
                        elif tLunes1 == "" :
                            tLunes1 = paciente
                            print("Turno reservado para el dia Lunes - Turno N° 1")
                        elif tLunes2 == "" :
                            tLunes2 = paciente 
                            print("Turno reservado para el dia Lunes - Turno N° 2")
                        elif tLunes3 == "" :
                            tLunes3 = paciente
                            print("Turno reservado para el dia Lunes - Turno N° 3")
                        elif tLunes4 == "" :
                            tLunes4 = paciente
                            print("Turno reservado para el dia Lunes - Turno N° 4")
                        else:
                            print("Ya no hay turnos disponibles para el dia Lunes. 'Posible Turno' dia Martes. Consulte con secretaria. ")     

                    elif dia == 2:
                        if paciente == tMartes1 or paciente == tMartes2 or paciente == tMartes3 :
                            print("Error . El paciente YA tiene, un turno el dia Martes")       
                        elif tMartes1 == "" :
                            tMartes1 = paciente
                            print("Turno reservado para el dia Martes - Turno N° 1") 
                        elif tMartes2 == "" :
                            tMartes2 = paciente
                            print("Turno reservado para el dia Martes - Turno N° 2") 
                        elif tMartes3 == "" :
                            tMartes3 = paciente
                            print("Turno reservado para el dia Martes - Turno N° 3") 
                        else:
                            print("Ya no hay turnos disponibles para el dia Martes. ")
                
                #Opcion "Cancelar Turno "
                elif opcion == 2 :
                    print("\nBienvenido, va a Cancelar un turno")

                    dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Validacion del dia ingresado para cancelar turno.
                    while not dia.isdigit() :
                        print("Error. Ingreso una opcion invalida de dia. ")
                        dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Validacion del rango de dias de atencion publico.
                    while int(dia) < 1 or int(dia)> 2 :
                        print("Error. Ingreso una opcion fuera de rango de dias. ")    
                        dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")
                        
                        #Validacion de dia ingresado valido.
                        while not dia.isdigit() :
                            print("Ingreso opcion ivalida de dia. ")
                            dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Día cancelar turno, ingresado correctamente. 
                    dia = int(dia)  

                    #Ingreso nombre de paciente para cancelar turno.
                    paciente = input("\nIngrese el nombre del paciente para cancelar turno: ")  

                    #Validacion de paciente con nombre y solo letras. Nombre no vacio.
                    #isalpha() para validar solamente letras.
                    while paciente == "" or not paciente.isalpha() :
                        print("Error. Ingresar nombre sin numeros ni caracteres")
                        paciente = input("Ingrese el nombre del paciente para cancelar turno: ")

                    #Cancelacion de turnos pacientes        
                    #Cancelamos dia Lunes.
                    if dia == 1 :
                        if paciente == tLunes1 :
                            tLunes1 = ""
                            print("Turno 1 Lunes  - Cancelado correctamente.")
                        elif paciente == tLunes2 :
                            tLunes2 = ""
                            print("Turno 2 Lunes  - Cancelado correctamente.")
                        elif paciente == tLunes3 :
                            tLunes3 = ""
                            print("Turno 3 Lunes  - Cancelado correctamente.")
                        elif paciente == tLunes4 :
                            tLunes4 = ""
                            print("Turno 4 Lunes  - Cancelado correctamente.")
                        else:
                            print("El paciente no tiene turno para el dia Lunes. ")            

                    #Cancelamos dia Martes.
                    elif dia == 2:
                        if paciente == tMartes1 :
                            tMartes1 = ""
                            print("Turno 1 Martes  - Cancelado correctamente.")
                        elif paciente == tMartes2 :
                            tMartes2 = ""
                            print("Turno 2 Martes  - Cancelado correctamente.")
                        elif paciente == tMartes3 :
                            tMartes3 = ""
                            print("Turno 3 Martes  - Cancelado correctamente.")
                        else:            
                            print("El paciente no tiene turno para el dia Martes. ")     

                #Ver agenda del día
                elif opcion == 3 :
                    print("\nBienvenido, revisamos la agenda del día")

                    dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Validacion del dia ingresado para ver agenda turno.
                    while not dia.isdigit() :
                        print("Error. Ingreso una opcion invalida de dia. ")
                        dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Validacion del rango de dias de atencion publico.
                    while int(dia) < 1 or int(dia)> 2 :
                        print("Error. Ingreso una opcion fuera de rango de dias. ")    
                        dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")
                        
                        #Validacion de dia ingresado valido.
                        while not dia.isdigit() :
                            print("Ingreso opcion ivalida de dia. ")
                            dia = input("Ingrese dia valido (1=Lunes , 2=Martes) : ")

                    #Día ver agenda de turnos, ingresado correctamente. 
                    dia = int(dia)  

                    #Mostramos agendas de dias libres y ocupados de atencion al cliente. 
                    #Agenda dia Lunes.
                    if dia == 1:
                        print("\nAgenda del Lunes")
                        print(f"Turno 1: {tLunes1 if tLunes1 != '' else '(libre)'}")
                        print(f"Turno 2: {tLunes2 if tLunes2 != '' else '(libre)'}")
                        print(f"Turno 3: {tLunes3 if tLunes3 != '' else '(libre)'}")
                        print(f"Turno 4: {tLunes4 if tLunes4 != '' else '(libre)'}")

                    #Agenda dia Martes
                    elif dia == 2:     
                        print("\nAgenda del Martes")
                        print(f"Turno 1: {tMartes1 if tMartes1 != '' else '(libre)'}")
                        print(f"Turno 2: {tMartes2 if tMartes2 != '' else '(libre)'}")
                        print(f"Turno 3: {tMartes3 if tMartes3 != '' else '(libre)'}")

                #Ver resumen general turnos 
                elif opcion == 4 :
                    print("\nOpcion seleccionada Ver resumen general")
                    tOcupadosLunes=0
                    tOcupadosMartes=0

                    #Analizamos individualmente por dias.
                    #Dia Lunes
                    if tLunes1 != "" :
                        tOcupadosLunes +=1
                    if tLunes2 != "" :
                        tOcupadosLunes +=1
                    if tLunes3 != "" :
                        tOcupadosLunes +=1
                    if tLunes4 != "" :
                        tOcupadosLunes +=1  
                    #Dia Martes    
                    if tMartes1 != "" :
                        tOcupadosMartes +=1  
                    if tMartes2 != "" :
                        tOcupadosMartes +=1  
                    if tMartes3 != "" :
                        tOcupadosMartes +=1  

                    #Calculo ocupacion en dias.
                    tDisponiblesLunes  = 4 - tOcupadosLunes           
                    tDisponiblesMartes = 3 - tOcupadosMartes          

                    print("\nResumen general")
                    print(f"Lunes -> Ocupados: {tOcupadosLunes} | Disponibles: {tDisponiblesLunes}")
                    print(f"Martes -> Ocupados: {tOcupadosMartes} | Disponibles: {tDisponiblesMartes}")

                    if tOcupadosLunes > tOcupadosMartes:
                        print("Dia con mas turnos: Lunes")
                    elif tOcupadosMartes > tOcupadosLunes:
                        print("Dia con mas turnos: Martes")
                    else:
                        print("Hay empate entre Lunes y Martes")
                
                #Opcion salir del sistema.
                elif opcion == 5 :
                    print("\nSistema cerrado , hasta la proxima.!! ")         

        case 4:
            print("---------------------------")
            print("\nIngresaste al Ejercicio 4\n")
            print("---------------------------")

            #Ejercicio 4 — Escape Room: La Bóveda

            #Variables iniciales
            energia =100
            tiempo = 12
            cerraduras_abiertas = 0
            alarma =False
            codigo_parcial = ""
            forzar_seguidas = 0 #cuenta las veces seguidas, que hacemos el intento de abrir la cerradura.

            nombre_agente = input("Ingresar el nombre del agente: ")

            #Validacion del nombre del agente.
            while nombre_agente == "" or not nombre_agente.isalpha():
                print("Error. El nombre del agente invalido. ") 
                nombre_agente = input("Ingresar el nombre del agente: ")

            while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 :
                print("\n--------Estado Actual----------")
                print(f"Agente: {nombre_agente}")
                print(f"Energia: {energia}")
                print(f"Tiempo: {tiempo}")
                print(f"Cerraduras Abiertas : {cerraduras_abiertas}")
                print(f"Alarma: {alarma}")
                print(f"Codigo Parcial: {codigo_parcial}")
                print("--------------------------------------\n")

                #Opciones de seleccion.
                print("1. Forzar cerradura")
                print("2. Hackear panel")
                print("3. Descansar")

                opcion = input("Ingrese una opcion valida entre 1 y 3:  ")

                #Validacion de opcion inicial menu
                while not opcion.isdigit() :
                    print("Error. Ingreso una opcion invalida. ")
                    opcion = input("Ingrese una opcion valida entre 1 y 3:  ")

                #Validacion del rango de opciones validas.
                while int(opcion) < 1 or int(opcion) > 3 :
                    print("Error. Ingreso una opcion fuera de rango. ")    
                    opcion = input("Ingrese una opcion valida entre 1 y 3:  ")

                    #Validacion de opcion inicial menu
                    while not opcion.isdigit() :
                        print("Error. Ingreso una opcion invalida. ")
                        opcion = input("Ingrese una opcion valida entre 1 y 3:  ")
                
                opcion = int(opcion)

                #Opcion 1 : Forzar cerradura
                if opcion == 1:
                    print("\nSelecciono: Forzar cerradura")
                    energia -= 20
                    tiempo -= 2
                    forzar_seguidas += 1

                    #No abre cerradura y activa alarma,luego de 3 intentos.
                    if forzar_seguidas == 3:
                        alarma = True
                        print("La cerradura se trabo por forzar 3 veces seguidas.")
                        
                    
                    else:
                        #Energia por debajo de 40, riesgo de alarma
                        if energia < 40:
                            riesgo = input("Riesgo de alarma. Ingrese un numero entre 1 y 3: ")

                            while not riesgo.isdigit():
                                print("Error. Ingreso invalido.")
                                riesgo = input("Riesgo de alarma. Ingrese un numero entre 1 y 3: ")

                            while int(riesgo) < 1 or int(riesgo) > 3:
                                print("Error. Numero fuera de rango.")
                                riesgo = input("Riesgo de alarma. Ingrese un numero entre 1 y 3: ")

                                while not riesgo.isdigit():
                                    print("Error. Ingreso invalido.")
                                    riesgo = input("Riesgo de alarma. Ingrese un numero entre 1 y 3: ")

                            riesgo = int(riesgo)

                            if riesgo == 3:
                                alarma = True
                                print("Se activo la alarma por forzar con poca energia.")

                        #No hay alarma, abre una cerradura
                        if alarma == False:
                            cerraduras_abiertas += 1
                            print("Se abrio 1 cerradura correctamente.")
                        else:
                            print("No se pudo abrir la cerradura por la alarma.")

                #Opcion 2 : Hackear panel
                elif opcion == 2:
                    print("\nSelecciono: Hackear panel")
                    energia -= 10
                    tiempo -= 3
                    forzar_seguidas = 0   

                    print("Iniciando hackeo...")

                    for paso in range(1, 5):
                        codigo_parcial += "A"
                        print(f"Paso {paso}/4 completado - Codigo parcial: {codigo_parcial}")

                    if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                        cerraduras_abiertas += 1
                        print("El hackeo fue exitoso. Se abrio 1 cerradura automaticamente.")
                    else:
                        print("Hackeo parcial realizado. Falta para abrir una cerradura.")

                #Opcion 3 : Descanso agente
                elif opcion == 3:
                    print("\nSelecciono: Descansar")
                    energia += 15
                    tiempo -= 1
                    forzar_seguidas = 0   

                    if energia > 100:
                        energia = 100

                    if alarma == True:
                        energia -= 10
                        print("La alarma sigue activa. Se pierden 10 puntos extra de energia.")

                    print("Descanso realizado correctamente.")

                #Bloqueo por alarma
                if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
                    bloqueado = True
                    print("\nSistema bloqueado por alarma.")
                    print("Perdiste la partida.")

            #Condiciones finales
            if cerraduras_abiertas == 3 and energia > 0 and tiempo > 0 and bloqueado == False:
                print("\nVICTORIA")
                print(f"Felicitaciones agente {nombre_agente}, abriste la bóveda.")
            elif bloqueado == True:
                print("\nDERROTA POR BLOQUEO")
            elif energia <= 0 or tiempo <= 0:
                print("\nDERROTA")
                print("Te quedaste sin energia o sin tiempo.")

        case 5:
            print("---------------------------")
            print("\nIngresaste al Ejercicio 5\n")
            print("---------------------------")

            #Ejercicio 5 — “Escape Room:"La Arena del Gladiador

            import random
            nombre_gladiador=input("Ingrese el nombre del gladiador: ")

            while nombre_gladiador=="" or not nombre_gladiador.isalpha():
                print("Error: Solo se permiten letras")
                nombre_gladiador=input("Ingrese el nombre del gladiador: ")

            nombre_gladiador=nombre_gladiador.capitalize()

            vida_gladiador = 100
            vida_enemigo = 100
            pociones_vida = 3 
            danio_base_gladiador = 15 
            danio_base_enemigo = 12
            turno_gladiador=True

            while vida_gladiador>0 and vida_enemigo>0:
                if turno_gladiador:
                    print(f"La vida de {nombre_gladiador} es {vida_gladiador}")
                    print(f"La vida del enemigo es {vida_enemigo}")
                    print(f"Cantidad de pociones de cura disponibles {pociones_vida}")
                    while True:
                        opcion=input('''
                            Indique la accion a realizar:
                            1)Ataque pesado
                            2)Ataque por rafaga
                            3)Curar
                            ''')
                        while opcion=="" or not opcion.isdigit():
                            print("Error: Solo se permiten numeros")
                            opcion=input('''
                            Indique la accion a realizar:
                            1)Ataque pesado
                            2)Ataque por rafaga
                            3)Curar
                            ''')
                        opcion=int(opcion)
                        match opcion:
                            case 1:
                                if vida_enemigo<20:
                                    vida_enemigo=vida_enemigo-1.5*danio_base_gladiador
                                    print(f"Atacaste al enemigo por {1.5*danio_base_gladiador} puntos de daño")
                                else:
                                    vida_enemigo=vida_enemigo-danio_base_gladiador
                                    print(f"Atacaste al enemigo por {danio_base_gladiador} puntos de daño")
                                turno_gladiador=False
                                break
                            case 2:
                                rafaga=random.randint(1,4)
                                for _ in range(rafaga):
                                    vida_enemigo-=5
                                    print("> Golpe conectado por 5 de daño")
                                turno_gladiador=False
                                break
                            case 3:
                                if pociones_vida>0:
                                    vida_gladiador=vida_gladiador+30
                                    pociones_vida-=1
                                    print(f"Te curaste, tu vida sube a {vida_gladiador}")
                                    print(f"Las pociones de cura quedan en {pociones_vida} pociones restantes.")
                                else:
                                    print("No dispone de mas pociones de vida")
                                    print("Pierdes el turno")
                                turno_gladiador=False
                                break
                            case _:
                                print("La opcion ingresada no es valida")
                                print("Intente de nuevo")
                else:
                    print("Turno de ataque del enemigo!!")
                    vida_gladiador=vida_gladiador-danio_base_enemigo
                    print("¡El enemigo te atacó por 12 puntos de daño!")
                    turno_gladiador=True

            if vida_gladiador>0:
                print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
            else:
                print(f"DERROTA. Has caído en combate.")     



        case 6:    
            print("\nOpcion salir del Menu")    