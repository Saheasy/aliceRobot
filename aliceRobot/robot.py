from flask import Blueprint, render_template, request, flash
from pymata4 import pymata4
import time

robot = Blueprint('robot', __name__)
board = None
robot_pins = {
    'servo_left': 8,
    'servo_right': 9,
    'ultrasonic': 
    'range': 0,
    'light': 1,
    'relay': 22
}
robot_data = {
        'servo_left': 87,
        'servo_right': 89,
        'ultrasonic': 7,6
        'range': 0,
        'light': 0,
        'relay': 0
    }
    
@robot.route('/', methods = ['POST','GET'])
def home():
    global board
    if request.method == 'POST':
        if request.form['submit'] == 'setup': 
            try: 
                board = pymata4.Pymata4()
                time.sleep(3)

                board.set_pin_mode_servo(robot_pins['servo_left'])
                board.servo_write(robot_pins['servo_left'], 87)
                board.set_pin_mode_servo(robot_pins['servo_right'])
                board.servo_write(robot_pins['servo_right'], 89)
                board.set_pin_mode_analog_input(robot_pins['range'])
                board.set_pin_mode_analog_input(robot_pins['light'])
                board.set_pin_mode_digital_output(robot_pins['relay'])
                board.set_pin_mode_sonar(robot_pins['ultrasonic'][0], robot_pins['ultrasonic'][1])
                
            except:
                flash('Already Set up', category='error')
        
        if request.form['submit'] == 'leftForwards': 
            robot_data['servo_left'] = 177
        elif request.form['submit'] == 'leftStop':
            robot_data['servo_left'] = 87
        elif request.form['submit'] == 'leftBackwards':
            robot_data['servo_left'] = 0
            
        if request.form['submit'] == 'rightForwards': 
            robot_data['servo_right'] = 0
        elif request.form['submit'] == 'rightStop': 
            robot_data['servo_right'] = 89
        elif request.form['submit'] == 'rightBackwards': 
            robot_data['servo_right'] = 179
        
        if request.form['submit'] == 'onRelay': 
            robot_data['relay'] = 1
        elif request.form['submit'] == 'offRelay': 
            robot_data['relay'] = 0
        
        if request.form['submit'] == 'updateSensory':
            pass
        
        if board != None:
            board.servo_write(robot_pins['servo_left'], robot_data['servo_left'] )
            board.servo_write(robot_pins['servo_right'], robot_data['servo_right'] )
            board.digital_write(robot_pins['relay'], robot_data['relay'])
            robot_data['range'] = board.analog_read(robot_pins['range'])[0]
            robot_data['light'] = board.analog_read(robot_pins['light'])[0]
            robot_data['ultrasonic'] = board.sonar_read(robot_pins['ultrasonic'][0])[0]
        else:
            flash('Board not initiated', category='error')
    
    return render_template('index.html', values = robot_data )
    
    