class usuarios:
    def __init__(self, mysql):
        self.mysql = mysql
        self.conexion = self.mysql.connect()
        self.cursor = self.conexion.cursor()
    
    def consultar(self):
        sql = f"SELECT * FROM cliente"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado
    
    def agregar(self, usuario):
        sql = f"INSERT INTO cliente (nombres,apellidos,tipo_documento,documento,genero,celular,correo,contra,fecha_nac,creado)\
            VALUES ('{usuario[0]}','{usuario[1]}','{usuario[2]}','{usuario[3]}','{usuario[4]}','{usuario[5]}','{usuario[6]}','{usuario[7]}','{usuario[8]}','{usuario[9]}')"
        self.cursor.execute(sql)
        self.conexion.commit()
        
    def buscar(self,documento):
        sql = f"SELECT * FROM cliente WHERE documento={documento}"
        self.cursor.execute(sql)
        resultado = self.cursor.fetchall()
        self.conexion.commit()
        return resultado