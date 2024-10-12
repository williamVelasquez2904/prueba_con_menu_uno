import mysql.connector
import bcrypt
import configparser

def obtener_conexion():

    config = configparser.ConfigParser()
    config.read('config.ini')

    conn = mysql.connector.connect(
        host=config['database']['host'],
        user=config['database']['user'],
        password=config['database']['password'],
        database=config['database']['database']
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

