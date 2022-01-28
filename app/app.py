from fastapi import FastAPI, HTTPException
from model_personne import ModelPersonne
from db import database
import ssn_parser

app = FastAPI()

@app.get("/personnes")
def fetch_personnes():
    db = database()
    results = db.personnes.find()
    personnes = []
    for result in results:
        p = {"nom": result["nom"], "prenom": result["prenom"],
             "ssn": result["ssn"]}
        personnes.append(p)
    return personnes

@app.post("/personnes/")
def create_personne(personne: ModelPersonne):
    
    db = database()
    if db.personnes.find_one({"ssn":personne.ssn}) is not None:
        HTTPException(status=404, detail="Ssn is already registered")

    result = db.personnes.insert_one(personne.dict())
    return personne.dict()

# @app.get("/personnes/{ssn}")
# def fetch_personne_by_ssn(ssn: str):
#     db = database()
#     result = db.personnes.find_one({"ssn":ssn})
#     personne = {"nom": result["nom"], "prenom": result["prenom"],
#                 "ssn": result["ssn"]}
#     return personne

@app.get("/personnes/{ssn}/{id}")
def fetch_personne_by_ssn(ssn: str, id:int, sex: bool = False, birth_date: bool = False,
                          birth_place: bool = False, position: bool = False):
    print("#################################", id)
    db = database()
    result = db.personnes.find_one({"ssn":ssn})
    personne = {"nom": result["nom"], "prenom": result["prenom"],
                "ssn": result["ssn"]}
    if sex:
        sex_val = ssn_parser.sex_from_ssn(ssn)
        personne["sex"] = sex_val
    if birth_date:
        birth_date_val = ssn_parser.birth_date_from_ssn(ssn)
        personne["birth_date"] = birth_date_val
    if birth_place:
        birth_place_val = ssn_parser.birth_place_from_ssn(ssn)
        personne["birth_place"] = birth_place_val
    if position:
        position_val = ssn_parser.position_from_ssn(ssn)
        personne["position"] = position_val
    return personne

@app.delete("/personnes/{ssn}")
def delete_personne_by_ssn(ssn: str):
    db = database()
    db.personnes.delete_one({"ssn":ssn})

@app.put("/personnes/{ssn}")
def update_personne_by_ssn(ssn: str, personne: ModelPersonne):
    db = database()
    result = db.personnes.update_one({"ssn":ssn}, {"$set": personne.dict()})
    return personne.dict()
