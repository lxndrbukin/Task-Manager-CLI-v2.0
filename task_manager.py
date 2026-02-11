from task import Task
from storage import load_tasks, save_tasks

class TaskManager():
    def __init__(self, filepath):
        self._filepath = filepath
        self.tasks = []
        self.load()

    @property
    def filepath(self):
        return self._filepath

    def add_task(self, title, desc, priority, status):
        task = Task(title, desc, priority, status)
        self.tasks.append(task)
        self.save()

    def load(self):
        self.tasks = load_tasks(self.filepath)

    def save(self):
        save_tasks(self.filepath, self.tasks)

    def view_all(self):
        return self.tasks

    def delete_task(self, task_id):
        original_num = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        self.save()
        return len(self.tasks) < original_num