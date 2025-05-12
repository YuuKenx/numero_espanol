def procesar_unidades(texto):
    """
    Procesa las unidades (1-9) en un texto en español y devuelve su valor numérico.
    
    Args:
        texto (str): Texto que contiene números en español
        
    Returns:
        int: Valor numérico de la unidad encontrada, o 0 si no se encuentra
    """
    unidades = {
        "uno": 1, "un": 1, "una": 1, 
        "dos": 2, 
        "tres": 3, 
        "cuatro": 4, 
        "cinco": 5,
        "seis": 6, 
        "siete": 7, 
        "ocho": 8, 
        "nueve": 9
    }
    
    # Buscar palabras completas para evitar coincidencias parciales
    palabras = texto.lower().split()
    for palabra in palabras:
        if palabra in unidades:
            return unidades[palabra]
    
    return 0  # Si no se encuentra ninguna unidad