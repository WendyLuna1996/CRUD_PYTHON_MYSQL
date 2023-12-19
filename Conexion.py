# pip install mysql-connector-python
import mysql.connector

class CConexion:

    def ConexionBaseDeDatos():
      try:
         conexion = mysql.connector.connect(user='root',password='0000',
                                               host='127.0.0.1',
                                               database='clientesdb',
                                               port='3308')
         print("conexion correcta")

         return conexion

      except mysql.connector.Error as error:
        print("Error al conectarte a la base de Datos {}".format(error))

        return conexion 

    ConexionBaseDeDatos()