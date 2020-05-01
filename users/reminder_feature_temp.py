import datetime
import calendar


'''
Rough snippet for reminder feature.
To be implemented/moved in views.
'''


class Task:
    def __init__(self, task_name: str, date: datetime.datetime = None, task_duration: datetime.datetime = None,
                 task_detail: str = None, task_reward_point: int = None):
        self.__name = task_name
        self.__date = date     # datetime obj; date assigned (task starting date)
        self.__detail = '' if task_detail is None else task_detail        # user memo
        self.__duration = datetime.timedelta(days=1) if task_duration is None else \
            datetime.timedelta(weeks=task_duration.weeks, days=task_duration.days, hours=task_duration.hours,
                               minutes=task_duration.minutes)
        self.__completed = False
        self.__task_reward_point = task_reward_point if None else 1

    def get_name(self):
        return self.__name

    def get_date(self):
        return self.__date

    def get_detail(self):
        return self.__detail

    def get_duration(self):
        return self.__duration

    def is_completed(self):
        return self.__completed

    def get_point_weight(self):
        return self.__task_reward_point


class Tasks:
    def __init__(self):
        self.__tasks = []

    def add(self, task: Task):
        self.__tasks.append(task)       # sort input

    def remove(self, task: Task):
        self.__tasks.remove(task.get_name())

    def clear(self):
        self.__tasks = []

    def size(self):
        return len(self.__tasks)

    def get_tasks(self):
        return self.__tasks


class User:
    def __init__(self):
        self.tasks = Tasks()


# test
def main():
    user = User()
    task1 = Task('go biking')
    user.tasks.add(task1)
    user_tasks = user.tasks.get_tasks()
    print(user_tasks[0].get_name())


if __name__ == "__main__":
    main()
