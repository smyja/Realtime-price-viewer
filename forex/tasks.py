import time
from celery import shared_task, task
from .scrapt import scrape

@task
def scrape_dev_to():
    
    scrape()
    return