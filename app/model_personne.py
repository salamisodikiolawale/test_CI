import re
from pydantic import BaseModel, validator

class ModelPersonne(BaseModel):
    nom: str
    prenom: str
    ssn: str

    @validator("ssn")
    def control_ssn_value(cls, value):
        """Controls the Ssn value.
        """
        # Il faudra que vous remplissiez ce code, par defaut il retournera True
        return True

    @validator("ssn")
    def control_ssn_key(cls, value):
        """Controls the Ssn key.
        """
        # Il faudra que vous remplissiez ce code, par defaut il retournera True
        return True

