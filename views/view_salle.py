import customtkinter as ctk
from models.salle import Salle
from services.services_salle import ServiceSalle
from tkinter import ttk


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

        self.btn_ajouter = ctk.CTkButton(self.f2, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0)

        self.btn_modifier = ctk.CTkButton(self.f2, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1)

        self.btn_supprimer = ctk.CTkButton(self.f2, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2)

        self.btn_rechercher = ctk.CTkButton(self.f2, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3)

        self.cadreList = ctk.CTkFrame(self, corner_radius=10)
        self.cadreList.pack(pady=10, padx=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("libelle", text="LIBELLÉ")
        self.treeList.heading("type", text="TYPE")
        self.treeList.heading("capacite", text="CAPACITÉ")

        self.treeList.column("code", width=80)
        self.treeList.column("libelle", width=200)
        self.treeList.column("type", width=150)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

        self.lister_salles()

    def ajouter_salle(self):
        salle = Salle(
            self.code.get(),
            self.libelle.get(),
            self.type.get(),
            int(self.capacite.get())
        )
        self.service_salle.ajouter_salle(salle)
        self.lister_salles()

    def modifier_salle(self):
        salle = Salle(
            self.code.get(),
            self.libelle.get(),
            self.type.get(),
            int(self.capacite.get())
        )
        self.service_salle.modifier_salle(salle)
        self.lister_salles()

    def supprimer_salle(self):
        code = self.code.get()
        self.service_salle.supprimer_salle(code)
        self.lister_salles()

    def rechercher_salle(self):
        salle = self.service_salle.rechercher_salle(self.code.get())

        if salle:
            self.libelle.delete(0, "end")
            self.type.delete(0, "end")
            self.capacite.delete(0, "end")

            self.libelle.insert(0, salle.libelle)
            self.type.insert(0, salle.type)
            self.capacite.insert(0, salle.capacite)

    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())

        liste = self.service_salle.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))