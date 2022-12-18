import sqlite3
from app import app
from flask import render_template, url_for, request, flash, redirect

def get_db_conn():
    conn = sqlite3.connect(r"C:\Python_Script\blog_venv\Projects\database.db")
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
@app.route("/index")
def index():
    user = { "username": "InaKyui" }
    return render_template("index.html", title="InaKyui - Blog", user=user)

@app.route("/contents")
def contents():
    conn = get_db_conn()
    contents = conn.execute("SELECT * FROM contents").fetchall()
    for c in contents:
        print(c["id"])
    return render_template("contents.html", title="contents", contents=contents)

def get_content(content_id):
    conn = get_db_conn()
    content = conn.execute("SELECT * FROM contents where id = ?", (content_id,)).fetchone()
    return content

@app.route("/contents/<int:content_id>")
def content(content_id):
    content = get_content(content_id)
    return render_template("content.html", content=content)

@app.route("/contents/new", methods=("GET", "POST"))
def add_content():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title:
            flash("NULL")
        elif not content:
            flash("NULL")
        else:
            conn = get_db_conn()
            conn.execute("INSERT INTO contents (title, content) VALUES ('{}', '{}')".format(title, content))
            conn.commit()
            conn.close()
            flash("success")
            return redirect(url_for("contents"))
    return render_template("new.html")

@app.route("/contents/<int:content_id>/edit", methods=("GET", "POST"))
def edit_content(content_id):
    content = get_content(content_id)

    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        if not title:
            flash("NULL")
        elif not content:
            flash("NULL")
        else:
            conn = get_db_conn()
            conn.execute("UPDATE contents SET title = {}, content = {} WHERE id = {}".format(title, content, content_id))
            conn.commit()
            conn.close()
            flash("success")
            return redirect(url_for("contents"))
    return render_template("edit.html", content=content)

@app.route("/contents/<int:content_id>/delete", methods=("POST",))
def delete_content(content_id):
    content = get_content(content_id)
    conn = get_db_conn()
    conn.execute("DELETE FROM contents where id = {}".format(content_id))
    conn.commit()
    conn.close()
    flash("delete")
    return redirect(url_for("contents"))