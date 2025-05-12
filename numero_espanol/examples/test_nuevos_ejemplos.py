from numero_espanol import convertir

# Nuevos ejemplos solicitados
nuevos_ejemplos = [
    ("dos mil trescientos cuarenta y cinco millones seiscientos setenta y ocho mil novecientos noventa y uno", 2345678991),
    ("quinientos cuarenta y seis billones setecientos ochenta y tres millones doscientos uno mil doscientos treinta y cuatro", 546000783201234),
    ("un billón doscientos treinta y cuatro mil quinientos sesenta y siete millones ochocientos noventa y uno mil doscientos treinta y cuatro", 1234567891234),
    ("tres millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve", 3456789),
    ("novecientos noventa y nueve mil novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve", 999999999999),
    ("cuatrocientos treinta y dos millones trescientos veintidós mil trescientos cuarenta y cinco", 432322345),
    ("cincuenta y seis millones setecientos ochenta y nueve mil trescientos veinte", 56789320),
    ("un billón quinientos millones trescientos veintitrés mil cuatrocientos cincuenta y seis", 1000500323456),
    ("doscientos treinta y cuatro millones quinientos sesenta y siete mil ochocientos noventa y uno", 234567891),
    ("setecientos ochenta y nueve millones trescientos treinta y tres mil cuatrocientos cincuenta y seis", 789333456),
]

# Probamos cada ejemplo
print("\n=== NUEVOS EJEMPLOS ===")
for texto, esperado in nuevos_ejemplos:
    try:
        resultado = convertir(texto)
        print(f'"{texto}" -> {resultado} (esperado: {esperado}) {"✓" if resultado == esperado else "✗"}')
    except Exception as e:
        print(f'"{texto}" -> ERROR: {str(e)}')