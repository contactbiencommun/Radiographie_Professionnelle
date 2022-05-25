import streamlit as st
import datetime as dt
import FunctionWebApp as fw
import time
import smtplib, ssl
import yagmail
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from tempfile import NamedTemporaryFile
from fpdf import FPDF
from PIL import Image
from paquet.database18mai22 import*

class Bilan:
    """Donne les résultats sous forme graphique"""
    def __init__(self,
                liste_domaine,
                liste_intéret_generaux

                ):

        self.liste_domaine=liste_domaine
        self.liste_intéret_generaux=liste_intéret_generaux





    def domainedesintérêt(self, range_note):
        """donne le score par domaine d'intérêt"""
        mon_dict_domaine = {self.liste_domaine[0]: (range_note[0] + range_note[23] + range_note[34]
                                              + range_note[45] + range_note[56] + range_note[67]
                                              + range_note[78] + range_note[89] + range_note[100]),
                            self.liste_domaine[1]: (range_note[1] + range_note[12] + range_note[35]
                                              + range_note[46] + range_note[57] + range_note[68]
                                              + range_note[79] + range_note[90] + range_note[101]),
                            self.liste_domaine[2]: (range_note[2] + range_note[13] + range_note[24]
                                              + range_note[47] + range_note[58] + range_note[69]
                                              + range_note[80] + range_note[91] + range_note[102]),

                            self.liste_domaine[3]: (range_note[3] + range_note[14] + range_note[25]
                                              + range_note[36] + range_note[59] + range_note[70]
                                              + range_note[81] + range_note[92] + range_note[103]),

                            self.liste_domaine[4]: (range_note[4] + range_note[15] + range_note[26]
                                              + range_note[37] + range_note[48] + range_note[71]
                                              + range_note[82] + range_note[93] + range_note[104]),

                            self.liste_domaine[5]: (range_note[5] + range_note[16] + range_note[27]
                                              + range_note[38] + range_note[49] + range_note[60]
                                              + range_note[83] + range_note[94] + range_note[105]),

                            self.liste_domaine[6]: (range_note[6] + range_note[17] + range_note[28]
                                              + range_note[39] + range_note[50] + range_note[61]
                                              + range_note[72] + range_note[95] + range_note[106]),

                            self.liste_domaine[7]: (range_note[7] + range_note[18] + range_note[29]
                                              + range_note[40] + range_note[51] + range_note[62]
                                              + range_note[73] + range_note[84] + range_note[107]),

                            self.liste_domaine[8]: (range_note[8] + range_note[19] + range_note[30]
                                              + range_note[41] + range_note[52] + range_note[63]
                                              + range_note[74] + range_note[85] + range_note[96]),

                            self.liste_domaine[9]: (range_note[9] + range_note[20] + range_note[31]
                                              + range_note[42] + range_note[53] + range_note[64]
                                              + range_note[75] + range_note[86] + range_note[97]),

                            self.liste_domaine[10]: (range_note[10] + range_note[21] + range_note[32]
                                               + range_note[43] + range_note[54] + range_note[65]
                                               + range_note[76] + range_note[87] + range_note[98]),

                            self.liste_domaine[11]: (range_note[11] + range_note[22] + range_note[33]
                                               + range_note[44] + range_note[55] + range_note[66]
                                               + range_note[77] + range_note[88] + range_note[99])}

        return mon_dict_domaine


    def get_interet_etalonne(self, range_note, sexe):
        """donne l'etalonnage par domaine d'intérêt en fonction du score et du sexe"""
        if sexe == "M" or sexe == "m":
            d = self.domainedesintérêt(range_note)
            mon_dict_final = {self.liste_domaine[0]: dict_domaine_intéret('Plein_air_H')[d[self.liste_domaine[0]]],
                              self.liste_domaine[1]: dict_domaine_intéret('Technique_H')[d[self.liste_domaine[1]]],
                              self.liste_domaine[2]: dict_domaine_intéret('Calcul_H')[d[self.liste_domaine[2]]],
                              self.liste_domaine[3]: dict_domaine_intéret('Scientifique_H')[d[self.liste_domaine[3]]],
                              self.liste_domaine[4]: dict_domaine_intéret('Contacts_personnels_H')[d[self.liste_domaine[4]]],
                              self.liste_domaine[5]: dict_domaine_intéret('Esthétique_H')[d[self.liste_domaine[5]]],
                              self.liste_domaine[6]: dict_domaine_intéret('Littéraire_H')[d[self.liste_domaine[6]]],
                              self.liste_domaine[7]: dict_domaine_intéret('Musical_H')[d[self.liste_domaine[7]]],
                              self.liste_domaine[8]: dict_domaine_intéret('Service_social_H')[d[self.liste_domaine[8]]],
                              self.liste_domaine[9]: dict_domaine_intéret('Travail_de_bureau_H')[d[self.liste_domaine[9]]],
                              self.liste_domaine[10]: dict_domaine_intéret('Pratique_H')[d[self.liste_domaine[10]]],
                              self.liste_domaine[11]: dict_domaine_intéret('Médical_H')[d[self.liste_domaine[11]]],

                              }


        else:
            d = self.domainedesintérêt(range_note)
            mon_dict_final = {self.liste_domaine[0]: dict_domaine_intéret('Plein_air_F')[d[self.liste_domaine[0]]],
                              self.liste_domaine[1]: dict_domaine_intéret('Technique_F')[d[self.liste_domaine[1]]],
                              self.liste_domaine[2]: dict_domaine_intéret('Calcul_F')[d[self.liste_domaine[2]]],
                              self.liste_domaine[3]: dict_domaine_intéret('Scientifique_F')[d[self.liste_domaine[3]]],
                              self.liste_domaine[4]: dict_domaine_intéret('Contacts_personnels_F')[d[self.liste_domaine[4]]],
                              self.liste_domaine[5]: dict_domaine_intéret('Esthétique_F')[d[self.liste_domaine[5]]],
                              self.liste_domaine[6]: dict_domaine_intéret('Littéraire_F')[d[self.liste_domaine[6]]],
                              self.liste_domaine[7]: dict_domaine_intéret('Musical_F')[d[self.liste_domaine[7]]],
                              self.liste_domaine[8]: dict_domaine_intéret('Service_social_F')[d[self.liste_domaine[8]]],
                              self.liste_domaine[9]: dict_domaine_intéret('Travail_de_bureau_F')[d[self.liste_domaine[9]]],
                              self.liste_domaine[10]: dict_domaine_intéret('Pratique_F')[d[self.liste_domaine[10]]],
                              self.liste_domaine[11]: dict_domaine_intéret('Médical_F')[d[self.liste_domaine[11]]],

                              }

        return mon_dict_final


