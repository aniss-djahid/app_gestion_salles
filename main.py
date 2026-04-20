from data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

conn = dao.get_connection()
print("connexion reussie")
conn.close()

s1 = Salle("xx19", "salle2026", "machines", 19)
dao.insert_salle(s1)
print("salle ajoutee")


s1.libelle = "Salle Informatique"
dao.update_salle(s1)
print("salle modifiee")


result = dao.get_salle("S01")
if result:
    result.afficher_infos()
else:
    print("pas de salle")

salles = dao.get_salles()
for s in salles:
    s.afficher_infos()

dao.delete_salle("S01")
print("salle supprimee")