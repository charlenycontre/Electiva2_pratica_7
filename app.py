# src/app.py
from flask import Flask
import mysql.connector
import os
 
app = Flask(__name__)
 
@app.route('/')
def hello():
    try:
        conn = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "db"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "example"),
            database=os.environ.get("DB_NAME", "testdb")
        )
        return """
<h1 style='color: #4e73df; text-align: center; margin-top: 20%;'>
            ¡Hola Mundo! Conexión a MySQL exitosa
</h1>
<p style='text-align: center; font-size: 1.2em;'>
            Desarrollado por: <strong>Charleny Contreras Ogando</strong> 🚀<br>
            Matrícula: <strong>20231051</strong> ✅
</p>
        """
    except mysql.connector.Error as err:
        return f"""
<h2 style='color: #e74a3b; text-align: center;'>
            Error al conectar a la base de datos ❌
</h2>
<p style='text-align: center;'>{err}</p>
        """
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)