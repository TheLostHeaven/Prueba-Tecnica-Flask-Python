# Api Boking de tours - Flask

# Índice

- [Version Oficial V1.0](#version-oficial-v1.0)
- [Estructura de carpetas](#estructura-de-carpetas)
- [Funcionalidades](#funcionalidades)
- [Tecnologías Usadas](#tecnologias-usadas)
- [Instalación](#instalacion)
- [Configuración](#configuracion)
- [Uso](#uso)
- [Contacto](#contacto)
- [Autores](#autores)

Este proyecto es un ejemplo de una API RESTful desarrollada con Flask que permite realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) en un modelo de tours


Este proyecto esta Generado en Flask 3.0.2 [Flask Micro-FrameWork](https://github.com/pallets/flask)


## Version Oficial V1.0

![Captura de pantalla 2024-03-04 060439](https://github.com/TheLostHeaven/Prueba-Tecnica-Flask-Python/assets/90277397/8079b889-650f-4d7d-8800-f3e76e938f6e)

## Estructura de carpetas

![Captura de pantalla 2024-03-04 055919](https://github.com/TheLostHeaven/Prueba-Tecnica-Flask-Python/assets/90277397/b9921fcd-2d9f-4509-84bb-c6f08c0b9c95)

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
## Configuración

> [!IMPORTANT]
>Es importante la configuracion y en MYSQL_DB asignar tu DB

1 .env Configuración

```env

SECRET_KEY=
MYSQL_HOST=
MYSQL_USER=
MYSQL_PASSWORD=
MYSQL_DB=
JWT_KEY=

ADMIN_USERNAME = 
ADMIN_FULLNAME = 
ADMIN_EMAIL = 
ADMIN_PASSWORD = 
ADMIN_ROLE_ID =

MYSQL_USER_TEST = 
MYSQL_PASSWORD_TEST = 
MYSQL_HOST_TEST = 
MYSQL_DATABASE_TEST = 
```
2 recuerda inicializar y configurar tu base de datos MySQL SQLite o en todo caso la de tu preferencia

3 Inicia la app con 
```bash
    python index.py
```
4 Puedes acceder a ella desde el puerto configurado:

http://127.0.0.1:5000/


## Uso

#### iniciado el puerto puedes navegar en diferentes rutas:
- user 
```bash
http://127.0.0.1:5000/register
http://127.0.0.1:5000/login
```
- tour
```bash
http://127.0.0.1:5000/tours/

```
- Bookings
```bash
http://127.0.0.1:5000/reserve/

```



## Contacto

Si tienes alguna pregunta o sugerencia o quieres la documentacion para desarrollar este proyecto, no dudes en contactarme en [tiquedaniel2002@gmail.com](tiquedaniel2002@gmail.com).


## Autores

- [@Daniel Molina](https://github.com/TheLostHeaven)
