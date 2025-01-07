import logging
from celery import shared_task

logger = logging.getLogger(__name__)
logging.basicConfig(filename='celery.log', encoding='utf-8', level=logging.DEBUG)

@shared_task
def log_message(msg: str):
    print("Message recieved")
    print(msg)
