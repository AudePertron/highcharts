import pandas as pd
import numpy as np

#récupération du fichier
df =pd.read_csv('transition.csv',sep = ",")
list(df.columns)


#drop des dats inutiles
df.drop(['id','title',
 'createdAt',
 'publishedAt',
 'updatedAt',
 'trashed',
 'trashedStatus',
 'authorId',
 'authorType',
 'authorZipCode',
"QUXVlc3Rpb246MTYw - Quel est aujourd'hui pour vous le problème concret le plus important dans le domaine de l'environnement ?",
 'QUXVlc3Rpb246MTYx - Que faudrait-il faire selon vous pour apporter des réponses à ce problème ?',
          'QUXVlc3Rpb246MTUz - Si oui, que faudrait-il faire pour vous convaincre ou vous aider à changer de mode de chauffage ?',
 "QUXVlc3Rpb246MTU0 - Avez-vous pour vos déplacements quotidiens la possibilité de recourir à des solutions de mobilité alternatives à la voiture individuelle comme les transports en commun, le covoiturage, l'auto-partage, le transport à la demande, le vélo, etc. ?",
 'QUXVlc3Rpb246MTU1 - Si oui, que faudrait-il faire pour vous convaincre ou vous aider à utiliser ces solutions alternatives ?',
 'QUXVlc3Rpb246MjA3 - Si non, quelles sont les solutions de mobilité alternatives que vous souhaiteriez pouvoir utiliser ?',
 'QUXVlc3Rpb246MTU3 - Et qui doit selon vous se charger de vous proposer ce type de solutions alternatives ?',
 "QUXVlc3Rpb246MTU4 - Que pourrait faire la France pour faire partager ses choix en matière d'environnement au niveau européen et international ?",
 "QUXVlc3Rpb246MTU5 - Y a-t-il d'autres points sur la transition écologique sur lesquels vous souhaiteriez vous exprimer ?",
    'QUXVlc3Rpb246MTQ3 - Si oui, de quelle manière votre vie quotidienne est-elle touchée par le changement climatique ?',
 "QUXVlc3Rpb246MTQ5 - Si oui, que faites-vous aujourd'hui pour protéger l'environnement et/ou que pourriez-vous faire ?",
       "QUXVlc3Rpb246MTUw - Qu'est-ce qui pourrait vous inciter à changer vos comportements comme par exemple mieux entretenir et régler votre chauffage, modifier votre manière de conduire ou renoncer à prendre votre véhicule pour de très petites distances ?",
       'QUXVlc3Rpb246MTUx - Quelles seraient pour vous les solutions les plus simples et les plus supportables sur un plan financier pour vous inciter à changer vos comportements ?'        

        ], axis=1, inplace = True)

#renommer colonnes
df = df.rename(columns={"QUXVlc3Rpb246MTQ2 - Diriez-vous que votre vie quotidienne est aujourd'hui touchée par le changement climatique ?": "quotidien", "QUXVlc3Rpb246MTQ4 - À titre personnel, pensez-vous pouvoir contribuer à protéger l'environnement ?": "personnel", "QUXVlc3Rpb246MTUy - Par rapport à votre mode de chauffage actuel, pensez-vous qu'il existe des solutions alternatives plus écologiques ?": "chauffage"})
print(df.columns)

#calcul des pourcentages
quotidien = df['quotidien'].value_counts(normalize=True) * 100
personnel = df['personnel'].value_counts(normalize=True) * 100
chauffage = df['chauffage'].value_counts(normalize=True) * 100

quotidien_oui = round(quotidien[0],2)
quotidien_non = round(quotidien[1],2)
personnel_oui = round(personnel[0],2)
personnel_non = round(personnel[1],2)
chauffage_oui = round(chauffage[0],2)
chauffage_non = round(chauffage[1],2)

