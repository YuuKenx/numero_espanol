from numero_espanol import convertir

# Ejemplos muy grandes con billones y millones
ejemplos_muy_grandes = [
    ("un billón quinientos veintitrés mil cuatrocientos setenta y ocho millones novecientos noventa y uno mil doscientos tres", 1523478991203),
    ("doscientos mil millones trescientos cuatro mil quinientos sesenta y siete millones ochocientos noventa y uno mil doscientos treinta y cuatro", 200304567891234),
    ("tres billones doscientos cuarenta y cinco mil millones quinientos noventa y ocho mil setecientos noventa y uno", 3245000598791),
    ("cinco mil trescientos veinte millones cuatrocientos diez mil setecientos ochenta y nueve", 5320410789),
    ("un billón doscientos tres mil cuatrocientos cincuenta millones setecientos sesenta y ocho mil novecientos noventa", 1203450768990),
    ("novecientos noventa y nueve billones novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve", 999000999999999),
    ("cuatro millones quinientos veintitrés mil setecientos ochenta y nueve billones trescientos treinta y tres millones", 4523789000333000000),
    ("seiscientos mil millones setecientos ochenta y nueve millones cuatrocientos cincuenta y seis mil setecientos ocho", 600789456708),
    ("un billón novecientos noventa y nueve millones novecientos noventa y nueve mil novecientos noventa y nueve", 1000999999999),
    ("dos billones quinientos noventa y ocho mil millones setecientos ochenta y nueve mil novecientos doce", 2598000789912),
]

# Ejemplos de cientos de miles
ejemplos_cientos_miles = [
    ("ciento dos mil trescientos cuarenta y cinco", 102345),
    ("quinientos cincuenta y seis mil setecientos ochenta y nueve", 556789),
    ("trescientos noventa y ocho mil seiscientos veintitrés", 398623),
    ("mil novecientos ochenta y cuatro mil quinientos sesenta y siete", 1984567),
    ("setecientos treinta y dos mil ochocientos noventa y uno", 732891),
]

# Ejemplos de millones
ejemplos_millones = [
    ("tres millones cuatrocientos cincuenta y seis mil setecientos ochenta y nueve", 3456789),
    ("doce millones trescientos veintitrés mil quinientos sesenta y siete", 12323567),
    ("seis millones ochocientos noventa y siete mil trescientos veintidós", 6897322),
    ("veintiún millones cuatrocientos cincuenta y seis mil setecientos noventa", 21456790),
    ("nueve millones novecientos noventa y nueve mil novecientos noventa", 9999990),
]

# Ejemplos de miles
ejemplos_miles = [
    ("mil doscientos tres", 1203),
    ("cinco mil cuatrocientos treinta y uno", 5431),
    ("tres mil novecientos cincuenta y seis", 3956),
    ("cuatro mil quinientos ochenta y siete", 4587),
    ("mil setecientos treinta y dos", 1732),
]

# Función para probar los ejemplos
def probar_ejemplos(categoria, ejemplos):
    print(f"\n=== {categoria} ===")
    for texto, esperado in ejemplos:
        try:
            resultado = convertir(texto)
            print(f'"{texto}" -> {resultado} (esperado: {esperado}) {"✓" if resultado == esperado else "✗"}')
        except Exception as e:
            print(f'"{texto}" -> ERROR: {str(e)}')

# Probamos todos los ejemplos
probar_ejemplos("EJEMPLOS MUY GRANDES", ejemplos_muy_grandes)
probar_ejemplos("CIENTOS DE MILES", ejemplos_cientos_miles)
probar_ejemplos("MILLONES", ejemplos_millones)
probar_ejemplos("MILES", ejemplos_miles)