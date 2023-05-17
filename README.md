# Repo_GrandesVoldeInfo

## Procesamiento inicial de los datos 

El Script 'consolidar_data.py' tiene como objetivo consolidar los archivos mensuales de operaciones del SEN en una sola base de datos. Se sigue el siguiente procedimiento:

1. Comprensión del negocio y los datos:
   - El objetivo de este código es procesar archivos de Excel que contienen datos relacionados con cierres de operaciones del SEN.
   - Se asume que los archivos de Excel están ubicados en una carpeta '/SEN' dentro del directorio en donde se encuentra este script.
   - El código busca filtrar y transformar los datos de los archivos Excel para obtener un DataFrame consolidado que cumpla con ciertos criterios de filtrado.

2. Preparación de los datos:
   - Se inicializan las variables necesarias, como el nombre de la carpeta que contiene los archivos de Excel.
   - Se obtiene la ruta completa de la carpeta utilizando la información de la máquina en donde se ejecuta el script.
   - Se lista los archivos en la carpeta y se filtran solo aquellos con extensiones de archivo específicas (".xlsx" o ".xls").

3. Procesamiento de datos:
   - Se itera sobre cada archivo Excel seleccionado.
   - Se carga el archivo en un DataFrame utilizando la función `pd.read_excel()` de la biblioteca pandas.
   - Se realizan varias operaciones de filtrado y transformación en los datos del DataFrame:
     - Se extraen los primeros 4 caracteres del nemotécnico y se almacenan en una nueva columna llamada "aux".
     - Se filtran las filas que no cumplan con ciertos criterios, como eliminar aquellas donde el valor en la columna "aux" sea igual a "TFVT" y mantener solo las filas donde el valor en la columna "SESION/RUEDA" sea "CONH", pues es en esta rueda de negociación, la de contado, en la que está nuestro interés.
   - El DataFrame filtrado se concatena con un DataFrame llamado "operaciones" que almacena los datos consolidados de todos los archivos Excel.

4. Salida:
   - Los datos procesados se guardan en un archivo CSV llamado "SEN.csv" utilizando el método `to_csv()` de pandas.

En resumen, el código procesa los datos financieros contenidos en los archivos Excel, filtrando y transformando los datos en un DataFrame consolidado que cumple con los criterios de interés. Finalmente, el resultado se guarda en un archivo CSV para su uso posterior sobre modelado y machine learning.