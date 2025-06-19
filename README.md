DrugDeveloper is a lightweight Python tool that predicts the toxicity, simulates metabolic transformations, and suggests bioisosteric replacements for small molecule drug candidates using simple SMILES input—no coding experience or external chemistry libraries (like RDKit) required.

Designed for students, educators, and early-stage researchers, this script helps demystify core concepts in drug development, such as pharmacokinetics, metabolism, and molecular optimization, using a rule-based and interpretable approach.

🚀 Features
✅ Toxicity Estimation
Quickly evaluates molecular weight, logP, H-bond donors/acceptors, and Lipinski's Rule of 5 violations.

✅ Metabolic Simulation
Uses regex-based transformations to predict how molecules may be metabolized (e.g., oxidation, dehalogenation, conjugation).

✅ Bioisosteric Suggestions
Recommends functional group replacements that may reduce toxicity or improve bioavailability.

✅ No External Dependencies
Pure Python — no RDKit, Open Babel, or external cheminformatics tools needed.

✅ CLI-Based Interactive Tool
Asks for user input (SMILES string) and prints clear, organized results to the terminal.

🧪 Example
bash
Copy
Edit
$ python DrugDeveloper.py
Enter the SMILES code of the compound: CC(=O)NC1=CC=C(C=C1)O

🔬 Predicted Toxicity:
Estimated Mol. Weight       273
Estimated LogP              2.6
H-Donors                    1
H-Acceptors                 2
RO5 Violations              0
Toxicity Risk               Low

🧬 Simulated Metabolic Transformations:
Pattern 'CH3' → 'COOH' ➜ CCOOH(=O)NC1=CC=C(C=C1)O

💡 Bioisosteric Suggestions:
Replace 'OH' → 'NH2' ➜ CC(=O)NC1=CC=C(C=C1)NH2
Replace 'OH' → 'F' ➜ CC(=O)NC1=CC=C(C=C1)F
📂 Use Cases
Educational tool in drug discovery & medicinal chemistry workshops

Quick structure-based screening for compound optimization

Teaching basic ADME/Tox concepts without complex software setup

Supporting structure-based discussions in pharmacology or cheminformatics

🛠️ How to Use
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/DrugDeveloper.git
cd DrugDeveloper
Run the script:

bash
Copy
Edit
python DrugDeveloper.py
Enter a valid SMILES string when prompted.

🧠 Limitations
Rule-based: Based on Lipinski's rule.

Simplified estimates for MW and logP.

Not suitable for production-grade modeling—meant for education and exploration.

