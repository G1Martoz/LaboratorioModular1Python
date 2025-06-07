import os
import pandas as pd
from sqlalchemy import create_engine
from modules.decoradores import manejar_errores, registrar_accion

class ProcesadorArchivosBase:
    def __init__(self):
        self.archivos_exitosos = []
        self.archivos_fallidos = []
        self.motor_db = create_engine('sqlite:///datos.db')
        self.directorio_archivos = 'files/'

    def leer_archivo(self, ruta_archivo):
        raise NotImplementedError("Debe implementarse en la subclase.")

    def validar_datos(self, df):
        if df.empty:
            raise ValueError("El DataFrame está vacío.")

        df.drop_duplicates(inplace=True)
        df.dropna(how='all', inplace=True)

        for columna in df.columns:
            if df[columna].isnull().any():
                raise ValueError(f"La columna '{columna}' contiene valores nulos.")
        return df

    def guardar_en_base(self, df, nombre_tabla):
        df.to_sql(nombre_tabla, self.motor_db, if_exists='replace', index=False)

class ProcesadorDatos(ProcesadorArchivosBase):
    EXTENSIONES_SOPORTADAS = ('.csv', '.json', '.xlsx', '.txt')

    @registrar_accion
    @manejar_errores
    def procesar_archivos(self):
        for nombre_archivo in os.listdir(self.directorio_archivos):
            extension = os.path.splitext(nombre_archivo)[1].lower()
            if extension not in self.EXTENSIONES_SOPORTADAS:
                self.archivos_fallidos.append((nombre_archivo, "Formato no soportado"))
                continue

            ruta_archivo = os.path.join(self.directorio_archivos, nombre_archivo)
            try:
                df = self.leer_archivo(ruta_archivo)
                df = self.validar_datos(df)
                nombre_tabla = os.path.splitext(nombre_archivo)[0]
                self.guardar_en_base(df, nombre_tabla)
                self.archivos_exitosos.append(nombre_archivo)
            except Exception as error:
                self.archivos_fallidos.append((nombre_archivo, str(error)))

    def leer_archivo(self, ruta_archivo):
        extension = os.path.splitext(ruta_archivo)[1].lower()
        if extension == '.csv':
            return pd.read_csv(ruta_archivo)
        elif extension == '.json':
            return pd.read_json(ruta_archivo)
        elif extension == '.xlsx':
            return pd.read_excel(ruta_archivo)
        elif extension == '.txt':
            return pd.read_csv(ruta_archivo, delimiter='|')  # o cambiar el delimitador
        else:
            raise ValueError(f"Extensión de archivo no reconocida: {extension}")

    @registrar_accion
    def mostrar_resumen(self):
        print(f"\n📦 Carga completada.")
        print(f"✅ Archivos cargados correctamente: {self.archivos_exitosos}")
        print(f"❌ Archivos fallidos: {self.archivos_fallidos}")
