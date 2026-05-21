import pandas as pd

data = pd.read_csv("donnees_propres.csv")
print(data)

#data_json=data.to_json("donnees_valides.json", orient="records", force_ascii=False, indent=4 )
data_json_indexe=data.to_json("donnees_valides_indexe.json", orient="index", force_ascii=False, indent=4 )