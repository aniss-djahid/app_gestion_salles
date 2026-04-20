import customtkinter as ctk
from services.services_salle import ServiceSalle


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.service_salle = ServiceSalle()

        self.title("Gestion Salles")
        self.geometry("1000x600")


        self.f1 = ctk.CTkFrame(self)
        self.f1.pack(pady=10)

        ctk.CTkLabel(self.f1, text="Code").grid(row=0, column=0)
        self.code = ctk.CTkEntry(self.f1)
        self.code.grid(row=0, column=1)

        ctk.CTkLabel(self.f1, text="Libellé").grid(row=1, column=0)
        self.libelle = ctk.CTkEntry(self.f1)
        self.libelle.grid(row=1, column=1)

        ctk.CTkLabel(self.f1, text="Type").grid(row=2, column=0)
        self.type = ctk.CTkEntry(self.f1)
        self.type.grid(row=2, column=1)

        ctk.CTkLabel(self.f1, text="Capacité").grid(row=3, column=0)
        self.capacite = ctk.CTkEntry(self.f1)
        self.capacite.grid(row=3, column=1)


        self.f2 = ctk.CTkFrame(self)
        self.f2.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.f2, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0)

        self.btn_modifier = ctk.CTkButton(self.f2, text="Modifier")
        self.btn_modifier.grid(row=0, column=1)

        self.btn_supprimer = ctk.CTkButton(self.f2, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2)

        self.btn_rechercher = ctk.CTkButton(self.f2, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3)

        self.btn_ajouter.configure(command=self.ajouter_salle)

    def ajouter_salle(self):
        salle = Salle(
            self.code.get(),
            self.libelle.get(),
            self.type.get(),
            int(self.capacite.get())
        )
        self.service_salle.ajouter_salle(salle)

        self.btn_modifier.configure(command=self.modifier_salle)

    def modifier_salle(self):
        salle = Salle(
            self.code.get(),
            self.libelle.get(),
            self.type.get(),
            int(self.capacite.get())
        )
        self.service_salle.modifier_salle(salle)