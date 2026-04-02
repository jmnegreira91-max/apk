[app]

# (str) Título de tu aplicación
title = SPY_OTM_Monitor

# (str) Nombre del paquete (sin espacios)
package.name = spyotmpro

# (str) Dominio del paquete (puedes dejar este)
package.domain = org.trading.ia

# (str) Directorio donde está tu main.py
source.dir = .

# (list) Extensiones de archivos a incluir
source.include_exts = py,png,jpg,kv,atlas

# (str) Versión de tu app
version = 1.0

# (list) LIBRERÍAS CRÍTICAS (No cambies esto, es lo que hace que funcione el SPY)
requirements = python3,kivy,yfinance,pandas,matplotlib,numpy,certifi,urllib3

# (str) Orientación de la pantalla
orientation = portrait

# (bool) Pantalla completa
fullscreen = 0

# (list) PERMISOS (Vital para recibir datos del mercado)
android.permissions = INTERNET

# (int) API de Android (33 es el estándar actual)
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a, armeabi-v7a

# (str) Icono (opcional, puedes añadir uno luego)
# icon.filename = %(source.dir)s/data/icon.png

[buildozer]
# (int) Nivel de log (2 para ver errores detallados)
log_level = 2

# (int) Warn on buildozer unexpected behavior
warn_on_root = 1
