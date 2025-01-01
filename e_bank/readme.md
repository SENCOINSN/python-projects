script python permettant de gérer la gestion des comptes bancaires

Dans ce programme,

-creation d'un compte bancaire
-depot d'argent
-retrait d'argent
-affichage du solde
-affichage des operations
-affichage du compte

On a deux type de comptes :
-compte courant
-compte epargne

avec le compte courant, on peut faire un virement vers un autre compte et aussi faire un retrait en banque , faire un depot en banque sur le compte 

le compte epargne ne peut faire que des depots et des retraits
avec un taux d'interet de 0.5%

Un compte a un numéro de compte unique constitué de 20 chiffres

un montant solde ,

la classe Client:

nom et prenom du proprietaire
numero de telephone,
email,
adresse
un username et un mot de passe

Un client est attaché à un compte:

un client peut disposer au maximum de 2 comptes (courant et epargne)


chaque compte dispose de plusieurs operations

La classe Operation:
 -date
 -montant
 -type (depot,retrait,virement)
 -numero de compte (avec le numero de compte du compte auquel elle est attaché)


 Toutes les operations sont enregistrées dans un dictionnaire 
 avec un indentifiant unique comme clés

 A l'issu toutes ces operations sont enregistrées dans un fichier texte

 Ce fichier texte peut être lu et affiché


 Le programme évoluera en passant vers un rest api backend avec 
 flask et sqlalchemy mysql