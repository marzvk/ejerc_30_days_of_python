# DIA 23 entorno virtual
##### ## ####### #######


# 1 El primer paso que se hizo fue crear la carpeta :
#   mkdir dia_23_Entorno_virtual


# 2 Luego te posicionas en esta carpeta
# cd dia_23_Entorno_virtual/


# 3 Aqui se crea el entorno en linux, el primer venv es el
# nombre de la funcion , el segundo es el nombre de la
# carpeta que uno genera para el entorno :
# python3 -m venv venv


# 4  activar el entorno
# source venv/bin/activate.fish


# 5 pip freeze, nos da nada, esta vacio


# 6 pip install Flask => pip freeze
# devuelve ahora:

# blinker==1.9.0
# click==8.1.8
# Flask==3.1.0
# itsdangerous==2.2.0
# Jinja2==3.1.6
# MarkupSafe==3.0.2
# Werkzeug==3.1.3


# 7 deactivate  => desactivamos el entorno


# 8 Crear archivo .gitignore => incluir dentro
#  venv
# .venv
