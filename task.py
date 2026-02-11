import uuid
from datetime import datetime
from enum import Enum

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Task():
    def __init__(self,
                 title,
                 desc,
                 priority,
                 status,
                 creation_date=None,
                 _id=None
                 ):
        self._id = str(uuid.uuid4()) if _id is None else _id
        self._title = title
        self._desc = desc
        self._priority = priority
        self._status = status
        self._creation_date = datetime.now().isoformat() if creation_date is None else creation_date
    @property
    def id(self):
        return self._id
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

    @classmethod
    def from_dict(cls, task_data):
        return cls(
            task_data["id"],
            task_data["title"],
            task_data["desc"],
            task_data["priority"],
            task_data["status"],
            task_data["creation_date"]
        )