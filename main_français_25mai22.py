from paquet.database18mai22 import*
from paquet.FormulairePOO_16mai22 import*
from paquet.RadiographiePOO_18mai22 import*
from paquet.BilanPOO_22mai22 import*
import FunctionWebApp as fw
import streamlit as st
from PIL import Image

def main(version):

    img1=Image.open("ImageMin.png")

    st.set_page_config(page_title="Bien Commun",
                       page_icon=img1,
                       layout="wide"
                        )

    image = "ImageBC.png"
    titre = dict_element_formulaire('titre', version)
    st.image(image)


    st.title(titre)

    fw.insert_video(dict_element_formulaire('video_de_présentation', version))

    formulaire = Formulaire(nom=dict_element_formulaire('nom', version),
                            prénom=dict_element_formulaire('prénom', version),
                            ddn=dict_element_formulaire('ddn', version),
                            formation=dict_element_formulaire('formation', version),
                            emploi=dict_element_formulaire('emploi', version),
                            sexe_sujet=dict_element_formulaire('sexe_sujet', version),
                            emploi_envisagé=dict_element_formulaire('emploi_envisagé', version),
                            numtel=dict_element_formulaire('numtel', version),
                            Email=dict_element_formulaire('Email', version),
                            user1=dict_element_formulaire('user1', version),
                            mypassword=dict_element_formulaire('mypassword', version),
                            mailto=dict_element_formulaire('mailto', version),
                            sujet=dict_element_formulaire('sujet', version),
                            messageRes=dict_element_formulaire('messageRes', version),
                            nom_bouton_soumettre=dict_element_formulaire('nom_bouton_soumettre', version)
                            )

    formulaire.cree_en_tête(image="ImageBC.png",
                            titre=dict_element_formulaire('titre', version),
                            sous_titre=dict_element_formulaire('sous_titre', version)
                            )

    is_ok=False
    v = formulaire.cree_formulaire()
    #st.write(v[0]) # nom
    #st.write(v[1])#numtel
    #st.write(v[2])#Email
    #st.write(v[3])#sexe_sujet

    if v[0]!=" " and v[1]!=" "and v[2] !=" "and v[3] !=" ":
        is_ok=True

    #st.write(is_ok)

    init_intitule = dict_element_formulaire('init_intitule', version)
    init_msgChoixNote = dict_element_formulaire('init_msgChoixNote', version)
    init_msgVerif = dict_element_formulaire('init_msgVerif', version)
    init_msgErreur = dict_element_formulaire('init_msgErreur', version)
    init_msg1 = dict_element_formulaire('init_msg1', version)
    init_msg2 = dict_element_formulaire('init_msg2', version)
    init_msg3 = dict_element_formulaire('init_msg3', version)
    init_msg4 = dict_element_formulaire('init_msg4', version)
    init_msg5 = dict_element_formulaire('init_msg5', version)
    init_msg6 = dict_element_formulaire('init_msg6', version)
    init_msg7 = dict_element_formulaire('init_msg7', version)
    init_msg8 = dict_element_formulaire('msg_error_formula', version)

    radiographieA = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST A",
        nom_test2="TEST B",
        i_débuttemp=0,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieB = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST B",
        nom_test2="TEST C",
        i_débuttemp=12,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"

    )

    radiographieC = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST C",
        nom_test2="TEST D",
        i_débuttemp=24,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieD = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST D",
        nom_test2="TEST E",
        i_débuttemp=36,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieE = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST E",
        nom_test2="TEST F",
        i_débuttemp=48,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieF = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST F",
        nom_test2="TEST G",
        i_débuttemp=60,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieG = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST G",
        nom_test2="TEST H",
        i_débuttemp=72,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieH = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST H",
        nom_test2="TEST I",
        i_débuttemp=84,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    radiographieI = Radiographie(
        range_metier=get_liste_métier(version),
        nom_test1="TEST I",
        nom_test2=dict_element_formulaire('bilan', version),
        i_débuttemp=96,
        intitule=init_intitule,
        msgChoixNote=init_msgChoixNote,  # msg "choisissez une note"
        msgVerif=init_msgVerif,  # Bouton "Vérification"
        msgErreur=init_msgErreur,  # "ERREUR: CHAQUE METIER DOIT AVOIR UNE NOTE DIFFERENTE!!!!  "
        msg1=init_msg1,  # "la note"
        msg2=init_msg2,  # "se répète"
        msg3=init_msg3,  # "les notes"
        msg4=init_msg4,  # "se répètent"
        msg5=init_msg5,  # "est diponible"
        msg6=init_msg6,  # "sont disponible"
        msg7=init_msg7  # "vous pouvez passer au"
    )

    # edit formulaire A

    result = radiographieA.edit_test(version)
    totalnote = result[0]
    totalmetier = result[1]
    verifT = []
    verifT.append(result[2])

    # edit formulaire B

    result1 = radiographieB.edit_test(version)
    totalnote = totalnote + result1[0]
    totalmetier = totalmetier + result1[1]
    verifT.append(result1[2])

    # edit formulaire C

    result2 = radiographieC.edit_test(version)
    totalnote = totalnote + result2[0]
    totalmetier = totalmetier + result2[1]
    verifT.append(result2[2])

    # edit formulaire D

    result3 = radiographieD.edit_test(version)
    totalnote = totalnote + result3[0]
    totalmetier = totalmetier + result3[1]
    verifT.append(result3[2])

    # edit formulaire E

    result4 = radiographieE.edit_test(version)
    totalnote = totalnote + result4[0]
    totalmetier = totalmetier + result4[1]
    verifT.append(result4[2])

    # edit formulaire F

    result5 = radiographieF.edit_test(version)
    totalnote = totalnote + result5[0]
    totalmetier = totalmetier + result5[1]
    verifT.append(result5[2])

    # edit formulaire G

    result6 = radiographieG.edit_test(version)
    totalnote = totalnote + result6[0]
    totalmetier = totalmetier + result6[1]
    verifT.append(result6[2])

    # edit formulaire H

    result7 = radiographieH.edit_test(version)
    totalnote = totalnote + result7[0]
    totalmetier = totalmetier + result7[1]
    verifT.append(result7[2])

    # edit formulaire I

    result8 = radiographieI.edit_test(version)
    totalnote = totalnote + result8[0]
    totalmetier = totalmetier + result8[1]
    verifT.append(result8[2])

    if is_ok==False:
     st.error(init_msg8)
    else:
