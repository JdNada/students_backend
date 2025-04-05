# gunicorn_config.py
workers = 4  # Nombre de workers (généralement 2-4 par cœur CPU)
worker_class = "uvicorn.workers.UvicornWorker"  # Utiliser Uvicorn comme worker
bind = "0.0.0.0:8000"  # Adresse et port d'écoute