from numero_espanol import convertir

# Casos que presentaban problemas
casos_problematicos = [
    # Caso 1: Problema con "dos mil" aplicado a millones
    ("dos mil trescientos cuarenta y cinco millones seiscientos setenta y ocho mil novecientos noventa y uno", 2345678991),
    
    # Caso 2: Problema con el procesamiento de billones y miles de millones
    ("un billón doscientos treinta y cuatro mil quinientos sesenta y siete millones ochocientos noventa y uno mil doscientos treinta y cuatro", 1234567891234),
    
    # Caso 3: Problema con el número de dígitos en números grandes
    ("novecientos noventa y nueve mil novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve", 999999999999),
    
    # Casos adicionales para verificar la corrección
    ("quinientos cuarenta y seis billones setecientos ochenta y tres millones doscientos uno mil doscientos treinta y cuatro", 546000783201234),
    ("tres millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve", 3456789),
    ("cuatrocientos treinta y dos millones trescientos veintidós mil trescientos cuarenta y cinco", 432322345),
    ("cincuenta y seis millones setecientos ochenta y nueve mil trescientos veinte", 56789320),
    ("un billón quinientos millones trescientos veintitrés mil cuatrocientos cincuenta y seis", 1000500323456),
    ("doscientos treinta y cuatro millones quinientos sesenta y siete mil ochocientos noventa y uno", 234567891),
    ("setecientos ochenta y nueve millones trescientos treinta y tres mil cuatrocientos cincuenta y seis", 789333456),
]

# Probamos cada caso
print("\n=== CASOS PROBLEMÁTICOS ===")
for texto, esperado in casos_problematicos:
    try:
        resultado = convertir(texto)
        print(f'"{texto}" -> {resultado} (esperado: {esperado}) {"✓" if resultado == esperado else "✗"}')
    except Exception as e:
        print(f'"{texto}" -> ERROR: {str(e)}')