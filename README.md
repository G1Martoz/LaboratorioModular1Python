# 🧪 LaboratorioModular1Python

Este proyecto permite procesar múltiples archivos de datos (`.csv`, `.json`, `.xlsx`, `.txt`) ubicados en un directorio, validarlos y almacenarlos en una base de datos SQLite utilizando `SQLAlchemy` y `Pandas`.

## 📁 Estructura del Proyecto

```
├── files/              # Directorio para archivos de entrada
├── modules/            # Módulos del proyecto
│   ├── decoradores.py  # Decoradores para logging y manejo de errores
│   └── procesador.py   # Procesamiento de archivos
├── main.py            # Aplicación base
├── datos.db           # Base de datos SQLite
└── requirements.txt   # Dependencias del proyecto
```


## ⚙️ Requisitos Técnicos

- Python 3.8+
- Uso de `SQLAlchemy` con `engine` como motor de conexión
- Estructura modular: uso de clases, herencia y decoradores personalizados
- Validación de datos antes de guardar
- Registro en consola de acciones y errores
- Soporte para múltiples formatos de archivo

## 📦 Instalación

1. Cloná el repositorio o descargá el ZIP.
2. Creá un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate 
En Windows: venv\Scripts\activate
```

## Instalá las dependencias:

pip install -r requirements.txt
▶️ Ejecución: Colocá tus archivos .csv, .json, .xlsx o .txt dentro del directorio files/.

## Ejecutá la aplicación:

python main.py
El sistema leerá, validará y guardará los datos en datos.db.

📝 Formato de archivos .txt
Los archivos .txt deben estar delimitados por el carácter | (pipe).
Ejemplo:

nombre|edad|ciudad
Ana|30|Rosario
Luis|25|Córdoba

✅ Resultado: Al finalizar, el sistema mostrará un resumen con los archivos procesados correctamente y los que fallaron, incluyendo el motivo del fallo.

📚 Dependencias:
- pandas
- sqlalchemy
- openpyxl (para archivos Excel)
*Incluidas en requirements.txt.*
