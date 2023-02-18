from django.apps import AppConfig


class ArticleConfig(AppConfig):
    """this config registers article app in django admin"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "article"

    # after create receiver in signals.py
    def ready(self):
        import article.signals
