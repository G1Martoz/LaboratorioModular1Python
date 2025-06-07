from modules.procesador import ProcesadorDatos
from modules.decoradores import registrar_accion

class AplicacionPrincipal:
    @staticmethod
    @registrar_accion
    def ejecutar():
        procesador = ProcesadorDatos()
        procesador.procesar_archivos()
        procesador.mostrar_resumen()

if __name__ == '__main__':
    AplicacionPrincipal.ejecutar()
