import csv
import pandas as pd
import os

def ingresar_ventas(ventas):
    while True:
        try:
            curso = input('Ingrese el nombre del curso: ').upper
            cantidad = int(input("Ingrese la cantidad de cursos: "))
            fecha = input('Ingrese la fecha de la venta (AAAA-MM-DD): ')
            precio = float(input('Ingrese el precio del curso: '))
            cliente = input('Ingrese el nombre del cliente: ').upper
        except ValueError:
            print('Entradas no valida, por favor intentelo nuevamente!')
            continue
        
        venta = {
            'Curso': curso,
            'Cantidad': cantidad,
            'Precio': precio,
            'Fecha':fecha,
            'Cliente': cliente
        }
        ventas.append(venta)
        
        continuar = input('Desea ingresar otra venta s/n: ').lower()
        if continuar == 's':
            print("\n ------------  Ingresando otra Venta  ---------")
        elif continuar == 'n':
            break
        else:
            print('Opción no valida. Saliendo de ventas.')
            break
        
def guardar_ventas(ventas):
    if not ventas:
        print('No hay nada que guardar')
    else:
        try:
            if os.path.exists('ventas.csv'):
                with open('ventas.csv','a',newline='') as archivo:
                    guardar = csv.DictWriter(archivo,fieldnames=['Curso','Cantidad','Precio','Fecha','Cliente'])
                    guardar.writerows(ventas)
            else:
                with open('ventas.csv','w',newline='') as archivo:
                    guardar = csv.DictWriter(archivo,fieldnames=['Curso','Cantidad','Precio','Fecha','Cliente'])
                    guardar.writeheader()
                    guardar.writerows(ventas)
            print('Datos gardados exitosamente!')
        except Exception as e:
            print(f'Error al guarda el archivo {e}')
            
            
def analizar_ventas():
    try:
        df = pd.read_csv('ventas.csv')
        print('\n ---------- RESUMEN DE VENTAS -------------')
        df['Ingreso'] = df['Cantidad' * df['Precio']]
        if not df.empty:
            curso_mas_vendido = df.groupby('Curso')['Cantidad'].sum().idxmax()
            print(f'Curso más vendido {curso_mas_vendido}')
            cliente_top = df.groupby('Cliente')['Ingreso'].sum().idxmax
            print(f'El cliente top es: {cliente_top}')
        else:
            print('No existen datos para analizar')
    
        print('\n Ventas por fecha')
        print(df.groupby('Fecha')['Ingreso'].sum().round(decimals=2))
    except FileNotFoundError:
            print('No se encontró el archivo csv.  Guarde datos antes de analizar')