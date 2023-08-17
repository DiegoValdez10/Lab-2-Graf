def timeMatrix (matrix1, matrix2):
    #multiply two matrices
    
    result = []
    for i in range(len(matrix1)):
        result.append([])
        for j in range(len(matrix2[0])):
            result[i].append(0)
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result
        
    
def timeMatrixSingle(matrix1, matrix2):
    filas_matriz = len(matrix1)
    columnas_matriz = len(matrix1[0])
    longitud_vector = len(matrix2)

    if columnas_matriz != longitud_vector:
        raise ValueError("El número de columnas de la matriz debe ser igual a la longitud del vector para calcular el producto punto.")

    resultado = [0] * filas_matriz

    for i in range(filas_matriz):
        for j in range(columnas_matriz):
            resultado[i] += matrix1[i][j] * matrix2[j]

    return resultado

def create_translation_matrix(translate):
    translation_matrix = [
        [1, 0, 0, translate[0]],
        [0, 1, 0, translate[1]],
        [0, 0, 1, translate[2]],
        [0, 0, 0, 1]
    ]
    return translation_matrix



                    