import pandas as pd
import os

# Path to your CSV file
input_csv = "/home/bio/TrmD_drug_design_project/REINVENT/results/stage2_v2_1.csv"  # Replace with your CSV file path
output_dir = "reinvent1_output_pdbqt_v2"  # Directory to save PDBQT files
os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist

# Read the CSV file with proper delimiter and encoding
try:
    data = pd.read_csv(input_csv, delimiter=",", encoding="utf-8-sig")
except Exception as e:
    print(f"Error reading CSV: {e}")
    exit()

# Check if 'Smiles' column exists
if 'SMILES' not in data.columns:
    raise ValueError("CSV file must have a 'Smiles' column")

# Initialize counters
total_molecules = len(data)
successful_conversions = 0
failed_conversions = []


counter = 0  


for index, row in data.iterrows():
    counter += 1
    smiles = row['SMILES']
    molecule_id = counter  
    output_pdbqt = os.path.join(output_dir, f"{molecule_id}.pdbqt")
    
    result = os.system(f'obabel -:"{smiles}" -O {output_pdbqt} --gen3d -p')
    
   
    if result == 0:  
        successful_conversions += 1
    else:
        failed_conversions.append(molecule_id)

# Summary
print(f"Total molecules in CSV: {total_molecules}")
print(f"Successfully converted molecules: {successful_conversions}")
print(f"Failed conversions: {len(failed_conversions)}")

if failed_conversions:
    print("Failed molecule IDs:")
    for mol in failed_conversions:
        print(mol)
