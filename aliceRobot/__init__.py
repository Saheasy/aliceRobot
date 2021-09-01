from flask import Flask, render_template,request, redirect, url_for
#robotFlaskExample
def run_robot():
    app = Flask(__name__)
    from .robot import robot
    app.register_blueprint(robot, url_prefix='/')
    return app

