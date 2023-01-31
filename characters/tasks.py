# Create your tasks here

# from demoapp.models import Widget
from characters.scraper import sync_characters_with_api
from celery import shared_task


@shared_task
def run_sync_with_api() -> None:
    sync_characters_with_api()


# @shared_task
# def count_characters() -> int:
#     return Character.objects.count()


# @shared_task
# def add(x, y):
#     return x + y
#
#
# @shared_task
# def mul(x, y):
#     return x * y
#
#
# @shared_task
# def xsum(numbers):
#     return sum(numbers)
#
#
# @shared_task
# def count_widgets():
#     return Widget.objects.count()
#
#
# @shared_task
# def rename_widget(widget_id, name):
#     w = Widget.objects.get(id=widget_id)
#     w.name = name
#     w.save()
