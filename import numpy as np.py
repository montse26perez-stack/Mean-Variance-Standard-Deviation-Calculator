import numpy as np

def calculate(list_in):
    # Validar que la lista contenga exactamente 9 números
    if len(list_in) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convertir la lista en una matriz de 3x3 usando NumPy
    matrix = np.array(list_in).reshape(3, 3)
    
    # Calcular y armar el diccionario con el formato exacto exigido
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), 
            matrix.mean(axis=1).tolist(), 
            matrix.mean()
        ],
        'variance': [
            matrix.var(axis=0).tolist(), 
            matrix.var(axis=1).tolist(), 
            matrix.var()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(), 
            matrix.std(axis=1).tolist(), 
            matrix.std()
        ],
        'max': [
            matrix.max(axis=0).tolist(), 
            matrix.max(axis=1).tolist(), 
            matrix.max()
        ],
        'min': [
            matrix.min(axis=0).tolist(), 
            matrix.min(axis=1).tolist(), 
            matrix.min()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(), 
            matrix.sum(axis=1).tolist(), 
            matrix.sum()
        ]
    }

    return calculations