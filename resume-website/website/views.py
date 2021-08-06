# This file houses the different web views accessible from the main host domain.

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask.helpers import flash
from .models import Post
from . import db
import datetime

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    posts = Post.query.all()
    return render_template("home.html")

@views.route("/about")
def about():
    return render_template("about.html", now = datetime.datetime.utcnow() + datetime.timedelta(seconds=9 * 3600))

@views.route("/contact")
def contact():
    return render_template("contact.html", now = datetime.datetime.utcnow() + datetime.timedelta(seconds=9 * 3600))