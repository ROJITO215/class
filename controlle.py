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