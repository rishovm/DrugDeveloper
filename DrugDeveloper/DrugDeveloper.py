import re

def predict_toxicity(smiles):
    # Basic heuristics
    mol_weight = 100 + len(smiles) * 5  # Simple estimate
    logp = round(len(re.findall(r'C', smiles)) * 0.3 + len(re.findall(r'N|O', smiles)) * 0.2, 2)
    h_donors = len(re.findall(r'NH2|OH', smiles))
    h_acceptors = len(re.findall(r'O|N', smiles))
    ro5_violations = int((mol_weight > 500) + (logp > 5) + (h_donors > 5) + (h_acceptors > 10))
    toxicity_risk = "Low"
    if ro5_violations >= 2:
        toxicity_risk = "High"
    elif ro5_violations == 1:
        toxicity_risk = "Moderate"

    return {
        "Estimated Mol. Weight": mol_weight,
        "Estimated LogP": logp,
        "H-Donors": h_donors,
        "H-Acceptors": h_acceptors,
        "RO5 Violations": ro5_violations,
        "Toxicity Risk": toxicity_risk
    }

def simulate_metabolism(smiles):
    metabolism_rules = {
        r'CH3': 'COOH',                # oxidation of methyl to acid
        r'OH': 'O-Glucuronide',        # Phase II conjugation
        r'NH2': 'NHOH',                # oxidation of amines
        r'Cl': 'OH',                   # oxidative dehalogenation
        r'Br': 'OH',                   # oxidative dehalogenation
        r'CCC': 'COC',                 # oxidative cleavage of alkyl chain
    }
    products = []
    for pattern, product in metabolism_rules.items():
        if re.search(pattern, smiles):
            new_smiles = re.sub(pattern, product, smiles, count=1)
            products.append((pattern, product, new_smiles))
    return products

def suggest_bioisosteres(smiles):
    replacements = {
        r'OH': ['NH2', 'F'],
        r'Cl': ['F', 'Br'],
        r'CH3': ['CF3', 'NH2'],
        r'NO2': ['CN', 'COOH'],
        r'COOH': ['SO2NH2', 'PO3H2'],
        r'Br': ['Cl', 'F'],
        r'CCC': ['CCN', 'COC']
    }
    suggestions = []
    for pattern, subs in replacements.items():
        if re.search(pattern, smiles):
            for sub in subs:
                new_smiles = re.sub(pattern, sub, smiles, count=1)
                suggestions.append((pattern, sub, new_smiles))
    return suggestions

def print_dict(title, data):
    print(f"\n🔬 {title}:")
    print("-" * 45)
    for k, v in data.items():
        print(f"{k:<30} {v}")
    print()

def main():
    smiles = input("Enter the SMILES code of the compound: ").strip()

    # Toxicity Prediction
    tox_data = predict_toxicity(smiles)
    print_dict("Predicted Toxicity", tox_data)

    # Metabolism Simulation
    metabolism = simulate_metabolism(smiles)
    print("\n🧬 Simulated Metabolic Transformations:")
    if metabolism:
        for original, metabolite, transformed in metabolism:
            print(f"Pattern '{original}' → '{metabolite}' ➜ {transformed}")
    else:
        print("No metabolism rules matched.")

    # Bioisosteric Replacement Suggestions
    suggestions = suggest_bioisosteres(smiles)
    print("\n💡 Bioisosteric Suggestions:")
    if suggestions:
        for original, replacement, transformed in suggestions:
            print(f"Replace '{original}' → '{replacement}' ➜ {transformed}")
    else:
        print("No suitable replacements found.")

if __name__ == "__main__":
    main()
