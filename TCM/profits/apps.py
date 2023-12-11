from django.apps import AppConfig

class ProfitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profits'

    def ready(self):
        import profits.signals