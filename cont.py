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