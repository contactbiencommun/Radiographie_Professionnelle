import streamlit as st
import datetime as dt
import FunctionWebApp as fw
import time
import smtplib, ssl
from PIL import Image
from paquet.database18mai22 import*


class Radiographie:
    """construction du test"""
    def __init__(self,
                 range_metier,
                 nom_test1,
                 nom_test2,
                 i_débuttemp,
                 intitule,               # "Test de personnalité : "
                 msgChoixNote,           #msg "choisissez une note"
                 msgVerif,               #Bouton "Vérification"
                 msgErreur,              #"ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
                 msg1,                   #"la note"
                 msg2,                   #"se répète"
                 msg3,                   #"les notes"
                 msg4,                   #"se répètent"
                 msg5,                   #"est diponible"
                 msg6,                   # "sont disponible"
                 msg7,                   # "vous pouvez passer au"


                 ):
        self.range_metier=range_metier
        self.nom_test1=nom_test1
        self.nom_test2=nom_test2
        self.i_débuttemp=i_débuttemp
        self.intitule=intitule
        self.msgChoixNote=msgChoixNote
        self.msgVerif=msgVerif
        self.msgErreur=msgErreur
        self.msg1 = msg1
        self.msg2 = msg2
        self.msg3 = msg3
        self.msg4 = msg4
        self.msg5 = msg5
        self.msg6 = msg6
        self.msg7 = msg7


    def edit_test(self,version):
        """edit the different tests"""
        nomkey = self.intitule+ self.nom_test1

        st.subheader(nomkey)

        with st.form(key=nomkey):
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                listeA = []
                listeA.append(self.range_metier[self.i_débuttemp])
                listeA.append(self.range_metier[self.i_débuttemp + 1])
                listeA.append(self.range_metier[self.i_débuttemp + 2])

                liste1 = []
                for elem in listeA:
                    st.write(elem)
                    expander = st.expander(dict_element_formulaire("Définition de",version)+" "+elem)
                    definition_metier=definition_metiers(version)[elem]
                    expander.write(definition_metier)
                    liste1.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            with col2:
                listeB = []
                listeB.append(self.range_metier[self.i_débuttemp + 3])
                listeB.append(self.range_metier[self.i_débuttemp + 4])
                listeB.append(self.range_metier[self.i_débuttemp + 5])

                liste2 = []
                for elem in listeB:
                    st.write(elem)
                    expander = st.expander(dict_element_formulaire("Définition de", version) + " " + elem)
                    definition_metier = definition_metiers(version)[elem]
                    expander.write(definition_metier)
                    liste2.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            with col3:
                listeC = []
                listeC.append(self.range_metier[self.i_débuttemp + 6])
                listeC.append(self.range_metier[self.i_débuttemp + 7])
                listeC.append(self.range_metier[self.i_débuttemp + 8])

                liste3 = []
                for elem in listeC:
                    st.write(elem)
                    expander = st.expander(dict_element_formulaire("Définition de", version) + " " + elem)
                    definition_metier = definition_metiers(version)[elem]
                    expander.write(definition_metier)
                    liste3.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            with col4:
                listeD = []
                listeD.append(self.range_metier[self.i_débuttemp + 9])
                listeD.append(self.range_metier[self.i_débuttemp + 10])
                listeD.append(self.range_metier[self.i_débuttemp + 11])

                liste4 = []
                for elem in listeD:
                    st.write(elem)
                    expander = st.expander(dict_element_formulaire("Définition de", version) + " " + elem)
                    definition_metier = definition_metiers(version)[elem]
                    expander.write(definition_metier)
                    liste4.append(
                        st.slider(label=self.msgChoixNote, min_value=1, max_value=12, key=elem))

            joinedlist = liste1 + liste2 + liste3 + liste4
            joinedmétier = listeA + listeB + listeC + listeD
            verif = True
            if not (fw.checkIfDuplicates_1(joinedlist)):
                verif = False

            submitted = st.form_submit_button(self.msgVerif)

            if submitted:

                if fw.checkIfDuplicates_1(joinedlist):

                    m1 =self.msgErreur
                    listduplicat = fw.getduplicat(joinedlist)
                    if len(listduplicat) == 1:
                        mess = self.msg1 + str(listduplicat) + self.msg2
                        st.error(m1 + mess)
                    else:
                        mess = self.msg3 + str(listduplicat) +self.msg4
                        st.error(m1 + mess)
                    note_total = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
                    notedispo = fw.getnotedispo(joinedlist, note_total)
                    if len(notedispo) == 1:
                        mess2 = self.msg1 + str(notedispo) + self.msg5
                        st.error(mess2)
                    else:
                        mess2 = self.msg3 + str(notedispo) + self.msg6
                        st.error(mess2)

                else:
                    verif = False
                    nom_test_temp = self.msg7 + self.nom_test2
                    st.success(nom_test_temp)

        return (joinedlist, joinedmétier, verif)


