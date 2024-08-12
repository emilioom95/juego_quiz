from django.apps import AppConfig

class JuegoConfig(AppConfig):
    name = 'juego'

    def ready(self):
        import juego.signals