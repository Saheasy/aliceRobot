from flask import Flask, render_template,request, redirect, url_for
from pymata4 import pymata4
import time

#robotFlaskExample
def run_robot():
    global board
    app = Flask(__name__)
    from .robot import robot
    app.register_blueprint(robot, url_prefix='/')
    return app

