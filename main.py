import random
import string

def generar_contraseña(longitud, may, min, num, esp):
    # Conjuntos de caracteres que pueden ser incluidos
    caracteres = ''
    if may:
        caracteres += string.ascii_uppercase  # Letras mayúsculas
    if min:
        caracteres += string.ascii_lowercase  # Letras minúsculas
    if num:
        caracteres += string.digits           # Números
    if esp:
        caracteres += string.punctuation      # Caracteres especiales

    # Asegurarse de que al menos un tipo de caracteres esté seleccionado
    if not caracteres:
        raise ValueError("Debe seleccionar al menos un tipo de caracteres.")

    # Generar la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Ejemplo de uso
longitud = 50  # Define la longitud de la contraseña
mayusculas=True
minusculas=True
numeros=True
especiales=False


print(generar_contraseña(longitud, mayusculas, minusculas, numeros, especiales))
