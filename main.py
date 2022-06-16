import xml.etree.ElementTree as et
from functools import partial
from logging import root
from tkinter import *
from tkinter import messagebox

#lecture de fichier xml
my_tree = et.parse(r"C:\Users\yassi\publication.xml")
tronc = my_tree.getroot()
# window = Tk()



# window.title("ProjetXml")
# window.geometry("1920x1080")
# window.minsize(480, 360)
# window.config(background='#D8DDD6')
a=""
eTitre=""
eNbr=""
eAnnee =""
eConference=""
eNom=""
eNumTel=""
eAdresse=""

def main():
    window = Tk()
    window.title("ProjetXml")
    window.geometry("1920x1080")

    frame = Frame(window)
    frame.pack()
    bottomframe = Frame(window)
    bottomframe.pack(side=TOP)

    # Creation frames
    frame_accueil = Frame(window, bg="#D8DDD6")

    frame_accueil2 = Frame(window, bg="#D8DDD6")

    # Frame 1
    label_title = Label(frame_accueil, text="Bienvenue sur notre plateforme !", font=("Arial", 40), bg="#D8DDD6",
                        fg="black")
    label_title.pack()

    # Frame2 : boutons
    bouton_ajouter = Button(frame_accueil2, text="Ajouter une publication", font=("Arial", 25), bg="black",
                            fg="#D8DDD6",
                            command=ajout)
    bouton_ajouter.grid(row=1, column=0)

    bouton_supprimer = Button(frame_accueil2, text="Supprimer une publication", font=("Arial", 25), bg="black",
                              fg="#D8DDD6",
                              command=supp)
    bouton_supprimer.grid(row=1, column=1)

    bouton_recherche = Button(frame_accueil2, text="Rechercher une publication", font=("Arial", 25), bg="black",
                              fg="#D8DDD6",
                              command=recherche)
    bouton_recherche.grid(row=1, column=2)

    # Affichage frames
    frame_accueil.pack(expand=YES)
    frame_accueil2.pack(expand=YES)

