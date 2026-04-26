# Ejercicio 1 — “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total. 

# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).
# 3. Por cada producto (usar for): Pedir precio (entero, validar .isdigit()). Pedir si tiene descuento S/N (validar con while, aceptar s o n en cualquier mayuscula/minuscula). Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar: Total sin descuentos, total con descuentos, ahorro total, promedio por producto (usar float y formatear con .2f).

nombre_cliente = input("Ingrese su nombre: ")
while not nombre_cliente.isalpha():
    print("Ingrese sólo letras.")
    nombre_cliente = input("Ingrese su nombre: ")
cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
while not cantidad_productos.isdigit() or int(cantidad_productos) <= 0:
    print("Ingrese un número entero positivo.")
    cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")
cantidad_productos = int(cantidad_productos)
total_sin_descuentos = 0
total_con_descuentos = 0
for i in range(cantidad_productos):
    precio = input (f"Ingrese el precio del producto {i+1}: ")
    while not precio.isdigit():
        print("Ingrese un número entero para el precio.")
        precio = input (f"Ingrese el precio del producto {i+1}: ")
    precio = int(precio)
    descuento = input("Tiene descuento? (S/N): ")
    while descuento.lower() not in ("s", "n"):
        print("Ingrese S o N: ")
        descuento = input("Tiene descuento? (S/N): ")
    print(f"Producto {i+1} - precio: {precio} - Descuento: {descuento}")
    if descuento.lower() == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio
    total_sin_descuentos += precio
    total_con_descuentos += precio_final
ahorro = total_sin_descuentos - total_con_descuentos
promedio = total_con_descuentos / cantidad_productos    
print(f"nombre_cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")
print(f"Total sin descuentos: ${total_sin_descuentos:.2f}")
print(f"Total con descuentos: ${total_con_descuentos:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")

# Ejercicio 2 — “Acceso al Campus y Menú Seguro”
# Objetivo: Login con intentos + menú de acciones con validación estricta.

# 1. Definir credenciales fijas en el código: usuario correcto: "alumno", clave correcta: "python123".
# 2. Permitir máximo 3 intentos para ingresar usuario y clave. 
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar. 
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir: 1. Ver estado de inscripción (mostrar “Inscripto”). 2. Cambiar clave (pedir nueva clave y confirmación; deben coincidir). 3. Mostrar mensaje motivacional (1 frase). 4. Salir 
# 5. Validación del menú: Debe ser número (.isdigit()), debe estar entre 1 y 4.
# Cambio de clave: La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.

usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
while intentos < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Bienvenido al campus virtual")
        while True:
            print("Menú:")
            print("1. Ver estado de inscripción")
            print("2. Cambiar clave")
            print("3. Mostrar mensaje motivacional")
            print("4. Salir")
            opcion = input("Ingrese una opción (1-4): ")
            if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
                print("Opción inválida. Ingrese un número entre 1 y 4.")
                continue
            opcion = int(opcion)
            if opcion == 1:
                print("Estado de inscripción: Inscripto")
            elif opcion == 2:
                nueva_clave = input("Ingrese la nueva clave (mínimo 6 caracteres): ")
                if len(nueva_clave) < 6:
                    print("La clave debe tener al menos 6 caracteres.")
                else:
                    confirmacion = input("Confirme la nueva clave: ")
                    if nueva_clave == confirmacion:
                        clave_correcta = nueva_clave
                        print("Clave cambiada exitosamente.")
                    else:
                        print("Las claves no coinciden.")
            elif opcion == 3:
                print("¡Estás haciendo un gran trabajo!")
            elif opcion == 4:
                print("Gracias por visitar el campus virtual. ¡Hasta luego!")
                break
        break
    else:
        intentos += 1
        print(f"Usuario o clave incorrectos. Intento {intentos} de 3.")
    if intentos == 3:
        print("Cuenta bloqueada.")

# Ejercicio 3 — “Agenda de turnos con nombres (sin listas)”
# Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos: Lunes: 4 turnos, Martes: 3 turnos. 
# Reglas: 1. Pedir nombre del operador (solo letras). 
# 2. Menú repetitivo hasta salir: 
    # 1. Reservar turno 
    # 2. Cancelar turno (por nombre) 
    # 3. Ver agenda del día 
    # 4. Ver resumen general 
    # 5. Cerrar sistema 
