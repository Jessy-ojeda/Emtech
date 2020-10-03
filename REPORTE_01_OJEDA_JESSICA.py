 #para iniciar, se importan los datos con los que trabajaremos:
from lifestore_file import lifestore_products , lifestore_sales ,  lifestore_searches 


#Suponiendo que ya hay cuentas registradas vamos a generar una lista que contenga los usuarios-admi y sus contraseñas

usuarios_admi = [["Priscila", "00aa"], ["Mario", "11bb"], ["Rafael", "22cc"], ["Ulises", "33dd"]]

#Para el inicio de sesion se mostrará primero un menú, en donde le sea posible al usuario elegir entre iniciar sesion o registrarse en caso de que no tener una cuenta.

respuesta = input ("""Hola, Bienvenido(@) a life Store 
Si deseas iniciar sesión escribe \"sesion\"
Si aun no te has registrado escribe \"registro\" 

""")

#debido a que mas adelante se utiliza "for" para iterar y comparar los datos de las variables "usuario"-"pasword"  para los usuarios que iniciaran sesion y las variables "usuario_new"-"password_new" para los usuarios que requiere registrarse, fue necesario declarar estas variables para no tener problema respecto a la existencia de las variables que no itroduzca nuestro usuario 

usuario = 0
password = 0
usuario_new = 0
password_new = 0 

#para decidir el camino que tomara el programa de acuerdo a lo que quiere realizar nuestro usuario, es necesario personalizar los mensajes que se mostraran y las vias que se seguiran segun sean las variables de entrada de la instruccion anterior. 
#entonces, tendremos 3 vias distintas de acuerdo a las 3 posibles variables de entrada 
#via 1: si el usuario escribe de acuerdo a la intrucccion anterior, la palabra "sesion" el programa le solicitara usuario y contraseña
#via 2: si el usuario escribe la palabra "registro" el programa le solicitara crear nombre de usuario y contrase;a y posterior a ello, se agregaran estas variables a la lista de "usuarios_admi"
#*IMPORTANTE* solo se le permitira al usuario crear su nombre de usuario y contraseña, si escribe correctamente la contrase;a que le otorgaron en gerencia: de esta forma evitamos que cualquier persona pueda regitrarse como usuario-administrador 
#via 3: si el usuario escribe alguna otra palabra o caracter que no sea "sesion" o "registro" se le mostrará una leyenda que le indique que su respuesta es invalida, y se le invita a ejecutar el programa de nuevo. 
#para que el programa terminara despues de un error, fue necesario incorporar las intrucciones a un bucle while, el cual terminará si la condicion deja de cumplirse, ademas nos permite utilizar esta condicion mas adelante para evitar que se muestre el resto de opciones (lo cual fue muy dificil de resolver U_U)
this = 0 
while this == 0 :
  if respuesta == "sesion":
    usuario = input ("escribe tu usuario: ")
    password = input ("escribe tu contraseña: ")
    break
    continue
  elif respuesta == "registro":
    password_registro = input ("escribe la contraseña que te otorgó gerencia para registrarte ") 
    if password_registro == "cielito":
      usuario_new = input ("crea tu nombre de usuario: ")
      password_new= input ("crea tu contraseña:  ")
      usuarios_admi.append ([usuario_new]+[password_new])
      this += 1
    else:
      print ("respuesta incorrecta, por favor solicita la contraseña a gerencia ")
      this +=1
  else:
    print ("respuesta invalida, intentalo de nuevo")
    this += 1  

#coloque una bandera para indicar que usuario siempre sera falso a menos que las variabes de entrada (usuario-password)(usuari_new-password_new) coincidan con los datos dentro de la lista "usuarios_admi"
#en caso de coincidir se le indicara una leyenda al uuario de "Bienvenido al menú"

usuario_correcto = 0 
for admi in range(0,len(usuarios_admi)):
  if (usuarios_admi[admi][0] == usuario   and usuarios_admi[admi][1] == password) or (usuarios_admi[admi][0] == usuario_new and usuarios_admi[admi][1] == password_new)  :
    print ("""
Bienvenido al menú """ + (usuario or usuario_new))
    usuario_correcto = 1 
    break