# =============================================================================================
#                                 Proposition d'envoi d"un rapport par mail
#/////////////////////////////////////////////////////////////////////////////////////////////
        genre = st.radio(
            dict_element_formulaire('msg_rapport_pdf', version),
            (dict_element_formulaire('oui', version), dict_element_formulaire('non', version)))

        if genre == dict_element_formulaire('oui', version):
            adressmail = st.text_input(dict_element_formulaire('entrez adresse email', version))

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////:::
#                                            RESULTATS DU TEST
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        st.markdown(dict_element_formulaire("msg_markdown", version))

        with st.form(key='metier3'):
            col1, col2, col3 = st.columns(3)

            with col1:
                métier1 = st.text_input(dict_element_formulaire("métier1", version))

            with col2:
                métier2 = st.text_input(dict_element_formulaire("métier2", version))
            with col3:
                métier3 = st.text_input(dict_element_formulaire("métier3", version))

            submitted = st.form_submit_button(dict_element_formulaire("Obtenir les résultats", version))

            if submitted == True:

                if (verifT[0] == False and verifT[1] == False and verifT[2] == False and verifT[3] == False and \
                        verifT[4] == False and verifT[5] == False and verifT[6] == False and verifT[7] == False and
                        verifT[
                            8] == False):
                    st.success(dict_element_formulaire("Tests terminés", version))




                    time.sleep(2)

                    # ==========================================================================================================
                    st.subheader(dict_element_formulaire("Intérêts généraux", version))

                    def plot_radar(data1, data2):
                        df = pd.DataFrame(dict(r=data1, theta=data2))
                        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
                        st.plotly_chart(fig, use_container_width=True)

                    sexe_sujet=v[3]

                    dtemp = intérêt_généraux_etalonne(get_liste_domaine(version), totalnote, sexe_sujet,version)

                    r = list(dtemp.values())

                    theta = list(dtemp.keys())

                    plot_radar(r, theta)

                    # =======================================================================================================

                    st.subheader(dict_element_formulaire("Domaines des intérêts spécifiques", version))


                    def plot_bar(domaines, val):
                        fig = go.Figure(go.Bar(
                            x=val,
                            y=domaines,
                            marker={'color': val,
                                    'colorscale': 'blugrn'},
                            orientation='h'))
                        st.plotly_chart(fig, use_container_width=True)

                    # d1=domainedesintérêt(liste_domaine, totalnote)

                    d1 = get_interet_etalonne(get_liste_domaine(version), totalnote, sexe_sujet,version)

                    d_list = list(d1.values())

                    domaines =get_liste_domaine(version)
                    val = d_list

                    d = {'domaines': domaines, 'val': val}
                    df = pd.DataFrame(data=d)
                    df1 = df.sort_values(by=['val'], ascending=True)

                    plot_bar(df1['domaines'], df1['val'])

                    # ================================================ EMAILING RAPPORT=======================================================


                    # bar chart
                    fig = go.Figure(go.Bar(
                        x=df1['val'],  # val,
                        y=df1['domaines'],  # domaines,
                        marker={'color': val,
                                'colorscale': 'blugrn'},
                        orientation='h'))
                    fig.update_layout(title_text=dict_element_formulaire("Domaines des intérêts spécifiques", version), title_x=0.5)

                    # radar chart
                    df = pd.DataFrame(dict(r=r, theta=theta))
                    fig2 = px.line_polar(df, r='r', theta='theta', line_close=True)
                    fig2.update_layout(title_text=dict_element_formulaire("Intérêts généraux", version), title_x=0.5)

                    with NamedTemporaryFile("r+b", delete=False) as fd:
                        fig.write_image(fd)
                        fd.seek(0)

                    with NamedTemporaryFile("r+b", delete=False) as fd1:
                        fig2.write_image(fd1)
                        fd1.seek(0)

                    pdf = FPDF()

                    pdf.add_page()

                    pdf.set_font("Arial", "B", size=15)

                    pdf.cell(180, 15, txt=dict_element_formulaire("VOTRE BILAN DE COMPETENCE", version),
                             ln=1, align='C')

                    pdf.set_font('Arial', "IU", size=14)
                    pdf.cell(180, 15, txt=dict_element_formulaire("Résultats de votre Radiographie Professionnelle", version),
                             ln=2, align='C')

                    pdf.image(fd1.name, x=20, y=40, w=160, h=120)

                    pdf.image(fd.name, x=30, y=150, w=144, h=108)

                    pdf.image("StickerOrange.png", x=5, y=5)

                    if version=="française":
                        bas_de_page="Capture.png"
                    else:
                        bas_de_page = "CaptureRoumain.png"

                    pdf.image(bas_de_page, x=30, y=270)

                    with NamedTemporaryFile("r+b", delete=False, suffix='.pdf') as fd3:
                        pdf.output(fd3)
                        fd3.seek(0)

                    user1 = "contactbiencommun@gmail.com"
                    mypassword = "2022Succes."
                    yag = yagmail.SMTP(user=user1, password=mypassword)
                    mailto1=user1 #envoi du rapport à bien commun
                    nom_prospect=v[0]
                    numtel_prospect=v[1]
                    email_prospect=v[2]
                    sexe_prospect=v[3]
                    message_bien_commun = f"Rapport du prospect : {nom_prospect}, de numero de tel:{numtel_prospect}, email:{email_prospect}, de sexe:{sexe_prospect}"
                    yag.send(to=mailto1, subject='Nouveau prospect', contents=message_bien_commun, attachments=fd3.name)

                    if genre == "Oui":
                        mailto = adressmail
                        message_prospect = dict_element_formulaire("Veuillez trouver ci-joint votre rapport", version)
                       # sending the email
                        yag.send(to=mailto, subject=dict_element_formulaire("Votre radiographine professionelle", version), contents=message_prospect, attachments=fd3.name)

                    fd.close()
                    fd1.close()
                    fd3.close()

                    st.success(dict_element_formulaire("Rapport Envoyé", version))

            else:
                    indice = [index for index, element in enumerate(verifT) if element == True]
                    verif2 = ["A", "B", "C", "D", "E","F","G","H","I"]
                    verif_indice=[verif2[index] for index in indice]

                    if len(indice)==1:
                        error_rempli_test=dict_element_formulaire("Le test de personnalité", version)+" "+' '.join(verif_indice)+" "+dict_element_formulaire("est mal fait", version)
                    else:
                        error_rempli_test=dict_element_formulaire("Les tests de personnalité", version)+" "+' '.join(verif_indice)+" "+dict_element_formulaire("sont mal faits", version)

                    st.error(error_rempli_test)


if __name__ == "__main__":

    vers = st.sidebar.radio(
        "Version/Versiune",
        ('française','română'))

    if vers=='française':
        vers=1
    elif vers=='română':
        vers=2

    if vers==1:
        version = "française"
    elif vers==2:
        version = "roumaine"

    main(version)