# 3. Reservar: Elegir día (1=Lunes, 2=Martes). Pedir nombre del paciente (solo letras). Verificar que no esté repetido en ese día (comparando con las variables ya cargadas). Guardar en el primer espacio libre (ej. lunes1, lunes2…). 
# 4. Cancelar: Elegir día. Pedir nombre del paciente (solo letras). Si existe, cancelar y dejar el espacio vacío (""). 
# 5. Ver agenda del día: Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
# 6. Resumen general: Turnos ocupados y disponibles por día. Día con más turnos (o empate).
# Restricciones:  No listas, no diccionarios, no sets, no tuplas. Se permite usar "" como “vacío”. Validaciones con .isalpha() y .isdigit() (sin try/except).

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("Ingrese el nombre del operador: ")
    if operador.isalpha():
        break
    else:
        print("El nombre del operador debe contener solo letras.")
while True:
    print("\nMenú:")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")
    opcion = input("Ingrese una opción (1-5): ")
    if not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        if opcion == "2":
            print("Para cancelar un turno, primero debe reservarlo.")
        print("Opción inválida. Ingrese un número entre 1 y 5.")
        continue
    opcion = int(opcion)
    if opcion == 1:
        dia = input("Elija un día (1=Lunes, 2=Martes): ")
        while dia not in ("1", "2"):
            print("Opción inválida. Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elija un día (1=Lunes, 2=Martes): ")
        paciente = input("Ingrese el nombre del paciente: ")
        if not paciente.isalpha():
                print("El nombre del paciente debe contener solo letras.")
                continue
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                print("\nEl paciente ya tiene un turno reservado el lunes.")
            elif lunes1 == "":
                lunes1 = paciente
                print(f"Turno reservado para {paciente} el lunes.")
            elif lunes2 == "":
                lunes2 = paciente
                print(f"\nTurno reservado para {paciente} el lunes.")
            elif lunes3 == "":
                lunes3 = paciente
                print(f"\nTurno reservado para {paciente} el lunes.")
            elif lunes4 == "":
                lunes4 = paciente
                print(f"\nTurno reservado para {paciente} el lunes.")
            else:
                print("\nNo hay más turnos disponibles el lunes.")
        elif dia == "2":
            if paciente == martes1 or paciente == martes2 or paciente == martes3:
                print("\nEl paciente ya tiene un turno reservado el martes.")
            elif martes1 == "":
                martes1 = paciente
                print(f"\nTurno reservado para {paciente} el martes.")
            elif martes2 == "":
                martes2 = paciente
                print(f"\nTurno reservado para {paciente} el martes.")
            elif martes3 == "":
                martes3 = paciente
                print(f"\nTurno reservado para {paciente} el martes.")
            else:
                print("\nNo hay más turnos disponibles el martes.")
    elif opcion == 2:
        dia = input("Elija un día (1=Lunes, 2=Martes): ")
        while dia not in ("1", "2"):
            print("Opción inválida. Ingrese 1 para Lunes o 2 para Martes.")
            dia = input("Elija un día (1=Lunes, 2=Martes): ")
        paciente = input("Ingrese el nombre del paciente: ")
        if not paciente.isalpha():
                print("El nombre del paciente debe contener solo letras.")
                continue
        if dia == "1":
            if lunes1 == paciente:
                lunes1 = ""                
                print(f"Turno cancelado para {paciente} el lunes.")
            elif lunes2 == paciente:
                lunes2 = ""
                print(f"Turno cancelado para {paciente} el lunes.")
            elif lunes3 == paciente:
                lunes3 = ""
                print(f"Turno cancelado para {paciente} el lunes.")
            elif lunes4 == paciente:
                lunes4 = ""
                print(f"Turno cancelado para {paciente} el lunes.")
            else:
                print(f"\nNo se encontró un turno reservado para {paciente} el lunes.")
        elif dia == "2":
            if martes1 == paciente:
                martes1 = ""
                print(f"Turno cancelado para {paciente} el martes.")
            elif martes2 == paciente:
                martes2 = ""
                print(f"Turno cancelado para {paciente} el martes.")
            elif martes3 == paciente:
                martes3 = ""
                print(f"Turno cancelado para {paciente} el martes.")
            else:
                print(f"\nNo se encontró un turno reservado para {paciente} el martes.")
    elif opcion == 3:
        print("Turno 1: lunes", lunes1 if lunes1 != "" else "(libre)")
        print("Turno 2: lunes", lunes2 if lunes2 != "" else "(libre)")
        print("Turno 3: lunes", lunes3 if lunes3 != "" else "(libre)")
        print("Turno 4: lunes", lunes4 if lunes4 != "" else "(libre)")
        print("Turno 1: martes", martes1 if martes1 != "" else "(libre)")
        print("Turno 2: martes", martes2 if martes2 != "" else "(libre)")
        print("Turno 3: martes", martes3 if martes3 != "" else "(libre)")
    elif opcion == 4:
        ocupados_lunes = 0
        ocupados_martes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1
        disponibles_lunes = 4 - ocupados_lunes
        disponibles_martes = 3 - ocupados_martes
        if ocupados_lunes > ocupados_martes:
                    print(f"El lunes tiene más turnos ocupados ({ocupados_lunes}) que el martes ({ocupados_martes}).")
        elif ocupados_martes > ocupados_lunes:
            print(f"El martes tiene más turnos ocupados ({ocupados_martes}) que el lunes ({ocupados_lunes}).")
        else:
            print(f"El lunes y el martes tienen la misma cantidad de turnos ocupados ({ocupados_lunes} {ocupados_martes}).")
    elif opcion == 5: # cerrar sistema
        print("Cerrando sistema. ¡Hasta luego!")
        break

