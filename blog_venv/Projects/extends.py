#-*- encoding: utf-8 -*-
#!/usr/bin/pixiv_venv python3.7
"""
[File]      : exts.py
[Time]      : 2023/05/22 15:03:39
[Author]    : InaKyui
[License]   : (C)Copyright 2022, InaKyui
[Version]   : 1.0
[Description] : Description.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

from flask_mail import Mail
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
cache = Cache()