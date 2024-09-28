import streamlit as st
#1. Función de saludo simple: Escribe una función llamada saludar() que reciba un nombre como parámetro y que imprima un saludo personalizado, por ejemplo, “Hola, Juan”. Luego, invoca la función varias veces con diferentes nombres.
def saludar(nombre):
    return f"Hola, {nombre}"
#2. Suma de dos números: Crea una función sumar() que reciba dos números como parámetros y devuelva su suma. Llama a la función y muestra el resultado en pantalla.
def sumar(num1, num2):
    return num1 + num2
#3. Área de un triángulo: Escribe una función llamada calcular_area_triangulo() que reciba la base y la altura de un triángulo, y calcule y devuelva su área. El área de un triángulo se calcula como "área"=1/2×"base"×"altura" .
def calcular_area_triangulo(base, altura):
    return 0.5 * base * altura
#4. Calculadora de descuento: Crea una función calcular_precio_final() que tome como parámetros el precio original de un producto, un porcentaje de descuento (opcional, por defecto 10%) y un impuesto (opcional, por defecto 16%). La función debe calcular el precio final después de aplicar el descuento y sumar el impuesto.
def calcular_precio_final(precio, descuento=10, impuesto=16):
    precio_descuento = precio - (precio * descuento / 100)
    precio_final = precio_descuento + (precio_descuento * impuesto / 100)
    return precio_final
#5. Suma de una lista de números: Escribe una función sumar_lista() que reciba una lista de números y devuelva la suma de todos ellos. Usa un bucle para recorrer la lista y sumar sus elementos.
def sumar_lista(lista):
    return sum(lista)
#6. Funciones con valores predeterminados: Crea una función llamada producto() que tome como parámetros el nombre de un producto, la cantidad (por defecto 1) y el precio por unidad (por defecto 10). La función debe devolver el precio total a pagar. Luego, prueba invocar la función con diferentes combinaciones de argumentos.
def producto(nombre_producto, cantidad=1, precio_por_unidad=10):
    total = cantidad * precio_por_unidad
    return f"Total a pagar por {nombre_producto}: {total}"
#7. Números pares e impares: Escribe una función llamada numeros_pares_e_impares() que reciba una lista de números y devuelva dos listas: una con los números pares y otra con los impares. Usa un bucle para recorrer la lista y separar los números.
def numeros_pares_e_impares(lista):
    pares = [num for num in lista if num % 2 == 0]
    impares = [num for num in lista if num % 2 != 0]
    return pares, impares
#8. Multiplicación con *args: Crea una función llamada multiplicar_todos() que reciba cualquier cantidad de números utilizando *args y devuelva el resultado de multiplicarlos todos. Si no se pasan argumentos, debe devolver 1.
def multiplicar_todos(*args):
    if not args:
        return 1
    resultado = 1
    for num in args:
        resultado *= num
    return resultado
#9. Información de una persona con **kwargs: Escribe una función informacion_personal() que reciba cualquier cantidad de información personal usando **kwargs (por ejemplo: nombre, edad, dirección, etc.) e imprima cada dato en formato clave:valor.
def informacion_personal(**kwargs):
    return kwargs
#10. Calculadora flexible: Crea una función llamada calculadora_flexible() que tome tres parámetros: dos números y una operación (por defecto “suma”). La función debe realizar la operación especificada (suma, resta, multiplicación o división) sobre los números. Usa un diccionario o múltiples condicionales (if) o match para seleccionar la operación adecuada.
def calculadora_flexible(num1, num2, operacion="suma"):
    if operacion == "suma":
        return num1 + num2
    elif operacion == "resta":
        return num1 - num2
    elif operacion == "multiplicacion":
        return num1 * num2
    elif operacion == "division" and num2 != 0:
        return num1 / num2
    else:
        return "Operación no válida o división por cero"
    
st.title("Tarea Funciones en Python")

st.header("1. Saludo personalizado")
nombre = st.text_input("Introducir nombre")
if nombre:
    st.write(saludar(nombre))

st.header("2. Suma de dos números")
num1 = st.number_input("Introduce el primer número", key="num1", value=0)
num2 = st.number_input("Introduce el segundo número", key="num2", value=0)
if st.button("Calcular suma"):
    st.write(f"La suma es {sumar(num1, num2)}")

st.header("3. Área de un triángulo")
base = st.number_input("Introduce la base del triángulo", key="base", value=0.0)
altura = st.number_input("Introduce la altura del triángulo", key="altura", value=0.0)
if st.button("Calcular área"):
    st.write(f"El área es: {calcular_area_triangulo(base, altura)}")

st.header("4. Calculadora de descuento")
precio = st.number_input("Precio del producto", key="precio", value=0.0)
descuento = st.number_input("Porcentaje de descuento", key="descuento", value=10)
impuesto = st.number_input("Porcentaje de impuesto", key="impuesto", value=16)
if st.button("Calcular precio final"):
    st.write(f"El precio final es {calcular_precio_final(precio, descuento, impuesto)}")

st.header("5. Suma de una lista")
lista = st.text_input("Introduce una lista de números separados por comas", key="lista_numeros")
if lista:
    lista_numeros = [int(x) for x in lista.split(",")]
    st.write(f"La suma es {sumar_lista(lista_numeros)}")

st.header("6. Producto con valores predeterminados")
nombre_producto = st.text_input("Nombre del producto", key="nombre_producto")
cantidad = st.number_input("Cantidad", key="cantidad_producto", value=1)
precio_por_unidad = st.number_input("Precio por unidad", key="precio_por_unidad", value=10)
if st.button("Calcular precio total"):
    st.write(producto(nombre_producto, cantidad, precio_por_unidad))

st.header("7. Números pares e impares")
lista_pares_impares = st.text_input("Introduce una lista de números separados por comas", key="pares_impares")
if lista_pares_impares:
    lista_numeros = [int(x) for x in lista_pares_impares.split(",")]
    pares, impares = numeros_pares_e_impares(lista_numeros)
    st.write(f"Números pares: {pares}")
    st.write(f"Números impares: {impares}")

st.header("8. Multiplicación con *args")
numeros_multiplicacion = st.text_input("Introduce varios números separados por comas", key="multiplicacion")
if numeros_multiplicacion:
    lista_numeros = [int(x) for x in numeros_multiplicacion.split(",")]
    st.write(f"El resultado es {multiplicar_todos(*lista_numeros)}")

st.header("9. Información personal con **kwargs")
nombre_info = st.text_input("Nombre", key="nombre_info")
edad_info = st.number_input("Edad", key="edad_info", value=0)
direccion_info = st.text_input("Dirección", key="direccion_info")
if st.button("Mostrar información"):
    info = informacion_personal(nombre=nombre_info, edad=edad_info, direccion=direccion_info)
    for clave, valor in info.items():
        st.write(f"{clave}: {valor}")

st.header("10. Calculadora flexible")
num1_calc = st.number_input("Primer número", key="num1_calc", value=0.0)
num2_calc = st.number_input("Segundo número", key="num2_calc", value=0.0)
operacion_calc = st.selectbox("Selecciona la operación", ["suma", "resta", "multiplicacion", "division"], key="operacion_calc")
if st.button("Calcular operación"):
    resultado = calculadora_flexible(num1_calc, num2_calc, operacion_calc)
    st.write(f"El resultado es: {resultado}")
