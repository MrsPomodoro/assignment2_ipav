# This is a main  script.

import numpy as np
import cv2
import matplotlib.pyplot as plt

from transformation_parameters import compute_rotation_angle

# ---- test cases for transformation methods ----

# test 1: right -> up = +90 degrees
A1 = [0, 0]; B1 = [1, 0]
A2 = [0, 0]; B2 = [0, 1]

# test 2: right -> left = +180 degrees
A1b = [0, 0]; B1b = [1, 0]
A2b = [0, 0]; B2b = [-1, 0]

# test 3: right -> down = -90 degrees
A1c = [0, 0]; B1c = [1, 0]
A2c = [0, 0]; B2c = [0, -1]

# test 4: no rotation = 0 degrees
A1d = [0, 0]; B1d = [1, 0]
A2d = [0, 0]; B2d = [1, 0]

# test 5: 45 degrees rotation
A1e = [0, 0]; B1e = [1, 0]
A2e = [0, 0]; B2e = [1, 1]



if __name__ == '__main__':
    angle = compute_rotation_angle(A1, B1, A2, B2)
    print(f"Rotation angle: {angle:.2f} degrees")
    print(f"Expected:       90.00 degrees\n")

    angle = compute_rotation_angle(A1b, B1b, A2b, B2b)
    print(f"Rotation angle: {angle:.2f} degrees")
    print(f"Expected:       180.00 degrees\n")

    angle = compute_rotation_angle(A1c, B1c, A2c, B2c)
    print(f"Rotation angle: {angle:.2f} degrees")
    print(f"Expected:       -90.00 degrees\n")

    angle = compute_rotation_angle(A1d, B1d, A2d, B2d)
    print(f"Rotation angle: {angle:.2f} degrees")
    print(f"Expected:       0.00 degrees\n")

    angle = compute_rotation_angle(A1e, B1e, A2e, B2e)
    print(f"Rotation angle: {angle:.2f} degrees")
    print(f"Expected:       45.00 degrees\n")