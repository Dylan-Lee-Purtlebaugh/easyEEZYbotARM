# Import EEZYbotARM library
from easyEEZYbotARM.kinematic_model import EEZYbotARM_Mk2

# Initialise robot arm with initial joint angles
myRobotArm = EEZYbotARM_Mk2(initial_q1=0, initial_q2=70, initial_q3=-100)
myRobotArm.plot()  # plot it

#                       injection
#_____________________________________________________________________


def get_xyz_input():
    try:
        raw_input = input("Enter coordinates as X,Y,Z (mm): ")
        x_str, y_str, z_str = raw_input.strip().split(',')
        x, y, z = float(x_str), float(y_str), float(z_str)
        return x, y, z
    except ValueError:
        print("Invalid input. Please enter three numbers separated by commas.")
        return None





#___________________________________________________________________

# Assign cartesian position where we want the robot arm end effector to move to
# (x,y,z in mm from centre of robot base)
x = 0  # mm
y = 0  # mm
z = 13  # mm

# Compute inverse kinematics
a1, a2, a3 = myRobotArm.inverseKinematics(x, y, z)

# Print the result
print('To move the end effector to the cartesian position (mm) x={}, y={}, z={}, the robot arm joint angles (degrees)  are q1 = {}, q2= {}, q3 = {}'.format(x, y, z, a1, a2, a3))

# Visualise the new joint angles
myRobotArm.updateJointAngles(q1=a1, q2=a2, q3=a3)
myRobotArm.plot()
