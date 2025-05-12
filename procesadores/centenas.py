def procesar_centenas(texto):
    """
    Procesa las centenas (100-999) en un texto en español y devuelve su valor numérico.
    
    Args:
        texto (str): Texto que contiene números en español
        
    Returns:
        int: Valor numérico de la centena encontrada, o 0 si no se encuentra
    """
    centenas = {
        "cien": 100, "ciento": 100,
        "doscientos": 200, "doscientas": 200,
        "trescientos": 300, "trescientas": 300,
        "cuatrocientos": 400, "cuatrocientas": 400,
        "quinientos": 500, "quinientas": 500,
        "seiscientos": 600, "seiscientas": 600,
        "setecientos": 700, "setecientas": 700,
        "ochocientos": 800, "ochocientas": 800,
        "novecientos": 900, "novecientas": 900
    }
    
    texto = texto.lower()
    palabras = texto.split()
    
    for palabra, valor in centenas.items():
        if palabra in palabras:
            # Caso especial para "cien" vs "ciento"
            if palabra == "cien" and "ciento" not in texto:
                return 100
            elif palabra == "ciento" or palabra == "cien":
                # Si es "ciento" seguido de algo, es 100 + ese algo
                return 100
            else:
                return valor
    
    return 0  # Si no se encuentra ninguna centena