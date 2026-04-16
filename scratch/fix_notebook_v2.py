import json

ntbk_path = '/home/prophet/Downloads/Notebook_Projects/src/Notebook/heart_disease_xgboost.ipynb'
with open(ntbk_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

target_found = False
for cell in nb['cells']:
    if cell['cell_type'] == 'code' and any('new_patients = pd.DataFrame(' in line for line in cell['source']):
        # Updated code for step 10
        # Reformatting as list of strings (standard for ipynb)
        new_source = [
            "new_patients = pd.DataFrame({\n",
            "    'age':           [45,    62,    38,    55  ],\n",
            "    'gender':        [1,     0,     1,     0   ],\n",
            "    'impluse':       [80,    95,    70,    88  ],\n",
            "    'pressurehight': [130,   165,   118,   145 ],\n",
            "    'pressurelow':   [85,    100,   75,    92  ],\n",
            "    'glucose':       [120,   210,   88,    160 ],\n",
            "    'kcm':           [1.5,   3.2,   0.7,   2.1 ],\n",
            "    'troponin':      [0.01,  0.18,  0.002, 0.09],\n",
            "})\n",
            "\n",
            "# Fix: Reorder columns to match training features\n",
            "new_patients = new_patients[X.columns]\n",
            "\n",
            "preds = model.predict(new_patients)\n",
            "probs = model.predict_proba(new_patients)\n",
            "\n",
            "new_patients['result']            = pd.Series(preds).map({1: '🔴 Positive', 0: '🟢 Negative'})\n",
            "new_patients['prob_negative (%)'] = (probs[:, 0] * 100).round(1)\n",
            "new_patients['prob_positive (%)'] = (probs[:, 1] * 100).round(1)\n",
            "\n",
            "print('═' * 45)\n",
            "print('    HEART DISEASE PREDICTION RESULTS')\n",
            "print('═' * 45)\n",
            "display(new_patients)\n",
            "\n",
            "pos = (preds == 1).sum()\n",
            "neg = (preds == 0).sum()\n",
            "print(f'\\nSummary: {pos} Positive  |  {neg} Negative  |  {len(preds)} Total')"
        ]
        cell['source'] = new_source
        target_found = True
        break

if target_found:
    with open(ntbk_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1)
    print("Notebook updated successfully.")
else:
    print("Could not find the target cell.")
