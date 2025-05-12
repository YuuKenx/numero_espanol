from numero_espanol import convertir

# Casos básicos (ya probados)
casos_basicos = [
    ("trescientos cuarenta y cinco", 345),
    ("mil doscientos treinta y cuatro", 1234),
    ("un millón doscientos treinta y cuatro", 1000234),
    ("quinientos sesenta y siete", 567),
    ("mil uno", 1001),
    ("un millón ciento uno", 1000101),
    ("dos millones", 2000000)
]

# Casos complejos
casos_complejos = [
    # Números grandes con millones
    ("novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve", 999999999),
    ("ciento veintitrés millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve", 123456789),
    
    # Números con combinaciones complejas
    ("dos millones trescientos cuarenta y cinco mil seiscientos setenta y ocho", 2345678),
    ("veintitrés millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve", 23456789),
    
    # Números con billones
    ("un billón", 1000000000000),
    ("dos billones trescientos cuarenta y cinco mil millones seiscientos setenta y ocho millones novecientos un mil doscientos treinta y cuatro", 2345678901234),
    
    # Casos especiales y variaciones
    ("mil millones", 1000000000),
    ("un millardo", 1000000000),  # Variante menos común en español
    ("dos mil millones trescientos cuarenta y cinco", 2000000345),
    
    # Números muy grandes
    ("novecientos ochenta y siete mil seiscientos cincuenta y cuatro millones trescientos veintiún mil", 987654321000),
]

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

# Probamos los casos básicos
print("\n=== CASOS BÁSICOS ===")
for texto, esperado in casos_basicos:
    resultado = convertir(texto)
    print(f'"{texto}" -> {resultado} (esperado: {esperado}) {"✓" if resultado == esperado else "✗"}')

# Probamos los casos complejos
print("\n=== CASOS COMPLEJOS ===")
for texto, esperado in casos_complejos:
    try:
        resultado = convertir(texto)
        print(f'"{texto}" -> {resultado} (esperado: {esperado}) {"✓" if resultado == esperado else "✗"}')
    except Exception as e:
        print(f'"{texto}" -> ERROR: {str(e)}')

# Probamos los nuevos ejemplos
print("\n=== NUEVOS EJEMPLOS ===")
for texto, esperado in nuevos_ejemplos:
    try:
        resultado = convertir(texto)
        print(f'"{texto}" -> {resultado} (esperado: {esperado}) {"✓" if resultado == esperado else "✗"}')
    except Exception as e:
        print(f'"{texto}" -> ERROR: {str(e)}')