#========================================Fonction pour graphique "intéret généraux===================================

    def intérêt_généraux(self, range_note):
        """donne le score par personnalité"""
        dict_domainedesintérêt = self.domainedesintérêt(range_note)

        dict_domaine2 = {
                         self.liste_intéret_generaux[0]: (2 * dict_domainedesintérêt[self.liste_domaine[3]]
                                                          + dict_domainedesintérêt[self.liste_domaine[11]]),
                         self.liste_intéret_generaux[1]: (dict_domainedesintérêt[self.liste_domaine[7]]
                                                          +dict_domainedesintérêt[self.liste_domaine[5]]
                                                          + dict_domainedesintérêt[self.liste_domaine[6]]),
                         self.liste_intéret_generaux[2]: dict_domainedesintérêt[self.liste_domaine[8]],
                         self.liste_intéret_generaux[3]: dict_domainedesintérêt[self.liste_domaine[4]],
                         self.liste_intéret_generaux[4]: (dict_domainedesintérêt[self.liste_domaine[2]]
                                                          +dict_domainedesintérêt[self.liste_domaine[9]]),
                         self.liste_intéret_generaux[5]: (dict_domainedesintérêt[self.liste_domaine[0]]
                                                         + dict_domainedesintérêt[self.liste_domaine[10]]
                                                         + dict_domainedesintérêt[self.liste_domaine[1]])
                         }

        return dict_domaine2

    def intérêt_généraux_etalonne(self, range_note, sexe):
        """ donne l'étalonnage par personnalité en fonction du score et du sexe"""
        if sexe == "M" or sexe == "m":
            d = self.intérêt_généraux(range_note)

            mon_interet_final = {self.liste_intéret_generaux[0]: dict_personnalité('Investigateur_H')[d[self.liste_intéret_generaux[0]]],
                                 self.liste_intéret_generaux[1]: dict_personnalité('Artiste_H')[d[self.liste_intéret_generaux[1]]],
                                 self.liste_intéret_generaux[2]: dict_personnalité('Social_H')[d[self.liste_intéret_generaux[2]]],
                                 self.liste_intéret_generaux[3]: dict_personnalité('Entreprenant_H')[d[self.liste_intéret_generaux[3]]],
                                 self.liste_intéret_generaux[4]: dict_personnalité('Conventionnel_H')[d[self.liste_intéret_generaux[4]]],
                                 self.liste_intéret_generaux[5]: dict_personnalité('Réaliste_H')[d[self.liste_intéret_generaux[5]]]
                                 }
        else:
            d = self.intérêt_généraux(range_note)

            mon_interet_final =  {self.liste_intéret_generaux[0]: dict_personnalité('Investigateur_F')[d[self.liste_intéret_generaux[0]]],
                                 self.liste_intéret_generaux[1]: dict_personnalité('Artiste_F')[d[self.liste_intéret_generaux[1]]],
                                 self.liste_intéret_generaux[2]: dict_personnalité('Social_F')[d[self.liste_intéret_generaux[2]]],
                                 self.liste_intéret_generaux[3]: dict_personnalité('Entreprenant_F')[d[self.liste_intéret_generaux[3]]],
                                 self.liste_intéret_generaux[4]: dict_personnalité('Conventionnel_F')[d[self.liste_intéret_generaux[4]]],
                                 self.liste_intéret_generaux[5]: dict_personnalité('Réaliste_F')[d[self.liste_intéret_generaux[5]]]
                                 }

        return mon_interet_final


