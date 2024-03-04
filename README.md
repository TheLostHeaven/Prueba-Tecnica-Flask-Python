# Api Boking de tours - Flask

Este proyecto es un ejemplo de una API RESTful desarrollada con Flask que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de ours


Este proyecto esta Generado en Flask 3.0.2 [Flask Micro-FrameWork](https://github.com/pallets/flask)


## Version Oficial V1.0



## Estructura de carpetas


## Funcionalidades

- Se implemento `Login, register y CRUD` en su primera version para navegar por las diferente rutas del proyecto.
- Se implemento un `Register` para que los usuarios se puedan registrar en la app y planificar sus tours
- Se implemento un `Login` para que los usuarios se puedan loguear y ver sus tours en cualquier momento
- Se implemento un `CRUD` para que los administradores de la pagina pueda crear varios tours y que los clientes pueda ver cuales estan disponibles para planificar sus viajes
- Se implemento un `micro dashboard` para que los administradores puedan obtener todos los usuarios, crear nuevos administradores y Eliminar usuarios

## Tecnologias Usadas
- PIP
- Python
- JWT (Json Web Token)
- Flask FrameWork
- MySQL
- PyTest
- SQLAlchemy

## Instalacion

1 Clona el repositorio en tu maquina local
```bash
$ git clone https://github.com/TheLostHeaven/Prueba-Tecnica-Flask-Python
```

2 Navega en el directorio del proyecto 
```bash
$ cd Prueba-Tecnica-Flask-Python
```

3 Puedes cambiar el origen del proyecto con los siguientes comando

```bash
$ git remote -v
$ git remote remove origin
$ git remote add origin <nueva_url_del_repositorio>
```

4 Instalar venv (O el entorno de preferencia)

- Windows
```bash
- $ python -m venv venv
```
- Linux/Mac
```bash
- $ python3 -m venv venv
```

5 Inicia el entorno virtual

- Windows
```bash
- $ source venv/Scripts/activate
```
- Linux/Mac
```bash
- $ source venv/bin/activate
```

6 Instalar las dependecias necesarias con el entorno activo
- Recuerda tener el requirements.txt en el root de la carpeta y ejecutas

```bash
$ pip install -r requirements.txt
```


## Uso

1 Inicia la app con 
```bash
$ python index.py
```

2 Puedes acceder a ella desde el puerto configurado:

http://127.0.0.1:5000/

3 Prueba las diferentes Funcionalidades de la pagina 

## Contacto

Si tienes alguna pregunta o sugerencia o quieres la documentacion para desarrollar este proyecto, no dudes en contactarme en [tiquedaniel2002@gmail.com](tiquedaniel2002@gmail.com).


## Autors

- [@Daniel Molina](https://github.com/TheLostHeaven)