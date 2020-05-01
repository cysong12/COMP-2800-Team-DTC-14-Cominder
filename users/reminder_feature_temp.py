import datetime
import calendar
from enum import Enum

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
    def __init__(self, first, last, birth_date, gender_enum, intolerance: list = None, **kwargs):
        self.__tasks = Tasks()
        self.__first_name = first
        self.__last_name = last
        self.__birth_date = birth_date
        self.__gender = gender_enum
        self.__middle_name = ''
        self.__food_intolerance = intolerance if intolerance is not None else []
        for key in kwargs:
            if key == "middle_name":
                self.__middle_name = kwargs[key]

    def get_tasks(self):
        return self.__tasks

    def get_full_name(self):
        return ' '.join([self.__first_name, self.__last_name])

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_birth_date(self):
        return self.__birth_date

    def get_gender(self):
        return self.__gender

    def get_food_intolerance(self):
        return self.__food_intolerance


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    APACHI_HELICOPTER = 4


def search_and_insert_sorted(tasks: Tasks, task: Task, size):
    i = size - 1
    tasks.get_tasks().append('')
    while i >= 0 and tasks.get_tasks()[i].get_date() > task.get_date():
        tasks.get_tasks()[i + 1] = tasks.get_tasks()[i]
        i -= 1
    tasks.get_tasks()[i + 1] = task


# test
def main():
    user = User('Choi', 'Song', datetime.datetime(1992, 12, 18), True, middle_name="Yong")
    task1 = Task('go biking', datetime.datetime(2020, 5, 1))
    task2 = Task('go play league', datetime.datetime(2020, 5, 3))
    task3 = Task('go scubadiving', datetime.datetime(2020, 5, 4))
    task4 = Task('go play hearthstone', datetime.datetime(2020, 5, 4))
    task5 = Task('go play tft', datetime.datetime(2020, 5, 4))
    task6 = Task('go hiking', datetime.datetime(2020, 5, 6))
    task7 = Task('go learn python', datetime.datetime(2020, 5, 9))
    user.get_tasks().add(task1)
    user.get_tasks().add(task2)
    user.get_tasks().add(task3)
    user.get_tasks().add(task4)
    user.get_tasks().add(task5)
    user.get_tasks().add(task6)
    user.get_tasks().add(task7)
    user_tasks = user.get_tasks()

    a_task = Task('go ham', datetime.datetime(2020, 5, 7))
    search_and_insert_sorted(user_tasks, a_task, user_tasks.size())
    user_tasks.debug_print()


if __name__ == "__main__":
    main()