#en caso de que el usuario, contraseña o ambos sean incorrectos se le darán al usuario  dos oportunidades de ingresar, en caso de fallar ambas el programa termina y le da una da una leyenda que indica que fallo en ambos intentos, solicitandole que se comunique con gerencia
contador = 0
while  usuario_correcto == 0 and contador < 3 and this ==0 :
  print("""
  contraseña o usuario incorrectos, vuelve a intentarlo
  (tienes 3 oportunidades)
  """ )
  usuario = input ("escribe tu usuario: ")
  password = input ("escribe tu contraseña: ")
  contador += 1
  print ("No. de oportunidades que te quedan: ", (3-contador))
  for admi in range(0,len(usuarios_admi)):
    if usuarios_admi[admi][0] == usuario and usuarios_admi[admi][1] == password:
      print ("Bienvenido al menú "+ usuario)
      usuario_correcto = 1 
      break
if usuario_correcto == 0 and this == 0 :
  print("fallaste los dos intentos, por favor comunicate con gerencia")
  exit()

#en caso de haber ingresado o registrado de manera correcta, el programa le abrira el menú al usuario-administrador
if usuario_correcto == 1:
  opcion_menu= input  ("""
escribe el numero de opcion que desees visualizar
1: 50 productos con mayores ventas
2: 100 productos con mayor búsquedas
3: los 20 productos con las mejores reseñas
4: los 20 productos con las peores reseñas
5: total de ingresos mensual
6: total de ingresos anual
7: ventas promedio mensuales
8: meses con más ventas al año
""")



#Codigo para opcion 1 "50 productos con mayores ventas"
#para realizar esta opcion, fue necesario crear una lista nombrada "producto_ventas en la que se incluyo un contador para las ventas, es decir el numero de ventas por producto, posterior a ello se necesitó ordenar de mayor a menor de acuerdo al numero de ventas. Para la impresion solo fue necesario llamar a los elementos del 0-50 para el caso de que el usuario eligiera la opcion 1"
contador_ventas = 0 
producto_ventas = []
for producto in lifestore_products:
  for idlist_ventas in lifestore_sales:
    if producto[0]== idlist_ventas[1]:
      contador_ventas += 1 

  cuerpo_lista = [producto[0], producto[1],producto[3],contador_ventas]
  producto_ventas.append(cuerpo_lista)
  contador_ventas = 0

ventas_ordenadas = []
while producto_ventas:
  ordenar = producto_ventas[0][3]
  sin_ordenar = producto_ventas [0]
  for ventas in producto_ventas:
    if ventas [3] > ordenar:
        ordenar = ventas[3]
        sin_ordenar = ventas
  ventas_ordenadas.append(sin_ordenar)
  producto_ventas.remove(sin_ordenar)
#Fin de odigo para opcion 1 "50 productos con mayores ventas"


#Inicio de codigo para opcion 2 "100 productos con mayor búsquedas"
#para la opcion 2 fue necesario contar las busquedas por cada producto y agregarlas a una variable, despues de tener este numero dentro de una lista que fue creada y nombrada como "producto busquedas" se ordenaron los productos de acuerdo a el mayornumero de busquedas, para la impresion de la opsion 2 solo necesitamos llamar a los productos en un rango del 0 al 96, ya que no tenemos los 100 productos. 
contador_busquedas = 0 
producto_busquedas = []
for producto in lifestore_products:
  for idlist_busquedas in lifestore_searches:
    if producto[0]== idlist_busquedas[1]:
      contador_busquedas += 1 

  cuerpo_busqueda = [producto[0], producto[1],producto[3], contador_busquedas]
  producto_busquedas.append(cuerpo_busqueda)
  contador_busquedas = 0

busquedas_ordenadas = []
while producto_busquedas:
  ordenar = producto_busquedas[0][3]
  sin_ordenar = producto_busquedas [0]
  for busquedas in producto_busquedas:
    if busquedas [3] > ordenar:
        ordenar = busquedas[3]
        sin_ordenar = busquedas
  busquedas_ordenadas.append(sin_ordenar)
  producto_busquedas.remove(sin_ordenar)
#fin de codigo para opcion 2 "100 productos con mayor búsquedas"