def Ajouter():
    global  a
    a="heyy"
    root = Tk()
    root.title("Ajouter une publication")
    root.geometry("1920x1080")

    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=TOP)

    # Creation frames
    #     frame_page1_1 = Frame(root, bg="#D8DDD6")
    #     frame_page1_2 = Frame(root, bg="#D8DDD6")

    # Frame 1
    label_title = Label(root, text="informations de la publication", font=("Arial", 25), fg="black")
    label_title.pack(side=TOP, pady=10)

    label_subtitle = Label(root, text="Veuillez remplir les champs suivants "
                           , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
    label_subtitle.pack(side=TOP, pady=10)

    l2 = Label(root, text="Titre").pack()
    e2 = Entry(root).pack()


    l3 = Label(root, text="Nbres des Pages").pack()
    e3 = Entry(root).pack()


    l4 = Label(root, text="Année").pack()
    e4 = Entry(root).pack()


    l5 = Label(root, text="Conference").pack()
    e5 = Entry(root).pack()


    l6 = Label(root, text="Informations Auteur").pack()

    l7 = Label(root, text="Nom").pack()
    e7= Entry(root).pack()


    l9 = Label(root, text="Num Tel").pack()
    e8 = Entry(root).pack()


    l10 = Label(root, text="Adresse").pack()
    e9 = Entry(root).pack()


    global eTitre
    eTitre = e2.get()
    global eNbr
    eNbr = e3.get()
    global eAnnee
    eAnnee = e4.get()
    global eConference
    eConference = e5.get()
    global eNom
    eNom = e7.get()
    global eNumTel
    eNom = e8.get()
    global eAdresse
    eNom = e9.get()

    # Button(root, text="Envoyer",
    #        command=partial(ajouterPublication, eTitre, eNbr, eAnnee, eConference, eNom, eNumTel, eAdresse)).pack(pady=50)
    b = Button(root ,text="Submit", command = ajouterPublication).pack(pady=20)

    # Frame 2
    bouton_suivant1 = Button(root, text="back", font=("Arial", 10), bg="black", fg="#D8DDD6",
                             command=back)
    bouton_suivant1.pack()

    # Affichage frames


#     frame_page1_1.pack(expand=YES)
#     frame_page1_2.pack(expand=YES)
#     window.mainloop()





def ajout():
    Ajouter()
    window.destroy()


#     window.quit()
def supp():
    Supprimer()

def recherche():
    Rechercher()

def ajouterPublication():
    global eTitre
    eTitre = e2.get()
    global eNbr
    eNbr = e3.get()
    global eAnnee
    eAnnee = e4.get()
    global eConference
    eConference = e5.get()
    global eNom
    eNom = e7.get()
    global eNumTel
    eNom = e8.get()
    global eAdresse
    eNom = e9.get()
    pub = et.SubElement(tronc[0], 'publication')
    et.SubElement(pub, 'titre').text = eTitre
    et.SubElement(pub, 'nbpages').text = eNbr
    et.SubElement(pub, 'nbpages').text = eAnnee
    et.SubElement(pub, 'conference').text = eConference
    auteur = et.SubElement(pub, 'auteur')
    et.SubElement(auteur, 'nom').text = eNom
    et.SubElement(auteur, 'numtel').text = eNumTel
    et.SubElement(auteur, 'adresse').text = eAdresse

    # my_tree.write(et.tostring(tronc, 'UTF-8'), "publication.xml")

    my_tree.write(r"C:\Users\yassi\publication.xml")

    messagebox.showinfo("Statut de l'envoie", "publication enregistrée!")

def back():
    main()
    root.quit()

def Rechercher():
    root = Tk()
    root.title("Rechercher une publication")
    root.geometry("1920x1080")

    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=TOP)

    # Creation frames
    #     frame_page1_1 = Frame(root, bg="#D8DDD6")
    #     frame_page1_2 = Frame(root, bg="#D8DDD6")

    label_subtitle = Label(root, text="Veuillez remplir le champ suivant"
                           , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
    label_subtitle.pack(side=TOP, pady=10)

    l1 = Label(root, text="Element à recherhcer").pack()
    e1 = Entry(root).pack()
    bTitre = Button(root, text="Rechercher par titre", command=Commande).pack(pady=20)

    bConference = Button(root, text="Rechercher par confrence", command=Commande).pack(pady=20)

    bAuteur = Button(root, text="Rechercher par auteur", command=Commande).pack(pady=20)

    # Frame 2
    bouton_suivant1 = Button(root, text="Retour", font=("Arial", 20), bg="blue", fg="#D8DDD6",
                             command=main)
    bouton_suivant1.pack()

def Commande():
    messagebox.showinfo("Recherche", "Recherche en cours...Veuillez patientez")

def rechercheParTitre():
    root = Tk()
    root.title("Rechercher une publication")
    root.geometry("1920x1080")

    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=TOP)
    l2 = Label(root, text="Titre").pack()
    e2 = Entry(root).pack()
    eTitre = r = e2

    l3 = Label(root, text="Nbres des Pages").pack()
    eNbr = Entry(root).pack()
    eNbr = eNbr

    l4 = Label(root, text="Année").pack()
    eAnnee = Entry(root).pack()
    eAnnee = eAnnee

    l5 = Label(root, text="Conference").pack()
    eConference = Entry(root).pack()
    eConference = eConference

    l6 = Label(root, text="Informations Auteur").pack()

    l7 = Label(root, text="Nom").pack()
    eNom = Entry(root).pack()
    eNom = eNom

    l9 = Label(root, text="Num Tel").pack()
    eNumTel = Entry(root).pack()
    eNumTel = eNumTel

    l10 = Label(root, text="Adresse").pack()
    eAdresse = Entry(root).pack()
    eAdresse = eAdresse

