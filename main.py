from services.services_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

print("Liste des salles :")
salles = service.recuperer_salles()
for s in salles:
    s.afficher_infos()

s1 = Salle("yy19", "salle2027", "livres", 30)
ok, msg = service.ajouter_salle(s1)
print(msg)

s1.libelle = "Salle Informatique"
ok, msg = service.modifier_salle(s1)
print(msg)

result = service.rechercher_salle("yy20")
if result:
    result.afficher_infos()
else:
    print("Salle introuvable")

ok = service.supprimer_salle("yy19")
print("Salle supprimée")