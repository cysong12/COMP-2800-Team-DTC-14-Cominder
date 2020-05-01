import datetime
import calendar


'''
Rough snippet for reminder feature.
To be implemented/moved in views.
'''


class Task:
    def __init__(self, task_name: str, date: datetime.datetime, task_duration: datetime.datetime = None,
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

    def debug_print(self):
        counter = 1
        for task in self.__tasks:
            print(f"{counter}: {task.get_name()} {task.get_date()}")
            counter += 1


class User:
    def __init__(self):
        self.tasks = Tasks()


def search_and_insert_sorted(tasks: Tasks, task: Task, size):
    i = size - 1
    tasks.get_tasks().append('')
    while i >= 0 and tasks.get_tasks()[i].get_date() > task.get_date():
        tasks.get_tasks()[i + 1] = tasks.get_tasks()[i]
        i -= 1
    tasks.get_tasks()[i + 1] = task


# test
def main():
    user = User()
    task1 = Task('go biking', datetime.datetime(2020, 5, 1))
    task2 = Task('go play league', datetime.datetime(2020, 5, 3))
    task3 = Task('go scubadiving', datetime.datetime(2020, 5, 4))
    task4 = Task('go play hearthstone', datetime.datetime(2020, 5, 4))
    task5 = Task('go play tft', datetime.datetime(2020, 5, 4))
    task6 = Task('go hiking', datetime.datetime(2020, 5, 6))
    task7 = Task('go learn python', datetime.datetime(2020, 5, 9))
    user.tasks.add(task1)
    user.tasks.add(task2)
    user.tasks.add(task3)
    user.tasks.add(task4)
    user.tasks.add(task5)
    user.tasks.add(task6)
    user.tasks.add(task7)
    user_tasks = user.tasks

    a_task = Task('go ham', datetime.datetime(2020, 5, 7))
    search_and_insert_sorted(user_tasks, a_task, user_tasks.size())
    user_tasks.debug_print()


if __name__ == "__main__":
    main()
