# Copyright (c) 2024 Carlos 'klozz' jesus
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicenciar
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
## SOFTWARE.  

import hashlib
import os

def verificar_hashes(directory, archivo_hashes):
  """
  Compara los hashes almacenados en un archivo con los hashes calculados de los archivos originales.

  Args:
    directorio: El directorio donde se encuentran los archivos.
    archivo_hashes: El nombre del archivo que contiene los hashes.
  """

  with open(archivo_hashes, 'r') as f:
    for linea in f:
      ruta_archivo, hash_esperado = linea.strip().split(':')
      
      with open(ruta_archivo, 'rb') as f:
        hash_calculado = hashlib.sha1(f.read()).hexdigest()
        
      if hash_calculado != hash_esperado:
        print(f"Error: El hash del archivo {ruta_archivo} no coincide.")
      else:
        print(f"El hash del archivo {ruta_archivo} coincide.")

# Ejemplo de uso:
directory = "images"
archivo_hashes = "hashes.txt"

verificar_hashes(directory, archivo_hashes)
