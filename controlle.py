from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

maillot = Blueprint('maillot', __name__)

@maillot.route('/maillot', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor) 
    cursor.execute('SELECT * FROM maillot')
    maillot = cursor.fetchall()
    conn.close()

    return jsonify(maillot)

@maillot.route('/puertobycategoria', methods=['GET'])
def get_maillot_by_id():
    maillot = request.args.get('categoria')
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM  where categoria='+categoria)  # Execute a SQL query
    users = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(users)


@maillot.route('/maillot', methods=['POST'])
def create_user():
    data = request.get_json()  # Obtener los datos JSON del cuerpo de la solicitud
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen 'nombre' y 'edad'
        sql = "INSERT INTO maillot (codigo, color, premio, tipo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (data['codigo'], data['color'], data['premio'], data['tipo']))
        conn.commit()  # Confirmar la transacción
        return jsonify({'message': 'maillot creado exitosamente'}), 201
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo crear el maillot'), 500
    finally:
        if conn:
            conn.close()

@maillot.route('/maillot/<string:color>', methods=['PUT'])
def update_user(color):
    data = request.get_json()
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Suponiendo que los datos incluyen 'nombre' y 'edad'
        sql = "UPDATE maillot SET tipo = %s, color = %s, premio = %s WHERE color = %s"
        cursor.execute(sql, (data['tipo'], data['color'], data['premio'], color))
        conn.commit()
        if cursor.rowcount == 0:
            return jsonify({'message': 'maillot no encontrado'}), 404
        return jsonify({'message': 'maillot actualizado exitosamente'})
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo actualizar el maillot'), 500
    finally:
        if conn:
            conn.close()



@maillot.route('/maillot/<string:color>', methods=['DELETE'])
def delete_user(color):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM maillot WHERE color = %s"
        cursor.execute(sql, (color,))
        conn.commit()
        
        if cursor.rowcount == 0:
            return jsonify({'message': 'maillot no encontrado'}), 404
        return jsonify({'message': 'maillot eliminado exitosamente'})
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return jsonify('No se pudo eliminar el maillot'), 500
    finally:
        if conn:
            conn.close()