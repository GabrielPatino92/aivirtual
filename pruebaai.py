import subprocess
import os

def revisar_codigo_con_pylint(ruta_archivo):
    try:
        # Ejecuta pylint en el archivo especificado
        resultado = subprocess.run(
            ['pylint', ruta_archivo],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        # Muestra los resultados del análisis
        print("Resultados de Pylint:")
        print(resultado.stdout)
    except FileNotFoundError:
        print("Pylint no está instalado. Por favor, instálalo con 'pip install pylint'.")

# Ruta del archivo a revisar
ruta_archivo = 'pruebaai.py'
revisar_codigo_con_pylint(ruta_archivo)
# Solución para agregar el directorio de Scripts a PATH temporalmente

# Agregar el directorio de Scripts a PATH
scripts_path = r'C:\Users\lpati\AppData\Roaming\Python\Python312\Scripts'
os.environ["PATH"] += os.pathsep + scripts_path

# Verificar si pylint está en PATH
if not any(os.access(os.path.join(path, 'pylint.exe'), os.X_OK) for path in os.environ["PATH"].split(os.pathsep)):
    print(f"Advertencia: pylint no se encuentra en PATH. Asegúrate de que '{scripts_path}' esté correctamente configurado.")
else:
    # Verificar si pylint está en PATH y ejecutar el análisis si es posible
    if any(os.access(os.path.join(path, 'pylint.exe'), os.X_OK) for path in os.environ["PATH"].split(os.pathsep)):
        revisar_codigo_con_pylint(ruta_archivo)
    else:
        print(f"Advertencia: pylint no se encuentra en PATH. Asegúrate de que '{scripts_path}' esté correctamente configurado.")
