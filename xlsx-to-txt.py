import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

file = os.path.join(script_dir, "rfam-whitelist.xlsx")

df = pd.read_excel(file, header=None)

families_ids = df.iloc[:, 0]

families_ids.to_csv(os.path.join(script_dir, "rfam-whitelist.txt"), index=False, header=False)

print(families_ids)
