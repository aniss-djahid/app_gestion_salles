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


