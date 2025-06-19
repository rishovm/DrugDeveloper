def lipinski_rules(smiles):
    # Simplified estimations by string patterns for demo
    mol_weight = estimate_mol_weight(smiles)
    logp = estimate_logp(smiles)
    h_donors = smiles.count('O') + smiles.count('N')  # crude count of donors
    h_acceptors = smiles.count('O') + smiles.count('N')  # crude acceptors
    ro5_violations = 0
    if mol_weight > 500:
        ro5_violations += 1
    if logp > 5:
        ro5_violations += 1
    if h_donors > 5:
        ro5_violations += 1
    if h_acceptors > 10:
        ro5_violations += 1
    return mol_weight, logp, h_donors, h_acceptors, ro5_violations

def estimate_mol_weight(smiles):
    # Very rough molecular weight estimate by count of atoms
    atom_weights = {'C':12, 'H':1, 'O':16, 'N':14, 'S':32, 'P':31, 'F':19, 'Cl':35, 'Br':80, 'I':127}
    weight = 0
    i = 0
    while i < len(smiles):
        # Check two-letter atoms
        if i+1 < len(smiles) and smiles[i:i+2] in atom_weights:
            weight += atom_weights[smiles[i:i+2]]
            i += 2
        elif smiles[i] in atom_weights:
            weight += atom_weights[smiles[i]]
            i += 1
        else:
            i += 1
    return weight

def estimate_logp(smiles):
    # Simplified estimate: count hydrophobic groups minus polar groups
    hydrophobic = smiles.count('C') + smiles.count('F') + smiles.count('Cl') + smiles.count('Br') + smiles.count('I')
    polar = smiles.count('O') + smiles.count('N') + smiles.count('S') + smiles.count('P')
    return round(hydrophobic*0.3 - polar*0.5, 1)  # arbitrary weights

def predict_toxicity(logp, ro5_violations):
    if ro5_violations >= 2 or logp > 5:
        return "High"
    elif ro5_violations == 1 or logp > 3.5:
        return "Moderate"
    else:
        return "Low"

def predict_metabolism(smiles):
    metabolism = []
    if 'C(=O)O' in smiles or 'COC=' in smiles:  # ester group present
        metabolism.append("Ester hydrolysis likely: ester → carboxylic acid + alcohol")
    if 'C' in smiles:  # crude check for alkyl side chains
        metabolism.append("Possible oxidation on alkyl side chains to hydroxyl or carboxyl groups")
    if 'OH' in smiles or 'O' in smiles:
        metabolism.append("Possible aromatic hydroxylation")
    if not metabolism:
        metabolism.append("No metabolism rules matched.")
    return metabolism

def suggest_bioisosteric_replacements(smiles):
    suggestions = []
    if 'C(=O)O' in smiles or 'COC=' in smiles:
        suggestions.append("Consider replacing ester with amide to improve metabolic stability.")
    if 'OH' in smiles:
        suggestions.append("Replace aromatic hydroxyl groups with fluorine or methyl to improve metabolic stability.")
    if 'N' in smiles:
        suggestions.append("Consider modifying nitrogen-containing groups to reduce toxicity.")
    if not suggestions:
        suggestions.append("No suitable bioisosteric replacements found.")
    return suggestions

def main():
    print("DrugDeveloper - Simple Metabolism and Bioisosteric Prediction Tool")
    smiles = input("Enter the SMILES code of the compound: ").strip()

    mol_weight, logp, h_donors, h_acceptors, ro5_violations = lipinski_rules(smiles)
    toxicity = predict_toxicity(logp, ro5_violations)
    metabolism = predict_metabolism(smiles)
    bioisosteres = suggest_bioisosteric_replacements(smiles)

    print("\n🔬 Predicted Toxicity:")
    print("---------------------------------------------")
    print(f"Estimated Mol. Weight          {mol_weight}")
    print(f"Estimated LogP                 {logp}")
    print(f"H-Donors                      {h_donors}")
    print(f"H-Acceptors                   {h_acceptors}")
    print(f"RO5 Violations                {ro5_violations}")
    print(f"Toxicity Risk                 {toxicity}")

    print("\n🧬 Simulated Metabolic Transformations:")
    for m in metabolism:
        print("-", m)

    print("\n💡 Bioisosteric Suggestions:")
    for b in bioisosteres:
        print("-", b)

if __name__ == "__main__":
    main()
