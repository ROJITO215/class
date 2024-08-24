from flask import Blueprint, jsonify, request
import pymysql
from conexion import get_db_connection

etapa = Blueprint('etapa', __name__)

@etapa.route('/etapa', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor) 
    cursor.execute('SELECT * FROM etapa')
    etapa = cursor.fetchall()
    conn.close()

    return jsonify(etapa)