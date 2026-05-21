from fastapi  import FastAPI
import json

app = FastAPI()

def charger_etudiants():
    with open("etudiants.json", "r", encoding="utf-8") as f:
        return json.load(f)


@app.get("/")
def accueil():
    return("Api creer avec succes !!! ")

@app.get("/etudiants")
def liste_etudiant():
    charger_etudiants()