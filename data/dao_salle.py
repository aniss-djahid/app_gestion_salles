import json
import mysql.connector
from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open("data/config.json", "r") as file:
            config = json.load(file)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"],
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "insert into salle(code, libelle, type, capacite) values(%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "update salle set libelle = %s, capacite = %s where code = %s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "delete from salle where code = %s"
        cursor.execute(query, (code,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = "select * from salle where code = %s"
        cursor.execute(query, (code,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None
