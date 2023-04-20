import openpyxl
from datetime import datetime


def actualizar_archivo_excel(archivo_excel, archivo_csv):
    # Configuración
    COLUMNAS = {
        'fecha_vencimiento': 'Fecha de vencimiento',
        'estado': 'Estado',
        'tipo_incidencia': 'Tipo de Incidencia',
    }
    ESTADOS = {
        'PRODUCCION': 'CERRADO',
        'CERRADO': 'CERRADO',
    }
    TIPOS_INCIDENCIA_VALIDOS = [
        'Funcionalidad Planificada',
        'Tarea Planificada',
        'Tarea No Planificada'
    ]

    # Función para formatear la fecha
    def formatear_fecha(fecha):
        if isinstance(fecha, datetime):
            return fecha.strftime('%d%m%Y')
        return fecha

    # Función para formatear el estado
    def formatear_estado(estado):
        return ESTADOS.get(estado, estado)

    # Función para formatear el tipo de incidencia
    def formatear_tipo_incidencia(tipo_incidencia):
        if tipo_incidencia not in TIPOS_INCIDENCIA_VALIDOS:
            raise ValueError(
                f'Tipo de incidencia no válida: {tipo_incidencia}')
        return tipo_incidencia

    try:
        # Leer el archivo Excel
        workbook = openpyxl.load_workbook("C:\Work\jira.xlsx")

        # Seleccionar la hoja de trabajo
        worksheet = workbook.active

        # Iterar sobre las filas y hacer los cambios necesarios
        for row in worksheet.iter_rows(min_row=2):
            # Cambiar el formato de la fecha
            fecha_actualizada = row[COLUMNAS['fecha_vencimiento']].value
            row[COLUMNAS['fecha_vencimiento']
                ].value = formatear_fecha(fecha_actualizada)

            # Cambiar el estado de la tarea
            estado = row[COLUMNAS['estado']].value
            row[COLUMNAS['estado']].value = formatear_estado(estado)

            # Cambiar el tipo de incidencia si es válido
            tipo_incidencia = row[COLUMNAS['tipo_incidencia']].value
            if tipo_incidencia:
                row[COLUMNAS['tipo_incidencia']
                    ].value = formatear_tipo_incidencia(tipo_incidencia)

        # Guardar el archivo Excel actualizado
        workbook.save(archivo_csv)
        workbook.close()

        print(f"Archivo {archivo_csv} actualizado con éxito!")

    except FileNotFoundError:
        print(f"Error: El archivo {archivo_excel} no existe.")
    except Exception as e:
        print(f"Error al actualizar el archivo: {e}")
