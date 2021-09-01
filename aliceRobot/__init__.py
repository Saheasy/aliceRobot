from flask import Flask, render_template,request, redirect, url_for
import secrets
#robotFlaskExample
def run_robot():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secrets.token_urlsafe(10)
    from .robot import robot
    app.register_blueprint(robot, url_prefix='/')
    return app

