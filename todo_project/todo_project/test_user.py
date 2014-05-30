# coding: utf-8

from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login, logout, authenticate
)
username='hails'
password='123123123'
authenticate(username=username,
                            password=password)
