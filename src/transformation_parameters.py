
#################################
# TODO ASSIGNMENT PART 1:
# 1. To obtain the rotation angle one can use the equation for the angle between 2 vectors (the 2 vectors being the vector
#    from A1 to B1 and the vector from A2 to B2).
# 2. To obtain the scaling one can determine the length ratio of these 2 vectors.
# 3. To obtain the x- and y-offsets one needs to, e.g.:
#       - compute the half-point of the line segment from A1 to B1 (let’s denote it with HP1)
#       - transform points A2 and B2 with the inverse transformation of the rotation and scaling with the parameters
#         obtained in 1. And 2. (let’s denote these transformed points A3 and B3)
#       - compute the half point on the line segment A3-B3 (let’s denote it with HP2).
#       - define a vector pointing from HP1 to HP2. If you computed everything correctly, this vector resembles the offset vector
#################################

# transformation_parameters.py
# author: Barbara Klimek
# This module handles:
# - computing rotation angle from landmark pairs
# - computing scaling factor from landmark pairs
# - computing x- and y-offsets via the half-point method
# - building the final 3x3 affine transformation matrix



import numpy as np


# Compute the rotation angle between vector A1->B1 (original image) and vector A2->B2 (transformed image).
def compute_rotation_angle(A1, B1, A2, B2):

    v1 = np.array(B1) - np.array(A1)               # vector from A1 to B1 in original image
    v2 = np.array(B2) - np.array(A2)               # vector from A2 to B2 in transformed image

    # angle of each vector using arctan2
    angle_v1 = np.arctan2(v1[1], v1[0])
    angle_v2 = np.arctan2(v2[1], v2[0])

    # rotation angle = difference between the two angles
    angle_rad = angle_v2 - angle_v1
    angle_deg = np.rad2deg(angle_rad)

    return angle_deg