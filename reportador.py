import os
import time
from datetime import datetime

# Paleta de colores para consola
VERDE = "\033[1;32m"
AMARILLO = "\033[1;33m"
CYAN = "\033[1;36m"
RESET = "\033[0m"

def generar_reporte_html():
    os.system("clear")
    print(f"{CYAN}======================================================={RESET}")
    print(f"       📊 GENERADOR DE REPORTES HTML - PROYECTO LIBERTAD")
    print(f"{CYAN}======================================================={RESET}")
    print(f"{AMARILLO}[!] Leyendo registros de auditoría local...{RESET}")
    
    ruta_txt = os.path.expanduser("~/mis_script/reporte_intrusos.txt")
    contenido_tabla = ""
    
    # Leemos el archivo de intrusos generado por tu comando 'caza'
    if os.path.exists(ruta_txt):
        with open(ruta_txt, "r") as f:
            lineas = f.readlines()
            for linea in lineas:
                if "IP:" in linea:
                    # Parseamos la línea 'IP: 192.168.43.1 | Router Principal'
                    partes = linea.strip().split("|")
                    ip = partes[0].replace("IP:", "").strip()
                    dispositivo = partes[1].strip() if len(partes) > 1 else "Desconocido"
                    
                    # Insertamos filas en formato HTML con diseño táctico
                    contenido_tabla += f"""
                    <tr>
                        <td style="padding: 12px; border-bottom: 1px solid #333; color: #00ffcc; font-family: monospace;">{ip}</td>
                        <td style="padding: 12px; border-bottom: 1px solid #333; color: #fff;">{dispositivo}</td>
                        <td style="padding: 12px; border-bottom: 1px solid #333; color: #1, 32m;"><span style="background: rgba(0,255,204,0.1); color: #00ffcc; padding: 4px 8px; border-radius: 4px; font-size: 12px;">ACTIVO</span></td>
                    </tr>
                    """
    
    # Si el archivo está vacío o no existe, ponemos una fila por defecto
    if not contenido_tabla:
        contenido_tabla = """
        <tr>
            <td colspan="3" style="padding: 20px; text-align: center; color: #ff3366;">No se encontraron registros de auditorías recientes.</td>
        </tr>
        """
        
    fecha_actual = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    
    # Estructura del documento HTML con diseño oscuro Premium
    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte de Auditoría - Proyecto Libertad</title>
    <style>
        body {{ background-color: #0b0f19; color: #f3f4f6; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; padding: 20px; }}
        .card {{ max-width: 700px; margin: 30px auto; background: #111827; border: 1px solid #1f2937; border-radius: 12px; padding: 24px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }}
        .header {{ text-align: center; border-bottom: 2px solid #1f2937; padding-bottom: 15px; margin-bottom: 20px; }}
        .title {{ color: #00e5ff; margin: 0; font-size: 24px; letter-spacing: 1px; }}
        .meta {{ color: #9ca3af; font-size: 14px; margin-top: 5px; }}
        table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        th {{ text-align: left; padding: 12px; background: #1f2937; color: #9ca3af; font-size: 14px; text-transform: uppercase; }}
        .footer {{ text-align: center; margin-top: 25px; color: #4b5563; font-size: 12px; }}
    </style>
</head>
<body>
    <div class="card">
        <div class="header">
            <h2 class="title">🛡️ REPORTE DE SEGURIDAD OPERATIVA</h2>
            <div class="meta">Proyecto Libertad 2026 | Sincronización Satelital</div>
        </div>
        <p><strong>Dispositivo Auditor:</strong> Infinix X6870 (Android 15)</p>
        <p><strong>Fecha de Generación:</strong> <span style="color: #am; font-family: monospace;">{fecha_actual}</span></p>
        
        <table>
            <thead>
                <tr>
                    <th>Dirección IP</th>
                    <th>Identificación del Host</th>
                    <th>Estado de Conexión</th>
                </tr>
            </thead>
            <tbody>
                {contenido_tabla}
            </tbody>
        </table>
        
        <div class="footer">
            Generado automáticamente por el módulo reportador.py desde Termux.
        </div>
    </div>
</body>
</html>"""

    # Guardamos el archivo HTML final listo para producción
    ruta_salida = os.path.expanduser("~/mis_script/reporte.html")
    with open(ruta_salida, "w") as f:
        f.write(html_template)
        
    print(f"\n{VERDE}✅ ¡REPORTE HTML GENERADO CON ÉXITO!{RESET}")
    print(f"📄 Guardado en: {AMARILLO}'~/mis_script/reporte.html'{RESET}")
    print(f"{CYAN}======================================================={RESET}")

if __name__ == "__main__":
    generar_reporte_html()
