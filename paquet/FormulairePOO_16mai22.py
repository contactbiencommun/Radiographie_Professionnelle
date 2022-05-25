import streamlit as st
import datetime as dt
import time
import smtplib, ssl
import yagmail
from PIL import Image

class Formulaire:
    """ Création de formulaire de contact"""

    def __init__(self,
                 nom,
                 prénom,
                 ddn,
                 formation,
                 emploi,
                 sexe_sujet,
                 emploi_envisagé,
                 numtel,
                 Email,
                 user1,
                 mypassword,
                 mailto,
                 sujet,
                 messageRes,
                 nom_bouton_soumettre,

                 date="Data",


                 ):

        self.nom = nom
        self.prénom = prénom
        self.ddn = ddn
        self.formation = formation
        self.emploi = emploi
        self.sexe_sujet = sexe_sujet
        self.emploi_envisagé = emploi_envisagé
        self.numtel = numtel
        self.Email = Email
        self.user1 = user1
        self.mypassword = mypassword
        self.mailto = mailto
        self.sujet = sujet
        self.messageRes = messageRes
        self.date = date
        self.nom_bouton_soumettre=nom_bouton_soumettre

    def cree_en_tête(self,image,titre,sous_titre):
        """crée l'entête du site"""
        st.image(image)
        st.title(titre)
        st.subheader(sous_titre)

    def cree_test(self):

        st.subheader("TEST")


    def cree_formulaire(self):
        """crée un formulaire """
        with st.form(key='my_form'):
            nom = st.text_input(self.nom," ")
            prénom = st.text_input(self.prénom)
            ddn = st.text_input(self.ddn)
            formation = st.text_input(self.formation)
            emploi = st.text_input(self.emploi)
            sexe_sujet = st.text_input(self.sexe_sujet)
            emploi_envisagé = st.text_input(self.emploi_envisagé)
            numtel = st.text_input(self.numtel," ")
            Email = st.text_input(self.Email," ")
                                  #if "is_ok" in st.session_state:
               #" st.session_state["is_ok"] = True

            #st.write(st.session_state["is_ok"])
            #st.write("avant", st.session_state)
            submit_button1 = st.form_submit_button(label=self.nom_bouton_soumettre)

            if submit_button1:
            #   if nom==None or numtel==None or Email==None:
              #      st.session_state["is_ok"] = not st.session_state["is_ok"]
                #st.write("apres", st.session_state)
                dateCompletDuJour = str(dt.datetime.today().isoformat())[0:16]

                message_mail = self.date + " :" + dateCompletDuJour + "\n" + self.nom + " :" + nom + "\n" + self.prénom + " :" + prénom + "\n" + \
                               self.ddn + " :" + ddn + "\n" + \
                               self.formation + " :" + formation + "\n" + self.emploi + " :" + emploi + "\n" + \
                               self.sexe_sujet + " :" + sexe_sujet + "\n" + self.emploi_envisagé + " :" + emploi_envisagé + "\n" + \
                               self.numtel + " :" + numtel + "\n" + self.Email + " :" + Email

                yag = yagmail.SMTP(user=self.user1, password=self.mypassword)
                # sending the email
                yag.send(to=self.mailto, subject=self.sujet, contents=message_mail)

                st.success(self.messageRes)
                st.write(nom)
                st.write(numtel)
                st.write(Email)

            return (nom,numtel,Email,sexe_sujet)