#inicio de codigo para opcion 3 "los 20 productos con las mejores reseñas"
#primero hice una lista en donde conte el numero de reseñas que tenia cada producto y se guardaba en la variable "producto reseñas" posterior a esto (y por que no encontre otra forma de hacerlo) hice una nueva lista que sumaba los valores de las reseñas por cada productos, la tercer lista era para sacar el promedio de las reseñas de cada producto y finalmente la lista final tiene a los promedios de la reseñas pero acomodados de mayor a menor respecto a este valor; por lo que para la impresion de los 20 productos con mejores reseñas solo mande a llamar a los primeros 10 y para los 20 productos con peores reseñas mande a llamar a los ultimos 20 valores de la misma lista.
contador_resenas = 0 
producto_resenas = []
for producto in lifestore_products:
  for idlist_resenas in lifestore_sales:
    if producto[0]== idlist_resenas[1]:
      contador_resenas += 1 
  cuerpo_resenas = [producto[0],producto[1], contador_resenas,producto[3]]
  producto_resenas.append(cuerpo_resenas)
  contador_resenas = 0

suma_resenas = 0
producto_sumas = []
for producto in lifestore_products:
  for idlist_resenas in lifestore_sales:
    if producto[0]== idlist_resenas[1]:
      suma_resenas = suma_resenas +  idlist_resenas[2]
  cuerpo_sumas = [producto[0],producto[1], suma_resenas,producto[3]]
  producto_sumas.append(cuerpo_sumas)
  suma_resenas = 0

promedio_resena=0
list_promedioresenas = []
for numero_resena in producto_resenas:
  for suma_resena in producto_sumas:
    if numero_resena[0]== suma_resena[0]and numero_resena[2] > 0:
        promedio_resena = suma_resena[2] / numero_resena[2]
  cuerpo_promedio = [numero_resena[0],numero_resena[1],promedio_resena,numero_resena[3]]
  list_promedioresenas.append (cuerpo_promedio)
  promedio_resena=0

resenas_ordenadas = []
while list_promedioresenas:
  resenas_ordenar = list_promedioresenas[0][2]
  resenassin_ordenar = list_promedioresenas [0]
  for resenas in list_promedioresenas:
    if resenas [2] > resenas_ordenar:
        resenas_ordenar = resenas[2]
        resenassin_ordenar = resenas
  resenas_ordenadas.append(resenassin_ordenar)
  list_promedioresenas.remove(resenassin_ordenar)

#fin de codigo para opcion 3 "los 20 productos con las mejores reseñas"
#fin de codigo para opcion 3 "los 20 productos con las mejores reseñas"



no_repetir = 0 
while no_repetir != 1:
  if opcion_menu == "1":
    for elemento in range (0,50):
      print ("Producto: ",ventas_ordenadas[elemento][1],"\n""ID de producto: ",ventas_ordenadas[elemento][0],"\n""No. de ventas:",ventas_ordenadas[elemento][3],"\n""categoria:",ventas_ordenadas[elemento][2],"\n")
      no_repetir = 1
  elif opcion_menu == "2":
    for elemento in range (0,96):
      print ("Producto: ",busquedas_ordenadas[elemento][1],"\n""ID de producto: ",busquedas_ordenadas[elemento][0],"\n""Categoria:",busquedas_ordenadas[elemento][2],"\n","No. de busquedas:",busquedas_ordenadas[elemento][3],"\n")
    no_repetir = 1
  elif opcion_menu == "3":
    for elemento in range (0,20):
      print ("Producto: ",resenas_ordenadas[elemento][1],"\n""ID de producto: ",resenas_ordenadas[elemento][0],"\n""Promedio de reseñas:",resenas_ordenadas[elemento][2],"\n""Categoria:",resenas_ordenadas[elemento][3],"\n")
    no_repetir = 1
  elif opcion_menu == "4":
    for elemento in range (22,42):
      print ("Producto: ",resenas_ordenadas[elemento][1],"\n""ID de producto: ",resenas_ordenadas[elemento][0],"\n""Promedio de reseñas:",resenas_ordenadas[elemento][2],"\n""Categoria:",resenas_ordenadas[elemento][3],"\n")
    no_repetir = 1
  elif opcion_menu == "5":
    print ("sin datos :(")
    no_repetir = 1
  elif opcion_menu == "6":
    print ("sin datos :(")
    no_repetir = 1
  elif opcion_menu == "7":
    print ("sin datos :(")
    no_repetir = 1
  elif opcion_menu == "8":
    print ("sin datos :(")
    no_repetir = 1
  else:
    print ("opcion no encontrada")
    opcion_menu= input ("vuelve a intentarlo: ")
    
  












      






