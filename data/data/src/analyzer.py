import csv
from collections import defaultdict

def charger_depenses(fichier):
    depenses = []
    with open(fichier, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for ligne in reader:
            ligne["montant"] = float(ligne["montant"])
            depenses.append(ligne)
    return depenses


def analyser_depenses(depenses):
    total = 0
    par_categorie = defaultdict(float)

    for d in depenses:
        total += d["montant"]
        par_categorie[d["categorie"]] += d["montant"]

    return total, par_categorie


def generer_insights(total, par_categorie):
    insights = []
    categorie_max = max(par_categorie, key=par_categorie.get)
    part = (par_categorie[categorie_max] / total) * 100

    insights.append(
        f"La catégorie la plus coûteuse est **{categorie_max}**, représentant {part:.1f}% des dépenses totales."
    )

    if part > 30:
        insights.append(
            f"Une optimisation de la catégorie **{categorie_max}** pourrait avoir un impact significatif sur le budget."
        )

    return insights


def afficher_rapport(total, par_categorie, insights):
    print("\n📊 RAPPORT D'ANALYSE BUDGÉTAIRE\n")
    print(f"Dépenses totales : {total:.2f} $\n")

    print("Répartition par catégorie :")
    for cat, montant in par_categorie.items():
        print(f"- {cat} : {montant:.2f} $")

    print("\n🔍 Insights :")
    for i in insights:
        print(f"- {i}")


def main():
    depenses = charger_depenses("data/expenses.csv")
    total, par_categorie = analyser_depenses(depenses)
    insights = generer_insights(total, par_categorie)
    afficher_rapport(total, par_categorie, insights)


if __name__ == "__main__":
    main()
