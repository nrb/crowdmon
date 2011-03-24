from flask import Module, url_for, redirect, g, flash, request, current_app, render_template

frontend = Module(__name__)

@frontend.route("/")
def index():
    return "Hello!"
