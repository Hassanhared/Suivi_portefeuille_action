prix_actions = {"AAPL": 180,
                 "TSLA": 250,
                 "MHDF": 300
                }
portefeuile = {}
total = 0
print("Action disponibles:", ",".join(prix_actions.keys()))
while True:
    tache = input("donnez le nom du tache (ou 'fin' pour terminer):\n").upper()
    if tache == "FIN":
        break
    if tache not in prix_actions:
        print("Erreur: Action non reconnu\n")
        continue
    try:
        quant = int(input("donnez la quantité\n"))
        if quant <= 0:
            print("La quantité doit etre positive\n")
            continue
        portefeuile[tache] = quant
    except ValueError:
        print("Erreur: entrer un nombre valide\n")
print("----Résumé du portefeuille----")
for tache, quant in portefeuile.items():
    prix_unitaires = prix_actions[tache]
    valeur = prix_unitaires * quant
    total += valeur
    print(f"{tache}: {quant} x {prix_unitaires} $ = {valeur} $")
print(f" valeur total est {total} $")
sauvegarder = input("voulez-vous sauvegarder le resultat? (o/n) :").lower()
if sauvegarder == "o":
    with open("portefeuille.txt", "w") as f:
        f.write("---- Résumé du portefeuille ----")
        for tache, quant in portefeuile.items():
            valeur = prix_actions[tache] * quant
            f.write(f"{tache}: {quant} x {prix_actions[tache]} $ = {valeur} $ \n")
        f.write(f"valeur total : {total} $ ")
    print("Resultat sauvegardé dans 'portefeuille.txt'.")