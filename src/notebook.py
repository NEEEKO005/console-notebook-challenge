from datetime import datetime
from typing import List

class Note:
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


class Notebook:

    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> int:
        new_code = 1
        existing_codes = {int(note.code) for note in self.notes}
        while new_code in existing_codes:
            new_code += 1

        new_note = Note(str(new_code), title, text, importance)
        self.notes.append(new_note)

        return new_code