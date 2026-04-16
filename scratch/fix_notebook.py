import nbformat as nbf

# Load the notebook
ntbk_path = '/home/prophet/Downloads/Notebook_Projects/src/Notebook/heart_disease_xgboost.ipynb'
with open(ntbk_path, 'r', encoding='utf-8') as f:
    nb = nbf.read(f, as_version=4)

# Look for the cell containing the new_patients construction
target_cell_index = -1
for i, cell in enumerate(nb.cells):
    if cell.cell_type == 'code' and 'new_patients = pd.DataFrame(' in cell.source:
        target_cell_index = i
        break

if target_cell_index != -1:
    # Updated code for step 10
    new_source = """new_patients = pd.DataFrame({
    'age':           [45,    62,    38,    55  ],
    'gender':        [1,     0,     1,     0   ],
    'impluse':       [80,    95,    70,    88  ],
    'pressurehight': [130,   165,   118,   145 ],
    'pressurelow':   [85,    100,   75,    92  ],
    'glucose':       [120,   210,   88,    160 ],
    'kcm':           [1.5,   3.2,   0.7,   2.1 ],
    'troponin':      [0.01,  0.18,  0.002, 0.09],
})

# Fix: Reorder columns to match training features
new_patients = new_patients[X.columns]

preds = model.predict(new_patients)
probs = model.predict_proba(new_patients)

new_patients['result']            = pd.Series(preds).map({1: '🔴 Positive', 0: '🟢 Negative'})
new_patients['prob_negative (%)'] = (probs[:, 0] * 100).round(1)
new_patients['prob_positive (%)'] = (probs[:, 1] * 100).round(1)

print('═' * 45)
print('    HEART DISEASE PREDICTION RESULTS')
print('═' * 45)
display(new_patients)

pos = (preds == 1).sum()
neg = (preds == 0).sum()
print(f'\\nSummary: {pos} Positive  |  {neg} Negative  |  {len(preds)} Total')"""
    
    nb.cells[target_cell_index].source = new_source
    
    # Write back
    with open(ntbk_path, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)
    print("Notebook updated successfully.")
else:
    print("Could not find the target cell.")
