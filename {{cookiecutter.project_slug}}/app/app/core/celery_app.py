from celery import Celery

celery_app = Celery("worker", broker="redis://app_redis:6379")

celery_app.conf.task_routes = {"app.worker.test_celery": "main-queue"}
