#-*- encoding: utf-8 -*-
#!/usr/bin/blog_venv python3.7
"""
[File]        : extends.py
[Time]        : 2023/05/27 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 1.0
[Description] : Basic Class.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

from flask_mail import Mail
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mail = Mail()
cache = Cache()