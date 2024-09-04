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

def generar_hashes_sha1(directory, output_file):
  """
  Genera hashes SHA1 de todos los archivos en un directorio y los escribe en un archivo de texto.

  Args:
    directory: El directorio donde se encuentran los archivos.
    output_file: El nombre del archivo de salida donde se escribirán los hashes.

  eng
  Generates SHA1 hashes of all files in a directory and writes them to a text file.

  Args:
    directory: The directory where the files are located.
    output_file: The name of the output file where the hashes will be written.
  """

  with open(output_file, 'w') as salida:
    for root, _, files in os.walk(directory):
      for file in files:
        ruta_completa = os.path.join(root, file)
        with open(ruta_completa, 'rb') as f:
          hash_sha1 = hashlib.sha1()
          hash_sha1.update(f.read())
          hash_hex = hash_sha1.hexdigest()
          salida.write(f"{ruta_completa}:{hash_hex}\n")

# Ejemplo de uso:
directory = "images"  # Reemplaza con la ruta a tu directory
output_file = "hashes.txt"

generar_hashes_sha1(directory, output_file)
