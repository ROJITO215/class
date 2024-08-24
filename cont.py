from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

puerto = Blueprint('puerto', __name__)

@puerto.route('/puerto', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor) 
    cursor.execute('SELECT * FROM puerto')
    puerto = cursor.fetchall()
    conn.close()

    return jsonify(puerto)

@puerto.route('/puertobycategoria', methods=['GET'])
def get_puerto_by_id():
    categoria = request.args.get('categoria')
    nompuerto = request.args.get('nompuerto')
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM puerto where categoria ="' + categoria + '" or nompuerto ="'+ nompuerto + '"' )  # Execute a SQL query
    users = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(users)

@puerto.route('/puerto', methods=['POST'])
def create_user():
    data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen 'nombre' y 'edad'
        sql = "INSERT INTO puerto (altura, categoria, dorsal, netapa, nompuerto, pendiente) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (data['altura'], data['categoria'], data['dorsal'], data['netapa'], data['nompuerto'], data['pendiente']))
        conn.commit()  # Confirmar la transacción
        return jsonify({'message': 'puerto creado exitosamente'}), 201
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo crear el puerto'), 500
    finally:
        if conn:
            conn.close()


@puerto.route('/puerto/<string:categoria>', methods=['PUT'])
def update_user(categoria):
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen 'nombre' y 'edad'
        sql = "UPDATE puerto SET altura = %s, dorsal = %s, netapa = %s, pendiente = %s WHERE categoria = %s"
        cursor.execute(sql, (data['altura'], data['dorsal'], data['netapa'], data['pendiente'], categoria))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'puerto no encontrado'}), 404
        return jsonify({'message': 'puerto actualizado exitosamente'})
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo actualizar el puerto'), 500
    finally:
        if conn:
            conn.close()