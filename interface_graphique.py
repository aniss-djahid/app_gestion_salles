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