# Ejercicio 4  — “Escape Room: La Bóveda” 
# Historia: Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo limitados. Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás. 
# Variables iniciales (NO se piden por teclado): energia = 100, tiempo = 12, cerraduras_abiertas = 0, alarma = False, codigo_parcial = "".
# Validaciones obligatorias: No usar try/except. 
# Pedir nombre del agente y validar con .isalpha() en un while. Validar opciones del menú y cualquier número pedido con .isdigit() en un while. El juego debe funcionar con estructuras secuenciales, condicionales y repetitivas (puede usar funciones propias del lenguaje como .lower(), len(), formateo, etc.).
# Regla anti-spam: Para evitar que el jugador gane eligiendo “Forzar cerradura” 3 veces seguidas al iniciar: se cobra el costo normal (-20 energía, -2 tiempo), NO abre cerradura, y se activa la alarma automáticamente (alarma = True) porque “la cerradura se trabó”. Si el jugador elige opción 2 o 3, se corta la racha de “forzar seguidas”.
# Menú de acciones (se repite mientras el juego siga)
# El juego continúa mientras: energia > 0, tiempo > 0, cerraduras_abiertas < 3, y no esté bloqueado por alarma.
# En cada turno mostrar el estado y el siguiente menú: 
# 1. Forzar cerradura (costo: -20 energía, -2 tiempo) 
# Si la energía está por debajo de 40, hay “riesgo de alarma”: pedir un número 1-3 (validado). Si elige 3 → alarma=True. 
# Si no hay alarma, abre 1 cerradura. 
# Regla anti-spam: si es la 3ra vez seguida forzando, se activa alarma y no abre. 
# 2. Hackear panel (costo: -10 energía, -3 tiempo) 
# Debe usar un for de 4 pasos mostrando progreso. 
# En cada paso sumar una letra al codigo_parcial (por ejemplo “A”). 
# Si len(codigo_parcial) >= 8, se abre automáticamente 1 cerradura si todavía faltan. 
# 3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra).
# Regla de bloqueo por alarma: Si alarma == True y tiempo <= 3 y todavía no se abrió la bóveda, el sistema se bloquea y se pierde.
# Condiciones de fin 
# Si cerraduras_abiertas == 3 → VICTORIA 
# Si energia <= 0 o tiempo <= 0 → DERROTA 
# Si se bloquea por alarma → DERROTA (bloqueo)

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzadas_seguidas = 0

