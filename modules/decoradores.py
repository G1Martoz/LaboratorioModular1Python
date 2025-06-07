from functools import wraps

def registrar_accion(funcion):
    @wraps(funcion)
    def envoltorio(*args, **kwargs):
        print(f"▶ Ejecutando: {funcion.__name__}")
        resultado = funcion(*args, **kwargs)
        print(f"✔ Completado: {funcion.__name__}")
        return resultado
    return envoltorio

def manejar_errores(funcion):
    @wraps(funcion)
    def envoltorio(*args, **kwargs):
        try:
            return funcion(*args, **kwargs)
        except Exception as error:
            print(f"⚠ Error en {funcion.__name__}: {error}")
    return envoltorio
