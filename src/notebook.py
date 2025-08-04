# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

from datetime import datetime
from typing import List


class Note:

    HIGH: str="High"
    MEDIUM: str = "Medium"
    LOW: str="Low"


    def __init__(self,code,title,text,importance):
        self.code:int = code
        self.title:str = title
        self.text:str = text
        self.importance:str = importance
        self.creation_date = datetime.now()
        self.tags: List[str] = []