nombre_agente = input("Ingrese el nombre del agente: ")
while not nombre_agente.isalpha():
    print("Nombre inválido. Por favor, ingrese solo letras.")
    nombre_agente = input("Ingrese el nombre del agente: ")
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
        print(f"\nEstado actual: Energía = {energia}, tiempo = {tiempo}, cerraduras abiertas = {cerraduras_abiertas}, alarma = {alarma}")
        print("\nMenú de acciones:")
        print("1. Forzar cerradura")
        print("2. Hackear panel")
        print("3. Descansar")
        opcion = input("Seleccione una opción (1, 2 o 3): ")
        while not opcion.isdigit() or opcion not in ['1', '2', '3']:
            print("Opción inválida. Por favor, seleccione 1, 2 o 3.")
            opcion = input("Seleccione una opción (1, 2 o 3): ")
        if opcion == '1':
            energia -= 20
            tiempo -= 2
            forzadas_seguidas += 1
            if forzadas_seguidas == 3:
                alarma = True
                print("¡Alarma activada! La cerradura se trabó.")
            elif energia < 40:
                riesgo_alarma = input("¡Riesgo de alarma! Ingrese un número del 1 al 3: ")
                while not riesgo_alarma.isdigit() or riesgo_alarma not in ['1', '2', '3']:
                    print("Número inválido. Por favor, ingrese un número del 1 al 3.")
                    riesgo_alarma = input("¡Riesgo de alarma! Ingrese un número del 1 al 3: ")
                if riesgo_alarma == '3':
                    alarma = True
                    print("¡Alarma activada!")
                else:
                    cerraduras_abiertas += 1
                    print("Cerradura abierta.")
            else:
                cerraduras_abiertas += 1
                print("Cerradura abierta.")
        elif opcion == '2':
            energia -= 10
            tiempo -= 3
            for paso in range(1, 5):
                print(f"Hackeando... Paso {paso}/4")
                codigo_parcial += "A"
                print(f"Código parcial: {codigo_parcial}")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura abierta automáticamente por código completo.")
        elif opcion == '3':
            energia += 15
            if energia > 100:
                energia = 100
            tiempo -= 1
            if alarma:
                energia -= 10
                print("Alarma activa: energía reducida extra.")
        if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
            print("¡Sistema bloqueado por alarma! Has perdido.")
            break
