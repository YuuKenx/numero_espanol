from numero_espanol.procesadores.unidades import procesar_unidades
from numero_espanol.procesadores.decenas import procesar_decenas
from numero_espanol.procesadores.centenas import procesar_centenas

def procesar_numero_simple(texto):
    """
    Procesa un número simple (sin mil/millón/billón) y devuelve su valor numérico.
    
    Args:
        texto (str): Texto que contiene un número en español
        
    Returns:
        int: Valor numérico del número
    """
    resultado = 0
    texto = texto.lower().strip()
    
    # Procesamos centenas
    for palabra_centena in ["cien", "ciento", "doscientos", "trescientos", "cuatrocientos", 
                           "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]:
        if palabra_centena in texto.split():
            # Encontramos una centena
            if palabra_centena == "cien" and len(texto.split()) == 1:
                return 100
            
            centenas_result = procesar_centenas(palabra_centena)
            resultado += centenas_result
            
            # Procesamos el resto después de la centena
            resto_texto = texto
            pos_centena = texto.find(palabra_centena)
            if pos_centena > -1:
                # Eliminamos la parte de centenas del texto
                resto_texto = texto[pos_centena + len(palabra_centena):].strip()
                if resto_texto.startswith("y "):
                    resto_texto = resto_texto[2:].strip()
            
            # Procesamos decenas y unidades en el resto
            if resto_texto:
                decenas_result = procesar_decenas(resto_texto)
                if decenas_result > 0:
                    resultado += decenas_result
                else:
                    # Si no hay decenas, buscamos unidades
                    unidades_result = procesar_unidades(resto_texto)
                    resultado += unidades_result
            
            return resultado
    
    # Si no hay centenas, procesamos decenas
    decenas_result = procesar_decenas(texto)
    if decenas_result > 0:
        return decenas_result
    
    # Si no hay decenas, procesamos unidades
    unidades_result = procesar_unidades(texto)
    return unidades_result

def procesar_mil(texto):
    """
    Procesa números que contienen "mil" en un texto en español.
    
    Args:
        texto (str): Texto que contiene números en español con "mil"
        
    Returns:
        int: Valor numérico del número con "mil", o 0 si no se encuentra
    """
    texto = texto.lower()
    
    if "mil" not in texto:
        return 0
    
    # Caso especial para "mil millones"
    if "mil millones" in texto:
        pos_mil_millones = texto.find("mil millones")
        
        # Valor base: 1000000000 (mil millones)
        resultado = 1000000000
        
        # Si hay algo antes de "mil millones", es el multiplicador
        if pos_mil_millones > 0:
            multiplicador_texto = texto[:pos_mil_millones].strip()
            multiplicador = procesar_numero_simple(multiplicador_texto)
            
            # Si encontramos un multiplicador, lo aplicamos
            if multiplicador > 0:
                resultado = multiplicador * 1000000000
        
        # Si hay algo después de "mil millones", lo procesamos como un número adicional
        if pos_mil_millones + len("mil millones") < len(texto):
            resto_texto = texto[pos_mil_millones + len("mil millones"):].strip()
            
            # Procesamos el resto como un número completo
            resto = procesar_numero_simple(resto_texto)
            
            # Sumamos el resto al resultado
            resultado += resto
        
        return resultado
    
    # Caso especial para "mil millones de"
    if "mil millones de" in texto:
        return procesar_mil(texto.replace("mil millones de", "mil millones"))
    
    # Valor base: 1000
    resultado = 1000
    
    # Dividir el texto en partes antes y después de "mil"
    pos_mil = texto.find("mil")
    
    # Si hay algo antes de "mil", es el multiplicador
    if pos_mil > 0:
        multiplicador_texto = texto[:pos_mil].strip()
        multiplicador = procesar_numero_simple(multiplicador_texto)
        
        # Si encontramos un multiplicador, lo aplicamos
        if multiplicador > 0:
            resultado = multiplicador * 1000
    
    # Si hay algo después de "mil", lo procesamos como un número adicional
    if pos_mil + 3 < len(texto) and texto[pos_mil + 3:].strip():
        resto_texto = texto[pos_mil + 3:].strip()
        
        # Verificamos si el resto contiene "millones"
        if "millones" in resto_texto or "millón" in resto_texto:
            resto = procesar_millon(resto_texto)
        else:
            # Procesamos el resto como un número completo
            resto = procesar_numero_simple(resto_texto)
        
        # Sumamos el resto al resultado
        resultado += resto
    
    return resultado

def procesar_millon(texto):
    """
    Procesa números que contienen "millón/millones" en un texto en español.
    
    Args:
        texto (str): Texto que contiene números en español con "millón/millones"
        
    Returns:
        int: Valor numérico del número con "millón/millones", o 0 si no se encuentra
    """
    texto = texto.lower()
    
    # Caso especial para "mil millones"
    if "mil millones" in texto:
        return procesar_mil(texto)
    
    if "millón" in texto:
        pos_millon = texto.find("millón")
        sufijo = "millón"
    elif "millon" in texto:
        pos_millon = texto.find("millon")
        sufijo = "millon"
    elif "millones" in texto:
        pos_millon = texto.find("millones")
        sufijo = "millones"
    # Caso especial para "millardo/millardos" (menos común en español, pero usado en algunos países)
    elif "millardo" in texto:
        pos_millon = texto.find("millardo")
        sufijo = "millardo"
    elif "millardos" in texto:
        pos_millon = texto.find("millardos")
        sufijo = "millardos"
    else:
        return 0
    
    # Valor base: 1000000
    resultado = 1000000
    
    # Si hay algo antes de "millón/millones", es el multiplicador
    if pos_millon > 0:
        multiplicador_texto = texto[:pos_millon].strip()
        
        # Casos especiales
        if multiplicador_texto == "un":
            multiplicador = 1
        else:
            # Verificamos si el multiplicador contiene "mil"
            if "mil" in multiplicador_texto:
                multiplicador = procesar_mil(multiplicador_texto)
            else:
                # Procesamos el multiplicador como un número simple
                multiplicador = procesar_numero_simple(multiplicador_texto)
        
        # Si encontramos un multiplicador, lo aplicamos
        if multiplicador > 0:
            resultado = multiplicador * 1000000
    
    # Si hay algo después de "millón/millones", lo procesamos como un número adicional
    if pos_millon + len(sufijo) < len(texto) and texto[pos_millon + len(sufijo):].strip():
        resto_texto = texto[pos_millon + len(sufijo):].strip()
        
        # Eliminamos "de" si está presente (ej: "millones de")
        if resto_texto.startswith("de "):
            resto_texto = resto_texto[3:].strip()
        
        # Si el resto contiene "mil", lo procesamos como miles
        if "mil" in resto_texto:
            resto = procesar_mil(resto_texto)
        else:
            # Procesamos el resto como un número simple
            resto = procesar_numero_simple(resto_texto)
        
        # Sumamos el resto al resultado
        resultado += resto
    
    return resultado

def procesar_billon(texto):
    """
    Procesa números que contienen "billón/billones" en un texto en español.
    
    Args:
        texto (str): Texto que contiene números en español con "billón/billones"
        
    Returns:
        int: Valor numérico del número con "billón/billones", o 0 si no se encuentra
    """
    texto = texto.lower()
    
    if "billón" in texto:
        pos_billon = texto.find("billón")
        sufijo = "billón"
    elif "billon" in texto:
        pos_billon = texto.find("billon")
        sufijo = "billon"
    elif "billones" in texto:
        pos_billon = texto.find("billones")
        sufijo = "billones"
    else:
        return 0
    
    # Valor base: 1000000000000 (un billón en español)
    resultado = 1000000000000
    
    # Si hay algo antes de "billón/billones", es el multiplicador
    if pos_billon > 0:
        multiplicador_texto = texto[:pos_billon].strip()
        
        # Casos especiales
        if multiplicador_texto == "un":
            multiplicador = 1
        else:
            # Verificamos si el multiplicador contiene "millones"
            if "millones" in multiplicador_texto or "millón" in multiplicador_texto:
                multiplicador = procesar_millon(multiplicador_texto)
            # Verificamos si el multiplicador contiene "mil"
            elif "mil" in multiplicador_texto:
                multiplicador = procesar_mil(multiplicador_texto)
            else:
                # Procesamos el multiplicador como un número simple
                multiplicador = procesar_numero_simple(multiplicador_texto)
        
        # Si encontramos un multiplicador, lo aplicamos
        if multiplicador > 0:
            resultado = multiplicador * 1000000000000
    
    # Si hay algo después de "billón/billones", lo procesamos como un número adicional
    if pos_billon + len(sufijo) < len(texto) and texto[pos_billon + len(sufijo):].strip():
        resto_texto = texto[pos_billon + len(sufijo):].strip()
        
        # Eliminamos "de" si está presente (ej: "billones de")
        if resto_texto.startswith("de "):
            resto_texto = resto_texto[3:].strip()
        
        # Intentamos procesar el resto como millones
        if "millones" in resto_texto or "millón" in resto_texto:
            resto = procesar_millon(resto_texto)
        # Intentamos procesar el resto como miles
        elif "mil" in resto_texto:
            resto = procesar_mil(resto_texto)
        else:
            # Procesamos el resto como un número simple
            resto = procesar_numero_simple(resto_texto)
        
        # Sumamos el resto al resultado
        resultado += resto
    
    return resultado