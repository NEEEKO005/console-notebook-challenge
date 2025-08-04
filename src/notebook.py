from datetime import datetime
from typing import List

class Note:
    # Constantes de clase
    HIGH: str = 'HIGH'
    MEDIUM: str = 'MEDIUM'
    LOW: str = 'LOW'

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code: str = code
        self.title: str = title
        self.text: str = text
        self.importance: str = importance
        self.creation_date: datetime = datetime.now()
        self.tags: List[str] = []

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    