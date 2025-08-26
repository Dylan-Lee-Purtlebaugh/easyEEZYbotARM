# Import EEZYbotARM library
from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk2

# Initialise robot arm with initial joint angles
myRobotArm = EEZYbotARM_Mk2(initial_q1=0, initial_q2=70, initial_q3=-100)
myRobotArm.plot()  # plot it

#_____________________________________________________________________

def get_xyz_input():
    raw_input = input("Enter coordinates as X,Y,Z (mm) or type 'exit': ")
    if raw_input.lower() == 'exit':
        return 'exit'
    try:
        x_str, y_str, z_str = raw_input.strip().split(',')
        x, y, z = float(x_str), float(y_str), float(z_str)
        return x, y, z
    except ValueError:
        print("Invalid input. Please enter three numbers separated by commas.")
        return None

def move_to_xyz(x, y, z):
    try:
        a1, a2, a3 = myRobotArm.inverseKinematics(x, y, z)
        print(f"Moving to ({x}, {y}, {z}) → q1={a1:.2f}, q2={a2:.2f}, q3={a3:.2f}")
        myRobotArm.updateJointAngles(q1=a1, q2=a2, q3=a3)
        myRobotArm.plot()
    except Exception as e:
        print(f"IK failed: {e}")

#_____________________________________________________________________

while True:
    coords = get_xyz_input()
    if coords == 'exit':
        print("Exiting control loop.")
        break
    elif coords:
        x, y, z = coords
        move_to_xyz(x, y, z)
