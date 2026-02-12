from datetime import datetime
from enum import Enum

class Priority(Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class Status(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in progress"
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
        self._id = _id
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
    @priority.setter
    def priority(self, new_priority):
        try:
            valid_priority = Priority(new_priority)
            self._priority = valid_priority.value
        except ValueError:
            raise ValueError(f"{new_priority} is not valid: {[p.value for p in Priority]}")
    @property
    def status(self) -> str:
        return self._status
    @status.setter
    def status(self, new_status):
        try:
            valid_status = Status(new_status)
            self._status = valid_status.value
        except ValueError:
            raise ValueError(f"{new_status} is not valid: {[s.value for s in Status]}")
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
            title=task_data["title"],
            desc=task_data["desc"],
            priority=task_data["priority"],
            status=task_data["status"],
            creation_date=task_data["creation_date"],
            _id=task_data["id"]
        )