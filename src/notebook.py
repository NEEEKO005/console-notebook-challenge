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

    def __str__(self)->str:
        return f"Date: {self.creation_date}\n{self.title}: {self.text}"


class Notebook:

    def __init__(self):
        self.notes: List[Note] = []

    def add_note(self, title: str, text: str, importance: str) -> str:
       code: str =str(len(self.notes) + 1)
       note: Note = Note(code, title, text, importance)
       self.notes.append(note)
       return code

    def delete_note(self, code: str):
        for note in self.notes:
            if note.code == code:
                self.notes.remove(note)

    def import_note(self) -> list[Note]:
        important: List[str] = []
        for note in self.notes:
            if note.importance == Note.HIGH or note.importance == Note.MEDIUM:
                important.append(note)
        return important

    def notes_by_tag(self, tag: str) -> List[Note]:
        notes: List[Note] = []
        for note in self.notes:
            if tag in note.tags:
                notes.append(note)
        return notes

    def tag_with_most_notes(self) -> str:


