from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    
    def ready(self):
        import users.signals # Recommended to import this according to django documentation
