import hashlib
from flask import Flask, redirect, render_template, request
from flaskext.mysql import MySQL
from datetime import datetime
from Usuario import usuarios

empresa_app = Flask(__name__)
mysql = MySQL()

empresa_app.config['MYSQL_DATABASE_HOST'] = 'localhost'
empresa_app.config['MYSQL_DATABASE_PORT'] = 3306
empresa_app.config['MYSQL_DATABASE_USER'] = 'root'
empresa_app.config['MYSQL_DATABASE_PASSWORD'] = ''
empresa_app.config['MYSQL_DATABASE_DB'] = 'prueba'
mysql.init_app(empresa_app)
misUsuarios = usuarios(mysql)

@empresa_app.route("/")
def index():
    return render_template('index.html',msg="")

@empresa_app.route("/registrar")
def registrar():
    return render_template("registrar.html")


@empresa_app.route("/login", methods=['POST'])
def login():
    correo = request.form['correo']
    contraseña = request.form['contra']
    cifrada = hashlib.sha512(contraseña.encode("utf-8")).hexdigest()
    sql = f"SELECT * FROM cliente WHERE correo='{correo}' AND contra='{cifrada}'"
    con = mysql.connect()
    cur = con.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    con.commit()
    if len(resultado)==0:
        return render_template("index.html",msg="Credenciales incorrectas o usuario inactivo")
    else:
        return render_template("correcto.html",nom=resultado[0][0])
    

@empresa_app.route("/guardar", methods=['POST'])
def guardar():
    nombres = request.form['nombres']
    apellidos = request.form['apellidos']
    tipo_documento = request.form['tipo_documento']
    documento = request.form['documento']
    genero = request.form['genero']
    celular = request.form['celular']
    correo = request.form['correo']
    contra = request.form['contra']
    fecha_nac = request.form['fecha_nac']
    ahora = datetime.now()
    creado = ahora.strftime("%Y%m%d%H%M%S")
    misUsuarios.agregar([nombres,apellidos,tipo_documento,documento,genero,celular,correo,contra,fecha_nac,creado])
    return redirect('/')

if __name__=='__main__':
    empresa_app.run(host='0.0.0.0',debug=True,port=2645)
