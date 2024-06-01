def limpiar_y_guardar_datos_pgn(archivo_pgn):
    archivo_salida = archivo_pgn.replace('.pgn', '_limpio.pgn')

    with open(archivo_pgn, 'r') as archivo_entrada, open(archivo_salida, 'w') as archivo_salida:
        for linea in archivo_entrada:
            if linea.strip() and linea.strip()[0].isdigit():
                archivo_salida.write(linea)

    print(f"Los movimientos limpios se han guardado en {archivo_salida}")