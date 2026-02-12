from task import Task, Status
from storage import load_tasks, save_tasks

class TaskManager():
    def __init__(self, filepath):
        self._filepath = filepath
        self.tasks = []
        self.load()

    @property
    def filepath(self):
        return self._filepath

    def load(self):
        self.tasks = load_tasks(self.filepath)

    def save(self):
        save_tasks(self.filepath, self.tasks)

    def view_all(self):
        return self.tasks

    def add_task(self, title, desc, priority, status):
        task = Task(title, desc, priority, status)
        self.tasks.append(task)
        self.save()

    def delete_task(self, task_id):
        original_num = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save()
        return len(self.tasks) < original_num

    def mark_complete(self, task_id):
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task is None:
            return False
        task.status = Status.COMPLETED.value
        self.save()
        return True

    def filter_by_status(self, status):
        return [task for task in self.tasks if task.status == status]

    def filter_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def get_stats(self):
        return {
            "total": len(self.tasks),
            "completed": len([task for task in self.tasks if task.status == Status.COMPLETED.value]),
            "pending": len([task for task in self.tasks if task.status == Status.PENDING.value]),
            "in_progress": len([task for task in self.tasks if task.status == Status.IN_PROGRESS.value])
        }

    def search(self, keyword):
        keyword_lower = keyword.lower()
        return [
            task for task in self.tasks
            if keyword_lower in task.title.lower() or keyword_lower in task.desc.lower()
        ]