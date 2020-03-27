# Programme pour l'analyse des polarite des mots d'une phrase

import spacy
import fr_core_news_sm
nlp = fr_core_news_sm.load()

#OUVERTURE D'UN LEXIQUE
fichier = open("polarimots_1.1.lex", "r")
contenu = []
for line in fichier:
    contenu.append(line)

print("entrez la phrase à analyser:")
sentence = input()

#SEGMENTATION EN MOTS ET LEMMATISATION
def segmentation_en_mots (content):
    mots = nlp(content)
    mot_lemme = {}
    for token in mots:
        mot_lemme[token.text] = token.lemma_
    return mot_lemme

#RECHERCHE DU MOT DANS LE LEXIQUE
def trouve_mot(lemme):
    for item in contenu:
        liste_item = item.split()
        if lemme == liste_item[1]:
            polarite = liste_item[3]
            return polarite
    return 'UNK'

#AFFICHAGE DE LA POLARITE DE CHAQUE MOT
def affichage(phrase):
    tokens_result = segmentation_en_mots(sentence)
    for word in tokens_result:
        polarite = trouve_mot(tokens_result[word])
        print(word+"\t"+polarite)

affichage(sentence)

fichier.flush()
fichier.close()
