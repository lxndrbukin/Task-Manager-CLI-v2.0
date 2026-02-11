import uuid
from datetime import datetime

class Task():
    def __init__(self, title, desc, priority, status):
        self._id = str(uuid.uuid4())
        self._title = title
        self._desc = desc
        self._priority = priority
        self._status = status
        self._creation_date = datetime.now().isoformat()

    @property
    def title(self):
        return self._title
    @property
    def desc(self):
        return self._desc
    @property
    def priority(self) -> str:
        return self._priority
    @property
    def status(self) -> str:
        return self._status
    @status.setter
    def status(self, new_status):
        self._status = new_status
    @property
    def creation_date(self):
        return self._creation_date

    def to_dict(self):
        return {
            "id": self._id,
            "title": self.title,
            "desc": self.desc,
            "priority": self.priority,
            "status": self.status,
            "creation_date": self.creation_date
        }