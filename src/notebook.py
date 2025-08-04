# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

from datetime import datetime

datetime.now()

class Note:

    HIGH: str="High"
    MEDIUM: str = "Medium"
    LOW: str="Low"


    def __init__(self,code,title,text,importance):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()