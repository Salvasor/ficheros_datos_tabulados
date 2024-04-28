import pandas as pd
import timeit

# Función para medir el tiempo de ejecución de la lectura y escritura de datos en diferentes formatos
def test_format(file_format):
    if file_format == 'csv':
        # Lectura de datos desde un archivo CSV
        start_time = timeit.default_timer()
        df = pd.read_csv('datos.csv')
        read_time = timeit.default_timer() - start_time
        
        # Escritura de datos a un archivo CSV
        start_time = timeit.default_timer()
        df.to_csv('datos_output.csv', index=False)
        write_time = timeit.default_timer() - start_time
        
    elif file_format == 'excel':
        # Lectura de datos desde un archivo Excel (XLSX)
        start_time = timeit.default_timer()
        df = pd.read_excel('datos.xlsx')
        read_time = timeit.default_timer() - start_time
        
        # Escritura de datos a un archivo Excel (XLSX)
        start_time = timeit.default_timer()
        df.to_excel('datos_output.xlsx', index=False)
        write_time = timeit.default_timer() - start_time
        
    elif file_format == 'json':
        # Lectura de datos desde un archivo JSON
        start_time = timeit.default_timer()
        df = pd.read_json('datos.json')
        read_time = timeit.default_timer() - start_time
        
        # Escritura de datos a un archivo JSON
        start_time = timeit.default_timer()
        df.to_json('datos_output.json', orient='records')
        write_time = timeit.default_timer() - start_time
        
    elif file_format == 'parquet':
        # Lectura de datos desde un archivo Parquet
        start_time = timeit.default_timer()
        df = pd.read_parquet('datos.parquet')
        read_time = timeit.default_timer() - start_time
        
        # Escritura de datos a un archivo Parquet
        start_time = timeit.default_timer()
        df.to_parquet('datos_output.parquet', index=False)
        write_time = timeit.default_timer() - start_time
        
    else:
        print("Formato de archivo no válido.")
        return
    
    return read_time, write_time

# Pruebas para cada formato de archivo
for format in ['csv', 'excel', 'json', 'parquet']:
    read_time, write_time = test_format(format)
    print(f"Tiempo de lectura para {format}: {read_time} segundos")
    print(f"Tiempo de escritura para {format}: {write_time} segundos")
    print("-----------------------------")
