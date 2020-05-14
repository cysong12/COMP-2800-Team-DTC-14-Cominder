"""
WIP file to  be added to views.py

Also set a blackout period so the user is not notified at night time.  Default blackout period is 0:00-8:00.

notify_func is just a placeholder.
"""
import datetime


class BlackoutDecorator(object):
    def __init__(self, arg1, arg2, arg3):
        self.start_blackout = arg1
        self.end_blackout = arg2
        self.current_time = arg3

    def __call__(self, func):

        def wrapper(*args):
            if self.start_blackout <= self.current_time <= self.end_blackout:
                pass
            else:
                func()
        return wrapper


def main():
    current_time = int(datetime.datetime.now().strftime("%H"))
    start_blackout = 0
    end_blackout = 8

    @BlackoutDecorator(start_blackout, end_blackout, current_time)
    def notify_func():  # once notifications are implemented, delete this.
        print("hello")

    notify_func()   # import notification code here.  Alternatively, import this module into the notification feature.


if __name__ == "__main__":
    main()
