from flask import Flask, render_template,request, redirect, url_for
from pymata4 import pymata4
import time

#robotFlaskExample
app = Flask(__name__)

board = pymata4.Pymata4()
time.sleep(3)

board.set_pin_mode_servo(8)
board.servo_write(8, 87)
board.set_pin_mode_servo(9)
board.servo_write(9, 89)
board.set_pin_mode_analog_input(0)
board.set_pin_mode_analog_input(1)

@app.route('/', methods = ['POST','GET'])
def hello_world():
    if request.method == 'POST':

        if request.form['submit'] == 'leftForwards': 
            board.servo_write(8, 177)
        elif request.form['submit'] == 'leftStop': 
            board.servo_write(8, 87)
        elif request.form['submit'] == 'leftBackwards': 
            board.servo_write(8, 0)
            
        if request.form['submit'] == 'rightForwards': 
            board.servo_write(9, 0)
        elif request.form['submit'] == 'rightStop': 
            board.servo_write(9, 89)
        elif request.form['submit'] == 'rightBackwards': 
            board.servo_write(9, 179)
            
        else:
            pass

    return render_template('index.html', values = {'light':board.analog_read(1)[0], 'range':board.analog_read(0)[0], 'ultrasonic':0} )

if __name__ == "__main__":
    app.run(host='0.0.0.0')
