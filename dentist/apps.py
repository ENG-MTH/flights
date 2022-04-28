from django.apps import AppConfig


class DentistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dentist'

    class FlightsConfig(AppConfig):
        default_auto_field = 'django.db.models.BigAutoField'
        name = 'flights'

