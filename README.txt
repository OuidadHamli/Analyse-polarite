# Sentiments et polarité

**Version 1.0.0**

Sentiments et polarite est un code Python pour gérer la polarité de mots en faisant référence à un lexique déjà existant. 
Les instructions qui vont êtres réalisées sont les suivantes:
1. Ouvrir un fichier de texte, et lire son contenu en mémoire
2. Ouvrir un lexique au format tabulé, récupérer chaque champ dans une structure de données
3. Découper en mots une phrase entrée par l'utilisateur (vous, donc) au démarrage du programme
4. Pour chaque mot, vérifier s'il est présent dans la structure de données, si oui lui associer sa polarité.


#Prérequis

Code écrit et testé avec la version 3 de python.
Pour fonctionner, le code a besoin que le module spaCy français soit installé. Pour cela, tapez les lignes suivantes dans votre terminal:

pip3 install -U spacy
python3 -m spacy download fr_core_news_sm


## Installation

Pour commencer le code Sentiments et polarité il faut suivre les importations suivantes:

```bash

import spacy
import fr_core_news_sm
nlp = fr_core_news_sm.load()

```


## Usage

```python
import spacy

fichier = open("polarimots_1.1.lex", "r") #permet de faire la lecture d'un fichier lorsque le code se trouve dans le même dossier
```


## Support

Pour plus de détails sur notre code, contactez-nous.
Emails: Sarah Decottignies (sarah.decottignies@hotmail.fr)
Camille Wadoux (wadocam@yahoo.fr)
Marie Berteloot (marie.berteloot@hotmail.com)
Christina Petri (christina.petri.etu@univ-lille.fr)


## Contribution

Les demandes de tirage sont les bienvenues. Pour les changements majeurs, veuillez d'abord ouvrir un problème pour discuter de ce que vous aimeriez changer.


## Visuels

Une vidéo avec la description principale du code en français pourrait être fournie


## Auteurs et remerciements

Νous remercions notre professeur, M. Antonio Balvet, qui a contribué au projet via ses conseils et suggestions.


## License

Autorisé sous le [MIT](https://choosealicense.com/licenses/mit/)