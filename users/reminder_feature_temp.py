import datetime
import calendar


'''
Rough snippet for reminder feature.
To be implemented/moved in views.
'''


class Task:
    def __init__(self, task_name, task_duration=None, task_detail=None):
        self.__task_name = task_name
        self.__task_detail = task_detail
        self.__duration = datetime.timedelta(days=1) if task_duration is None else \
            datetime.timedelta(weeks=task_duration.weeks, days=task_duration.days, hours=task_duration.hours,
                               minutes=task_duration.minutes)
        self.__completed = False


class Tasks:
    def __init__(self):
        self.__tasks = []

    def add(self, task: Task):
        self.__tasks.append(task)       # sort input


class User:
    def __init__(self):
        self.__tasks = Tasks()

    def add_task(self):
        pass


def print_task_object(tasks):
    pass


def main():
    pass


if __name__ == "__main__":
    main()
