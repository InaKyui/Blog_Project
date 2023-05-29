#-*- encoding: utf-8 -*-
#!/usr/bin/blog_venv python3.7
"""
[File]        : index.py
[Time]        : 2023/05/27 18:00:00
[Author]      : InaKyui
[License]     : (C)Copyright 2023, InaKyui
[Version]     : 1.0
[Description] : Blueprint index.
"""

__authors__ = ["InaKyui <https://github.com/InaKyui>"]
__version__ = "Version: 1.0"

from flask import Blueprint, render_template

bp = Blueprint(name="index", import_name=__name__,  url_prefix="/")

@bp.route("/")
def homepage():
    return render_template("homepage.html")