def Supprimer():
    root = Tk()
    root.title("Supprimer une publication")
    root.geometry("1920x1080")

    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=TOP)


    label_subtitle = Label(root, text="Veuillez remplir le titre de la publication à supprimer"
                           , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
    label_subtitle.pack(side=TOP, pady=10)

    l1 = Label(root, text="le titre de la publication à supprimer").pack()
    e1 = Entry(root).pack()
    titr=e1.get()

    bSupp = Button(root, text="Supprimer", command=partial(delete_pub,titr), bg="red", fg="black").pack(pady=20)

    bAnnuler = Button(root, text="Annuler", command=Supprimer, bg="green", fg="black").pack(pady=20)

    # Frame 2
    bouton_back = Button(root, text="Retour", font=("Arial", 15), bg="blue", fg="#D8DDD6",
                         command=main)
    bouton_back.pack()

def pub_existe(titre):
    for pub in tronc.findall("publication"):
        tag_titre=pub.find("titre").text
        if tag_titre==titre:
            return pub
    return False

def delete_pub(titre):
    pub=pub_existe(titre)
    if not pub:
        Commande("echec de supprission","pas de publication a supprimer")
    else:
        tronc.remove(pub)
        my_tree.write('publication.xml')

def searchauteurnom(nom1):
    for pub in tronc.findall('publication'):
        for auteur in pub.findall("./auteur"):
            nom = auteur.find("nom")
            if (nom1 == nom.text):
                Comm("Affichage","auteur trouvé!")
                printpub(pub)
                return (True)

    print("pas d'auteur")

def Afficher():
    root = Tk()
    root.title("Ajouter une publication")
    root.geometry("1920x1080")

    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack(side=TOP)

    # Creation frames
    #     frame_page1_1 = Frame(root, bg="#D8DDD6")
    #     frame_page1_2 = Frame(root, bg="#D8DDD6")

    # Frame 1
    label_title = Label(root, text="informations sur la publication recherchée", font=("Arial", 25), fg="black")
    label_title.pack(side=TOP, pady=10)




    # Frame 2
    bouton_suivant1 = Button(root, text="back", font=("Arial", 10), bg="black", fg="#D8DDD6",
                             command=back)
    bouton_suivant1.pack()

    li = tkinter.Listbox()
def CommandeSup():
    messagebox.showinfo("Supprimer une publication", "Un element sera supprimer! ")

def CommandeAff():
    messagebox.showinfo("Afficher une publication", "Une publication a ete trouvée ")

def Comm(nom,affiche):
    messagebox.showinfo(nom, affiche)

main()
# Ajouter()
# Rechercher()
# Supprimer()
window.mainloop()



# import tkinter
# import xml.etree.ElementTree as et
# from functools import partial
# from logging import root
# from tkinter import *
# from tkinter import messagebox
#
#
#
#
#
# #lecture de fichier xml
# my_tree = et.parse(r"C:\Users\yassi\publication.xml")
# tronc = my_tree.getroot()
# window = Tk()
# import tkinter as tk
# from tkinter import ttk
#
#
# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.main()
#         # self.title('Tkinter StringVar')
#         # self.geometry("300x80")
#
#         # self.name_var = tk.StringVar()
#         #
#         # self.columnconfigure(0, weight=1)
#         # self.columnconfigure(1, weight=1)
#         # self.columnconfigure(2, weight=1)
#         #
#         # self.create_widgets()
#
#     def create_widgets(self):
#
#         padding = {'padx': 5, 'pady': 5}
#         # label
#         ttk.Label(self, text='Name:').grid(column=0, row=0, **padding)
#
#         # Entry
#         name_entry = ttk.Entry(self, textvariable=self.name_var)
#         name_entry.grid(column=1, row=0, **padding)
#         name_entry.focus()
#
#         # Button
#         submit_button = ttk.Button(self, text='Submit', command=self.submit)
#         submit_button.grid(column=2, row=0, **padding)
#
#         # Output label
#         self.output_label = ttk.Label(self)
#         self.output_label.grid(column=0, row=1, columnspan=3, **padding)
#
#     def submit(self):
#         self.output_label.config(text=self.name_var.get())
#
#     def main(self):
#         window = Tk()
#         self.title("ProjetXml")
#         self.geometry("1920x1080")
#
#         frame = Frame(self)
#         frame.pack()
#         bottomframe = Frame(self)
#         bottomframe.pack(side=TOP)
#
#         # Creation frames
#         frame_accueil = Frame(self, bg="#D8DDD6")
#
#         frame_accueil2 = Frame(self, bg="#D8DDD6")
#
#         # Frame 1
#         label_title = Label(self, text="Bienvenue sur notre plateforme !", font=("Arial", 40), bg="#D8DDD6",
#                             fg="black")
#         label_title.pack()
#
#         # Frame2 : boutons
#         bouton_ajouter = Button(frame_accueil2, text="Aaaajouter une publication", font=("Arial", 25), bg="black",
#                                 fg="#D8DDD6",
#                                 command=self.ajout)
#         bouton_ajouter.grid(row=1, column=0)
#
#         bouton_supprimer = Button(frame_accueil2, text="Supprimer une publication", font=("Arial", 25), bg="black",
#                                   fg="#D8DDD6",
#                                   command=self.supp)
#         bouton_supprimer.grid(row=1, column=1)
#
#         bouton_recherche = Button(frame_accueil2, text="Rechercher une publication", font=("Arial", 25), bg="black",
#                                   fg="#D8DDD6",
#                                   command=self.recherche)
#         bouton_recherche.grid(row=1, column=2)
#
#         # Affichage frames
#         frame_accueil.pack(expand=YES)
#         frame_accueil2.pack(expand=YES)
#
#     def Ajouter(self):
#
#         root = Tk()
#         root.title("Ajouter une publication")
#         root.geometry("1920x1080")
#
#         frame = Frame(root)
#         frame.pack()
#         bottomframe = Frame(root)
#         bottomframe.pack(side=TOP)
#
#         # Creation frames
#         #     frame_page1_1 = Frame(root, bg="#D8DDD6")
#         #     frame_page1_2 = Frame(root, bg="#D8DDD6")
#
#         # Frame 1
#         label_title = Label(root, text="informations de la publication", font=("Arial", 25), fg="black")
#         label_title.pack(side=TOP, pady=10)
#         label_subtitle = Label(root, text="Veuillez remplir les champs suivants "
#                                , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
#         label_subtitle.pack(side=TOP, pady=10)
#         l2 = Label(root, text="Titre").pack()
#         global titre
#         titre = StringVar()
#         e2 = Entry(root, textvariable=titre).pack()
#
#         l3 = Label(root, text="Nbres des Pages").pack()
#         global nbrr
#         nbrr = StringVar()
#         e3 = Entry(root, textvariable=nbrr).pack()
#
#         l4 = Label(root, text="Année").pack()
#         global ann
#         ann = StringVar()
#         e4 = Entry(root, textvariable=ann).pack()
#
#         l5 = Label(root, text="Conference").pack()
#         global conf
#         conf = StringVar()
#         e5 = Entry(root, textvariable=conf).pack()
#
        l6 = Label(root, text="Informations Auteur").pack()

        l7 = Label(root, text="Nom").pack()
        global nomm
        nomm = StringVar()
        e7 = Entry(root, textvariable=nomm).pack()

        l9 = Label(root, text="Num Tel").pack()
        global numt
        numt = StringVar()
        e8 = Entry(root, textvariable=numt).pack()

        l10 = Label(root, text="Adresse").pack()
        global adrr
        adrr = StringVar()
        e9 = Entry(root, textvariable=adrr).pack()

        # Button(root, text="Envoyer",
        #        command=partial(ajouterPublication, eTitre, eNbr, eAnnee, eConference, eNom, eNumTel, eAdresse)).pack(pady=50)
        b = Button(root, text="Submit", command=self.ajouterPublication).pack(pady=20)

        # Frame 2
        bouton_suivant1 = Button(root, text="back", font=("Arial", 10), bg="black", fg="#D8DDD6",
                                 command=self.back)
        bouton_suivant1.pack()

        # global eTitre
        # global eNbr
        # global eAnnee
        # global eConference
        # # eConference = e5.get()
        # global eNom
        # # eNom = e7.get()
        # global eNumTel
        # # eNumTel = e8.get()
        # global eAdresse
        # # eAdresse= e9.get()

    def ajout(self):
        self.Ajouter()

    def supp(self):
        self.Supprimer()
        self.CommandeSup()

    def recherche(self):
        self.Rechercher()

    def ajouterPublication(self):
        eTitre = titre.get()
        eNbr = str(nbrr)
        eAnnee = str(ann.get())
        eConference = str(conf.get())
        eNom = str(nomm.get())
        eNumTel = str(numt.get())
        eAdresse = str(adrr.get())
        print("titre " + eTitre)
        # print(eNbr.text)
        pub = et.SubElement(tronc[0], 'publication')
        et.SubElement(pub, 'titre').text = eTitre
        et.SubElement(pub, 'nbpages').text = eNbr
        et.SubElement(pub, 'annee').text = eAnnee
        et.SubElement(pub, 'conference').text = eConference
        auteur = et.SubElement(pub, 'auteur')
        et.SubElement(auteur, 'nom').text = eNom
        et.SubElement(auteur, 'numtel').text = eNumTel
        et.SubElement(auteur, 'adresse').text = eAdresse
        # my_tree.write(et.tostring(tronc, 'UTF-8'), "publication.xml")
        my_tree.write(r"C:\Users\yassi\publication.xml")
        messagebox.showinfo("Statut de l'envoie", "publication enregistrée!")

    def back(self):
        self.main()
        # root.quit()

    def Rechercher(self):
        # root = Tk()
        self.title("Rechercher une publication")
        self.geometry("1920x1080")

        frame = Frame(self)
        frame.pack()
        bottomframe = Frame(self)
        bottomframe.pack(side=TOP)

        # Creation frames
        #     frame_page1_1 = Frame(root, bg="#D8DDD6")
        #     frame_page1_2 = Frame(root, bg="#D8DDD6")

        label_subtitle = Label(self, text="Veuillez remplir le champ suivant"
                               , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
        label_subtitle.pack(side=TOP, pady=10)

        l1 = Label(self, text="Element à recherhcer").pack()
        global nom
        nom = StringVar()
        e1 = Entry(self, textvariable=nom).pack()
        bTitre = Button(self, text="Rechercher par titre", command=self.rechercheParTitre).pack(pady=20)

        bConference = Button(self, text="Rechercher par confrence", command=self.Commande).pack(pady=20)

        bAuteur = Button(self, text="Rechercher par auteur", command=self.Commande).pack(pady=20)

        # Frame 2
        bouton_suivant1 = Button(self, text="Retour", font=("Arial", 20), bg="blue", fg="#D8DDD6",
                                 command=self.main)
        bouton_suivant1.pack()

    def Commande(self):
        messagebox.showinfo("Recherche", "Recherche en cours...Veuillez patientez")

    def rechercheParTitre(self):
        root = Tk()
        root.title("Rechercher une publication")
        root.geometry("1920x1080")

        frame = Frame(root)
        frame.pack()
        bottomframe = Frame(root)
        bottomframe.pack(side=TOP)
        l2 = Label(root, text="Titre").pack()
        eTitre = StringVar()
        e2 = Entry(root, textvariable=eTitre).pack()
        eTitre = r = e2

        l3 = Label(root, text="Nbres des Pages").pack()
        eNbr = Entry(root).pack()
        eNbr = eNbr

        l4 = Label(root, text="Année").pack()
        eAnnee = Entry(root).pack()
        eAnnee = eAnnee

        l5 = Label(root, text="Conference").pack()
        eConference = Entry(root).pack()
        eConference = eConference

        l6 = Label(root, text="Informations Auteur").pack()

        l7 = Label(root, text="Nom").pack()
        eNom = Entry(root).pack()
        eNom = eNom

        l9 = Label(root, text="Num Tel").pack()
        eNumTel = Entry(root).pack()
        eNumTel = eNumTel

        l10 = Label(root, text="Adresse").pack()
        eAdresse = Entry(root).pack()
        eAdresse = eAdresse

    def Supprimer(self):
        root = Tk()
        root.title("Supprimer une publication")
        root.geometry("1920x1080")

        frame = Frame(root)
        frame.pack()
        bottomframe = Frame(root)
        bottomframe.pack(side=TOP)

        label_subtitle = Label(root, text="Veuillez remplir le titre de la publication à supprimer"
                               , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
        label_subtitle.pack(side=TOP, pady=10)

        l1 = Label(root, text="le titre de la publication à supprimer").pack()
        e1 = Entry(root).pack()
        titr = e1.get()

        bSupp = Button(root, text="Supprimer", command=partial(self.delete_pub, titr), bg="red", fg="black").pack(pady=20)

        bAnnuler = Button(root, text="Annuler", command=self.Supprimer, bg="green", fg="black").pack(pady=20)

        # Frame 2
        bouton_back = Button(root, text="Retour", font=("Arial", 15), bg="blue", fg="#D8DDD6",
                             command=self.main)
        bouton_back.pack()

    def pub_existe(titre):
        for pub in tronc.findall("publication"):
            tag_titre = pub.find("titre").text
            if tag_titre == titre:
                return pub
        return False

    def delete_pub(self,titre):
        pub = self.pub_existe(titre)
        if not pub:
            self.Commande("echec de supprission", "pas de publication a supprimer")
        else:
            tronc.remove(pub)
            my_tree.write('publication.xml')

    def searchauteurnom(nom1):
        # nomc =nom.get()
        for pub in tronc.findall('publication'):
            for auteur in pub.findall("./auteur"):
                nom = auteur.find("nom")

                if (nom1 == nom.text):
                    # Comm("Affichage","publication trouvée!")
                    # printpub(pub)
                    # return (True)
                    for x in root.findall("publication"):
                        Label(text="les infos de l'auteur:", font=30, bd=1, relief=SOLID).place(x=25, y=120)
                        Label(text="Nom:").place(x=25, y=150)
                        # Label(text=eNom).place(x=60, y=150)
                        Label(text="Prénom:").place(x=25, y=170)
                        Label(text=x.find('prenom').text).place(x=75, y=170)
                        Label(text="age:").place(x=25, y=190)
                        Label(text=x.find('age').text).place(x=50, y=190)
                        Label(text="Publication:").place(x=25, y=210)
                        Label(text=x.find('nomlivre').text).place(x=90, y=210)
                        Label(text="Genre:").place(x=25, y=230)
                        Label(text=x.find('genre').text).place(x=65, y=230)

        print("pas de publication ")

    def Afficher(self):
        root = Tk()
        root.title("Ajouter une publication")
        root.geometry("1920x1080")

        frame = Frame(root)
        frame.pack()
        bottomframe = Frame(root)
        bottomframe.pack(side=TOP)

        # Creation frames
        #     frame_page1_1 = Frame(root, bg="#D8DDD6")
        #     frame_page1_2 = Frame(root, bg="#D8DDD6")

        # Frame 1
        label_title = Label(root, text="informations sur la publication recherchée", font=("Arial", 25), fg="black")
        label_title.pack(side=TOP, pady=10)

        # Frame 2
        bouton_suivant1 = Button(root, text="back", font=("Arial", 10), bg="black", fg="#D8DDD6",
                                 command=self.back)
        bouton_suivant1.pack()

        li = tkinter.Listbox()

    def CommandeSup(self):
        messagebox.showinfo("Supprimer une publication", "Un element sera supprimer! ")

    def CommandeAff(self):
        messagebox.showinfo("Afficher une publication", "Une publication a ete trouvée ")

    def Comm(nom, affiche):
        messagebox.showinfo(nom, affiche)


if __name__ == "__main__":
    app = App()
    app.mainloop()

# titre="vvvvv"
# eNbr=""
# eAnnee =""
# eConference=""
# eNom=""
# eNumTel=""
# eAdresse=""
#
#
# main()
# # Ajouter()
# # Rechercher()
# # Supprimer()
# window.mainloop()































# import xml.etree.ElementTree as et
# from functools import partial
# from logging import root
# from tkinter import *
# from tkinter import messagebox
#
# my_tree = et.parse(r"C:\Users\yassi\publication.xml")
# tronc = my_tree.getroot()
# window = Tk()
#
#
#
# # window.title("ProjetXml")
# # window.geometry("1920x1080")
# # window.minsize(480, 360)
# # window.config(background='#D8DDD6')
#
# def Ajouter():
#     root = Tk()
#     root.title("Ajouter une publication")
#     root.geometry("1920x1080")
#
#     frame = Frame(root)
#     frame.pack()
#     bottomframe = Frame(root)
#     bottomframe.pack(side=TOP)
#
#     # Creation frames
#     #     frame_page1_1 = Frame(root, bg="#D8DDD6")
#     #     frame_page1_2 = Frame(root, bg="#D8DDD6")
#
#     # Frame 1
#     label_title = Label(root, text="informations de la publication", font=("Arial", 25), fg="black")
#     label_title.pack(side=TOP, pady=10)
#
#     label_subtitle = Label(root, text="Veuillez remplir les champs suivants "
#                            , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
#     label_subtitle.pack(side=TOP, pady=10)
#
#
#
#     l2 = Label(root, text="Titre").pack()
#     e2 = Entry(root).pack()
#
#
#     l3 = Label(root, text="Nbres des Pages").pack()
#     e3 = Entry(root).pack()
#
#     l4 = Label(root, text="Année").pack()
#     e4 = Entry(root).pack()
#
#
#     l5 = Label(root, text="Conference").pack()
#     e5 = Entry(root).pack()
#
#
#     l6 = Label(root, text="Informations Auteur").pack()
#
#     l7 = Label(root, text="Nom").pack()
#     e7= Entry(root).pack()
#
#
#     l9 = Label(root, text="Num Tel").pack()
#     e8 = Entry(root).pack()
#
#
#     l10 = Label(root, text="Adresse").pack()
#     e9 = Entry(root).pack()
#
#
#     # def variables():
#     #     eConference = e5.get()
#     #     eNom = e7.get()
#     #     eAdresse = e9.get()
#     #     eNumTel = e8.get()
#     #     eTitre = e2.get()
#     #     eAnnee = e4.get()
#     #     eNbr = e3.get()
#     #     ajouterPublication(eTitre,eNbr,eAnnee,eConference,eNom,eNumTel,eAdresse)
#     #
#     Button(root, text="Envoyer",
#            command=partial(ajouterPublication(), e2, e3, e4, e5, e7, e8,
#                            e9)).pack(pady=50)
#     # b = Button(root ,text="Submit", command = variables()).pack(pady=20)
#
#     # Frame 2
#     bouton_suivant1 = Button(root, text="back", font=("Arial", 10), bg="black", fg="#D8DDD6",
#                              command=back)
#     bouton_suivant1.pack()
#
#     # Affichage frames
#
#
# #     frame_page1_1.pack(expand=YES)
# #     frame_page1_2.pack(expand=YES)
# #     window.mainloop()
#
#
#
#
# def main():
#     window = Tk()
#     window.title("ProjetXml")
#     window.geometry("1920x1080")
#
#     frame = Frame(window)
#     frame.pack()
#     bottomframe = Frame(window)
#     bottomframe.pack(side=TOP)
#
#     # Creation frames
#     frame_accueil = Frame(window, bg="#D8DDD6")
#
#     frame_accueil2 = Frame(window, bg="#D8DDD6")
#
#     # Frame 1
#     label_title = Label(frame_accueil, text="Bienvenue sur notre plateforme !", font=("Arial", 40), bg="#D8DDD6",
#                         fg="black")
#     label_title.pack()
#
#     # Frame2 : boutons
#     bouton_ajouter = Button(frame_accueil2, text="Ajouter une publication", font=("Arial", 25), bg="black",
#                             fg="#D8DDD6",
#                             command=ajout)
#     bouton_ajouter.grid(row=1, column=0)
#
#     bouton_supprimer = Button(frame_accueil2, text="Supprimer une publication", font=("Arial", 25), bg="black",
#                               fg="#D8DDD6",
#                               command=supp)
#     bouton_supprimer.grid(row=1, column=1)
#
#     bouton_recherche = Button(frame_accueil2, text="Rechercher une publication", font=("Arial", 25), bg="black",
#                               fg="#D8DDD6",
#                               command=recherche)
#     bouton_recherche.grid(row=1, column=2)
#
#     # Affichage frames
#     frame_accueil.pack(expand=YES)
#     frame_accueil2.pack(expand=YES)
#
#
# def ajout():
#     Ajouter()
#     window.destroy()
#
#
# #     window.quit()
# def supp():
#     Supprimer()
#
#
# #     window.quit()
# def recherche():
#     Rechercher()
#
#
# #     window.quit()
#
#
# def ajouterPublication(eTitre, eNbr, eAnnee, eConference, eNom, eNumTel, eAdresse):
#     pub = et.SubElement(tronc[0], 'publication')
#     et.SubElement(pub, 'titre').text = eTitre
#     et.SubElement(pub, 'nbpages').text = eNbr
#     et.SubElement(pub, 'nbpages').text = eAnnee
#     et.SubElement(pub, 'conference').text = eConference
#     auteur = et.SubElement(pub, 'auteur')
#     et.SubElement(auteur, 'nom').text = eNom
#     et.SubElement(auteur, 'numtel').text = eNumTel
#     et.SubElement(auteur, 'adresse').text = eAdresse
#
#     # my_tree.write(et.tostring(tronc, 'UTF-8'), "publication.xml")
#
#     my_tree.write(r"C:\Users\yassi\publication.xml")
#
#     messagebox.showinfo("Statut de l'envoie", "publication enregistrée!")
#
#
# def back():
#     main()
#     root.quit()
#
# def Rechercher():
#     root = Tk()
#     root.title("Rechercher une publication")
#     root.geometry("1920x1080")
#
#     frame = Frame(root)
#     frame.pack()
#     bottomframe = Frame(root)
#     bottomframe.pack(side=TOP)
#
#     # Creation frames
#     #     frame_page1_1 = Frame(root, bg="#D8DDD6")
#     #     frame_page1_2 = Frame(root, bg="#D8DDD6")
#
#     label_subtitle = Label(root, text="Veuillez remplir le champ suivant"
#                            , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
#     label_subtitle.pack(side=TOP, pady=10)
#
#     l1 = Label(root, text="Element à recherhcer").pack()
#     e1 = Entry(root).pack()
    bTitre = Button(root, text="Rechercher par titre", command=Commande).pack(pady=20)

    bConference = Button(root, text="Rechercher par confrence", command=Commande).pack(pady=20)

    bAuteur = Button(root, text="Rechercher par auteur", command=Commande).pack(pady=20)

    # Frame 2
    bouton_suivant1 = Button(root, text="Retour", font=("Arial", 20), bg="blue", fg="#D8DDD6",
                             command=main)
    bouton_suivant1.pack()


# recherche
# def Commande():
#     messagebox.showinfo("Recherche", "Recherche en cours...Veuillez patientez")
#
# def rechercheParTitre():
#     root = Tk()
#     root.title("Rechercher une publication")
#     root.geometry("1920x1080")
#
#     frame = Frame(root)
#     frame.pack()
#     bottomframe = Frame(root)
#     bottomframe.pack(side=TOP)
#     l2 = Label(root, text="Titre").pack()
#     e2 = Entry(root).pack()
#     eTitre = r = e2
#
#     l3 = Label(root, text="Nbres des Pages").pack()
#     eNbr = Entry(root).pack()
#     eNbr = eNbr
#
#     l4 = Label(root, text="Année").pack()
#     eAnnee = Entry(root).pack()
#     eAnnee = eAnnee
#
#     l5 = Label(root, text="Conference").pack()
#     eConference = Entry(root).pack()
#     eConference = eConference
#
#     l6 = Label(root, text="Informations Auteur").pack()
#
#     l7 = Label(root, text="Nom").pack()
#     eNom = Entry(root).pack()
#     eNom = eNom
#
#     l9 = Label(root, text="Num Tel").pack()
#     eNumTel = Entry(root).pack()
#     eNumTel = eNumTel
#
#     l10 = Label(root, text="Adresse").pack()
#     eAdresse = Entry(root).pack()
#     eAdresse = eAdresse
#
#
# def Supprimer():
#     root = Tk()
#     root.title("Supprimer une publication")
#     root.geometry("1920x1080")
#
#     frame = Frame(root)
#     frame.pack()
#     bottomframe = Frame(root)
#     bottomframe.pack(side=TOP)
#
#
#     label_subtitle = Label(root, text="Veuillez remplir le titre de la publication à supprimer"
#                            , font=("Arial", 20), fg="black")  # bg="#D8DDD6"
#     label_subtitle.pack(side=TOP, pady=10)
#
#     l1 = Label(root, text="le titre de la publication à supprimer").pack()
#     e1 = Entry(root).pack()
#     titr=e1.get()
#
#     bSupp = Button(root, text="Supprimer", command=partial(delete_pub,titr), bg="red", fg="black").pack(pady=20)
#
#     bAnnuler = Button(root, text="Annuler", command=Supprimer, bg="green", fg="black").pack(pady=20)
#
#     # Frame 2
#     bouton_back = Button(root, text="Retour", font=("Arial", 15), bg="blue", fg="#D8DDD6",
#                          command=main)
#     bouton_back.pack()
#
# def pub_existe(titre):
#     for pub in tronc.findall("publication"):
#         tag_titre=pub.find("titre").text
#         if tag_titre==titre:
#             return pub
#     return False
#
# def delete_pub(titre):
#     pub=pub_existe(titre)
#     if not pub:
#         Commande("echec de supprission","pas de publication a supprimer")
#     else:
        tronc.remove(pub)
        my_tree.write('publication.xml')

# recherche
def Commande():
    messagebox.showinfo("Supprimer une publication", "Un element sera supprimer! ")

main()
# Ajouter()
# Rechercher()
# Supprimer()
window.mainloop()