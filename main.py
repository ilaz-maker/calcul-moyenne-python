def calcul_moyenne_generale():
    print("Calculateur de Moyenne Générale")
    
    nb_matieres = int(input("Combien de matières avez-vous ? : "))
    
    total_points = 0
    total_coeffs = 0
    
    for i in range(1, nb_matieres + 1):
        print(f"\n Matière {i} ")
        
        coeff = float(input("Coefficient : "))
        nb_notes = int(input("Nombre de notes dans cette matière : "))
        
        somme_notes = 0
        
        for j in range(1, nb_notes + 1):
            note = float(input(f"  - Note {j} (sur 20) : "))
            somme_notes += note

        moyenne_matiere = somme_notes / nb_notes
        print(f"  → Moyenne de la matière : {round(moyenne_matiere, 2)}")
        
        total_points += moyenne_matiere * coeff
        total_coeffs += coeff

    moyenne_generale = total_points / total_coeffs if total_coeffs != 0 else 0

    print("\n Résultat final ")
    print(f"Moyenne générale : {round(moyenne_generale, 2)} / 20")


if __name__ == "__main__":
    calcul_moyenne_generale()
