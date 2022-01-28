FROM python:3.10-alpine

# Installation du paquet fastapi
RUN pip install fastapi
# Installation du paquet uvicorn
RUN pip install uvicorn
# Installation du paquet pymongo
RUN pip install pymongo
# Installation du paquet requests
RUN pip install requests


# Copie du repertoire courant dans le repertoire de travail
COPY . .

# Le conteneur ecoute sur le port 3000
EXPOSE 3000

# Lancement du serveur uvicorn
# Note : besoin de bind le serveur a l'adresse 0.0.0.0 pour que 
# le traffic venant de l'exterieur du conteneur soit aussi accepte
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "3000"]

