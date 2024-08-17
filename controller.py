from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

# Crea un Blueprint para el endpoint de ciclista
ciclista = Blueprint('ciclista', __name__)

# Create una RUTA
@ciclista.route('/ciclista', methods=['GET'])
def get_users():
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM ciclista')  # Execute a SQL query
    ciclistas = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(ciclistas)  # Return the list as a JSON response

@ciclista.route('/ciclistaByDorsal', methods=['GET'])
def get_ciclista_by_id():
    dorsal = request.args.get('dorsal')
    conn = get_db_connection()  # Connect to the database
    cursor = conn.cursor(pymysql.cursors.DictCursor)  # Return results as dictionaries
    cursor.execute('SELECT * FROM ciclista where dorsal='+dorsal)  # Execute a SQL query
    users = cursor.fetchall()  # Fetch all rows from the result
    conn.close()  # Close the database connection

    return jsonify(users)