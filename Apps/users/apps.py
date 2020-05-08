from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'Apps.users'
    
    def ready(self):
        import users.signals
