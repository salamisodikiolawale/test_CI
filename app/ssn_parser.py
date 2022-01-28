import json
import requests
from datetime import datetime
from constants import MONTH_MAP

def sex_from_ssn(ssn):
    """Extract sex from ssn value
    """
    val : str = ssn[0]
    if val == "1":
        return "Homme"
    elif val == "2":
        return "Femme"
    return "Inconnu"

def birth_date_from_ssn(ssn):
    """Extract birth date from ssn value
    """
    month : int = int(ssn[3:5])
    year : str = ssn[1:3]
    if month <= 12:
        return MONTH_MAP[month] + " " + year
    elif month >= 31 and month <= 42:
        return MONTH_MAP[month - 30] + year
    return "Inconnu"

def birth_place_from_ssn(ssn):
    """Extract place of birth from ssn value
    """
    dept : str = ssn[5:7]
    commune : str = ssn[5:10]
    # Case etranger
    if dept == "99":
        res = json.loads(open("pays.json"))
        return res[dept]
    else:
        # Case DOM-TOM
        if dept in ["97" or "98"]:
            dept = ssn[5:8]        
        dept_res = requests.get(f"https://geo.api.gouv.fr/departements/{dept}")
        commune_res = requests.get(f"https://geo.api.gouv.fr/communes/{commune}")
        return {"departement": dept_res.json()["nom"], "commune": commune_res.json()["nom"]}

def position_from_ssn(ssn):
    """Extract position from ssn
    """
    return ssn[10:13]