if cerraduras_abiertas == 3:
    print("¡VICTORIA! Has abierto la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print("¡DERROTA! Te has quedado sin energía o tiempo.")

# Ejercicio 5  — “Escape Room: "La arena del gladiador"
# 1. Descripción del Escenario: Vas a desarrollar un simulador de batalla por turnos en Python. El programa enfrentará a un usuario (Gladiador) contra un oponente controlado por la computadora (enemigo). El objetivo es reducir los puntos de vida del oponente a cero antes de que él lo haga contigo. Este ejercicio evalúa el uso de variables (int, float, string, boolean), estructuras de control (if/elif/else), ciclos (while y for) y validación de datos estricta.
# 2.  Requerimientos Técnicos:
# A. Tipos de Datos  
# Debes utilizar obligatoriamente los siguientes tipos de datos para las variables del juego: 
# String: Para el nombre del jugador.  
# Int: Para los puntos de vida (HP) y cantidad de pociones.  
# Float: Para el cálculo del daño (ej: un golpe crítico multiplica el ataque por 1.5).
# Boolean: Para controlar si el juego sigue activo o quién tiene el turno.
# B.  Reglas de validación (¡Importante!)
# No está permitido usar bloques try / except.
# Para validar texto, debes usar el método .isalpha() dentro de un ciclo while.
# Para validar números, debes usar el método .isdigit() dentro de un ciclo while.
# 3. Flujo del Programa
# Paso 1: Configuración del personaje.
# El programa inicia pidiendo el nombre del gladiador.
# Validación: El nombre solo puede contener letras. Si el usuario ingresa números, símbolos o lo deja vacío, el programa debe decir "Error: Solo se permiten letras" y volver a preguntar hasta que sea válido.
# Paso 2: Inicialización de Estadísticas 
# El programa debe definir las variables iniciales (sin preguntar al usuario):  
# • Vida del Gladiador: 100 (int)  
# • Vida del Enemigo: 100 (int)  
# • Pociones de Vida: 3 (int)  
# • Daño base "Ataque Pesado": 15 (int)  
# • Daño base del enemigo: 12 (int)  
# • Turno Gladiador : True (booleano) 
# Paso 3: El ciclo de combate:
# El juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
# Turno de jugador: Muestra la vida actual de ambos y las pociones restantes. Luego, ofrece un menú con 3 opciones:
# 1. Ataque pesado.
# 2. Rafaga veloz. (Requiere uso de for).
# 3. Curar. 
# 4. Validación del Menú: El programa debe pedir la opción al usuario. 1. Verificar que lo ingresado sea un número (.isdigit()). 2. Verificar que el número sea 1, 2 o 3. Si falla alguna validación, mostrar mensaje de error y volver a pedir.
# Lógica de las acciones: 
# Acción A: Acción ataque pesado: (Opción 1): Calcula el daño final. Si la vida del enemigo es menor a 20 puntos, el jugador realiza un "golpe crítico" multiplicando su daño base por 1.5 (resultado float). Resta el daño a la vida del enemigo. Muestra un mensaje: "¡Atacaste al enemigo por X puntos de daño!"
# Acción B: Ráfaga veloz (Opción 2): Esta acción realiza una serie de golpes rápidos. Debes implementar un bucle for. El bucle debe repetirse 3 veces (usando range).
# Dentro del bucle, en cada repetición: 
# 1. Resta 5 puntos de daño a la vida del enemigo.  
# 2. Muestra el mensaje: ">Golpe conectado por 5 de daño".
# Acción C: Curar (Opción 3): Si tienes pociones (> 0): Suma 30 puntos a tu vida y resta 1 poción. Si NO tienes pociones: Muestra "¡No quedan pociones!" y pierdes el turno (el enemigo ataca igual).
# Turno del Enemigo: Justo después de tu acción, el enemigo ataca automáticamente.  
# Resta el daño base del enemigo (12) a tu vida.  
# Muestra un mensaje: "¡El enemigo te atacó por 12 puntos de daño!"
# Paso 4: Fin del juego.
# Cuando el ciclo termine (porque la vida de alguno llegó a 0 o menos), debes evaluar:  
# Si vida_jugador > 0: Mostrar "¡VICTORIA! [Nombre] ha ganado la batalla."  
# Si vida_jugador <= 0: Mostrar "DERROTA. Has caído en combate."

nombre = input("Ingresa el nombre de tu gladiador: ")
while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Ingresa el nombre de tu gladiador: ")
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado = 15
ataque_rapido = 5
daño_enemigo = 12
turno_gladiador = True
while vida_jugador > 0 and vida_enemigo > 0:
    if turno_gladiador:
        print(f"\n{nombre} - Vida: {vida_jugador} | Enemigo - Vida: {vida_enemigo} | Pociones: {pociones}")
        print("1. Ataque pesado")
        print("2. Ráfaga veloz")
        print("3. Curar")
        opcion = input("Elige tu acción (1, 2 o 3): ")
        while not opcion.isdigit() or opcion not in ['1', '2', '3']:
            print("Error: Opción inválida. Elige 1, 2 o 3.")
            opcion = input("Elige tu acción (1, 2 o 3): ")
        
        if opcion == '1':
            daño_final = ataque_pesado
            if vida_enemigo < 20:
                daño_final *= 1.5
            vida_enemigo -= daño_final
            print(f"\n¡Atacaste al enemigo por {daño_final:.2f} puntos de daño!")
        
        elif opcion == '2':
            for _ in range(3):
                vida_enemigo -= ataque_rapido
                print("> Golpe conectado por 5 de daño")
        
        elif opcion == '3':
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("¡Te has curado por 30 puntos de vida!")
            else:
                print("¡No quedan pociones! Pierdes el turno.")
        
        turno_gladiador = False
    
    else:
        vida_jugador -= daño_enemigo
        print(f"\n¡El enemigo te atacó por {daño_enemigo} puntos de daño!")
        turno_gladiador = True
if vida_jugador > 0:
    print(f"¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA. Has caído en combate.")