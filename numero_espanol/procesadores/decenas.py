from numero_espanol.procesadores.unidades import procesar_unidades

def procesar_decenas(texto):
    """
    Procesa las decenas (10-99) en un texto en español y devuelve su valor numérico.
    
    Args:
        texto (str): Texto que contiene números en español
        
    Returns:
        int: Valor numérico de la decena encontrada, o 0 si no se encuentra
    """
    # Números específicos del 10 al 29
    decenas_especificas = {
        "diez": 10, 
        "once": 11, 
        "doce": 12, 
        "trece": 13, 
        "catorce": 14,
        "quince": 15, 
        "dieciséis": 16, "dieciseis": 16, 
        "diecisiete": 17, 
        "dieciocho": 18, 
        "diecinueve": 19,
        "veinte": 20, 
        "veintiuno": 21, "veintiún": 21, "veintiun": 21,
        "veintidós": 22, "veintidos": 22,
        "veintitrés": 23, "veintitres": 23,
        "veinticuatro": 24,
        "veinticinco": 25,
        "veintiséis": 26, "veintiseis": 26,
        "veintisiete": 27,
        "veintiocho": 28,
        "veintinueve": 29
    }
    
    # Múltiplos de 10 (30, 40, etc.)
    multiplos_de_diez = {
        "veinte": 20,
        "treinta": 30, 
        "cuarenta": 40, 
        "cincuenta": 50,
        "sesenta": 60, 
        "setenta": 70, 
        "ochenta": 80, 
        "noventa": 90
    }
    
    texto = texto.lower()
    palabras = texto.split()
    
    # Primero verificamos si es un número específico (10-29)
    for palabra in palabras:
        if palabra in decenas_especificas:
            return decenas_especificas[palabra]
    
    # Luego verificamos si es un múltiplo de 10 con unidades (ej: "treinta y dos")
    for decena, valor_decena in multiplos_de_diez.items():
        if decena in palabras:
            # Si contiene "y", hay unidades
            if " y " in texto:
                # Encontrar la posición de la decena en el texto
                pos_decena = texto.find(decena)
                # Encontrar la posición de "y" después de la decena
                pos_y = texto.find(" y ", pos_decena)
                if pos_y > -1:
                    # Extraer la parte después de "y"
                    parte_unidades = texto[pos_y + 3:].strip()
                    # Procesar la unidad
                    unidad = procesar_unidades(parte_unidades)
                    return valor_decena + unidad
            else:
                # Solo la decena sin unidades
                return valor_decena
    
    return 0  # Si no se encuentra ninguna decena