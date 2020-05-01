import datetime
import calendar
from enum import Enum

'''
Rough snippet for reminder feature.
To be implemented/moved in views.py
'''


class Task:
    def __init__(self, task_name: str, date: datetime.datetime, task_duration: datetime.timedelta = None,
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
        # search_and_insert_task_sorted(self.__tasks, task, self.size())
        add_to_sorted_tasks(self.__tasks, task)

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


# initialized whenever user logs in
class User:
    def __init__(self, first: str, last: str, birth_date: datetime.datetime, gender_enum, intolerance: list = None, food_preferences: list = None, **kwargs):
        self.__tasks = Tasks()
        self.__first_name = first
        self.__last_name = last
        self.__birth_date = birth_date
        self.__gender = gender_enum
        self.__middle_name = ''
        self.__food_intolerance = intolerance if intolerance is not None else []
        self.__food_preferences = food_preferences if food_preferences is not None else []
        for key in kwargs:
            if key == "middle_name":
                self.__middle_name = kwargs[key]

    def get_tasks(self):
        return self.__tasks

    def get_full_name(self):
        if self.__middle_name:
            return ' '.join([self.__first_name, self.__last_name])
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

    def set_food_intolerance(self, intolerance: list):
        self.__food_intolerance = intolerance

    def add_food_intolerance(self, *args):
        for food in args:
            self.__food_intolerance.append(food)

    def set_food_preference(self, preferences: list):
        self.__food_preferences = preferences

    def add_food_preference(self, *args):
        for food in args:
            self.__food_preferences.append(food)


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3
    APACHE_HELICOPTER = 4


def search_and_insert_task_sorted(tasks: list, task: Task, size):
    i = size - 1
    tasks.append('')
    while i >= 0 and tasks[i].get_date() > task.get_date():
        tasks[i + 1] = tasks[i]
        i -= 1
    tasks[i + 1] = task


def search_find_index(tasks: list, task: Task, start, end):
    if end - start + 1 <= 0:
        return start
    else:
        mid = start + (end - start) // 2
        if tasks[mid].get_date() == task.get_date():
            return mid
        else:
            if task.get_date() < tasks[mid].get_date():
                return search_find_index(tasks, task, start, mid - 1)
            else:
                return search_find_index(tasks, task, mid + 1, end)


def add_to_sorted_tasks(tasks: list, task: Task):
    index = search_find_index(tasks, task, 0, len(tasks) - 1)
    tasks.insert(index, task)


# test
def main():
    user = User('Choi', 'Song', datetime.datetime(1992, 12, 18), True, middle_name="Yong")
    task1 = Task('go biking', datetime.datetime(2020, 5, 5))
    task2 = Task('go play league', datetime.datetime(2020, 5, 2))
    task3 = Task('go scubadiving', datetime.datetime(2020, 5, 4, 16))
    task4 = Task('go play hearthstone', datetime.datetime(2020, 5, 4, 12))
    task5 = Task('go play tft', datetime.datetime(2020, 5, 4, 1))
    task6 = Task('go hiking', datetime.datetime(2020, 5, 3))
    task7 = Task('go learn python', datetime.datetime(2020, 5, 9))
    user_tasks = user.get_tasks()
    user_tasks.add(task1)
    user_tasks.add(task2)
    user_tasks.add(task3)
    user_tasks.add(task4)
    user_tasks.add(task5)
    user_tasks.add(task6)
    user_tasks.add(task7)

    a_task = Task('go ham', datetime.datetime(2020, 5, 7))
    user_tasks.add(a_task)
    user_tasks.debug_print()


if __name__ == "__main__":
    main()
