from numero_espanol import convertir

def mostrar_ejemplo(texto):
    """Muestra un ejemplo de conversión de texto a número"""
    try:
        numero = convertir(texto)
        print(f'"{texto}" -> {numero}')
    except Exception as e:
        print(f'"{texto}" -> ERROR: {str(e)}')

# Ejemplos de unidades
print("\n=== UNIDADES ===")
for unidad in ["uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]:
    mostrar_ejemplo(unidad)

# Ejemplos de decenas
print("\n=== DECENAS ===")
for decena in ["diez", "once", "doce", "trece", "catorce", "quince", 
               "dieciséis", "diecisiete", "dieciocho", "diecinueve", 
               "veinte", "veintiuno", "veintidós", "treinta", 
               "treinta y uno", "cuarenta y dos", "cincuenta y tres", 
               "sesenta y cuatro", "setenta y cinco", "ochenta y seis", 
               "noventa y nueve"]:
    mostrar_ejemplo(decena)

# Ejemplos de centenas
print("\n=== CENTENAS ===")
for centena in ["cien", "ciento uno", "ciento diez", "ciento veinte", 
                "ciento treinta y dos", "doscientos", "doscientos uno", 
                "trescientos cuarenta y cinco", "cuatrocientos cincuenta y seis", 
                "quinientos sesenta y siete", "seiscientos setenta y ocho", 
                "setecientos ochenta y nueve", "ochocientos noventa", 
                "novecientos noventa y nueve"]:
    mostrar_ejemplo(centena)

# Ejemplos de miles
print("\n=== MILES ===")
for mil in ["mil", "mil uno", "mil cien", "mil doscientos treinta y cuatro", 
            "dos mil", "tres mil cuatrocientos cincuenta y seis", 
            "diez mil", "once mil ciento once", 
            "novecientos noventa y nueve mil novecientos noventa y nueve"]:
    mostrar_ejemplo(mil)

# Ejemplos de millones
print("\n=== MILLONES ===")
for millon in ["un millón", "dos millones", "un millón uno", "un millón cien", 
               "un millón ciento uno", "un millón doscientos treinta y cuatro", 
               "dos millones trescientos cuarenta y cinco mil seiscientos setenta y ocho", 
               "ciento veintitrés millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve"]:
    mostrar_ejemplo(millon)

# Ejemplos de billones
print("\n=== BILLONES ===")
for billon in ["un billón", "dos billones", "un billón uno", 
               "un billón cien millones", "un billón doscientos treinta y cuatro millones", 
               "dos billones trescientos cuarenta y cinco mil millones seiscientos setenta y ocho millones"]:
    mostrar_ejemplo(billon)

# Ejemplos de números muy grandes
print("\n=== NÚMEROS MUY GRANDES ===")
for grande in ["novecientos noventa y nueve mil millones novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve",
               "dos billones trescientos cuarenta y cinco mil millones seiscientos setenta y ocho millones novecientos un mil doscientos treinta y cuatro"]:
    mostrar_ejemplo(grande)