import mysql.connector
import bcrypt
import configparser
import socket

def obtener_conexion():
    nombre_maquina=socket.gethostname()
    
    config = configparser.ConfigParser()
    config.read('config.ini')
    if nombre_maquina=='WilliamJose':
    
        conn = mysql.connector.connect(
            host=config['database_home']['host'],
            user=config['database_home']['user'],
            password=config['database_home']['password'],
            database=config['database_home']['database']
        )

    #conn = mysql.connector.connect(
    #    host="192.168.0.102",
    #    user="root",
    #    password="",
    #    database="wejadminmot_test"
    #)
    return conn

def encriptar_clave(clave):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(clave.encode('utf-8'), salt)
    return hashed

def verificar_clave(clave, hashed):
    return bcrypt.checkpw(clave.encode('utf-8'), hashed)

