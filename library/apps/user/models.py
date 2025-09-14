from django.db import models
# models.py
from django.conf import settings   # para usar settings.AUTH_USER_MODEL
# ou em runtime:
from django.contrib.auth import get_user_model

Users = get_user_model()





