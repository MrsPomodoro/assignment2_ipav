
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
# - computing rotation angle
# - computing scaling factor
# - computing x- and y-offsets via the half-point method
# - building the final 3x3 affine transformation matrix



import numpy as np


# 1. Compute the rotation angle between vector A1->B1 (original image) and vector A2->B2 (transformed image).
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

## 2. To obtain the scaling one can determine the length ratio of these 2 vectors.
def compute_scaling(A1, B1, A2, B2):
    v1 = np.array(B1) - np.array(A1)       # vector from A1 to B1 in original image
    v2 = np.array(B2) - np.array(A2)       # vector from A2 to B2 in transformed image

    len_v1 = np.linalg.norm(v1)
    len_v2 = np.linalg.norm(v2)

    scale = len_v2 / len_v1
    return scale

# 3. To obtain the x- and y-offsets
def compute_offset(A1, B1, A2, B2, rotation_angle, scale):
    #  compute the half-point of the line segment from A1 to B1 (let’s denote it with HP1)
    HP1 = (np.array(A1) + np.array(B1)) / 2


    # - transform points A2 and B2 with the inverse transformation of the rotation
    A2_scaled = np.array(A2) / scale
    B2_scaled = np.array(B2) / scale

    phi = np.deg2rad(-rotation_angle)     # convert angle from degrees to radians

    R = np.eye(2)       # helper inverse rotation matrix from lecture/example09

    R[0, 0] = np.cos(phi)
    R[0, 1] = -np.sin(phi)

    R[1, 0] = np.sin(phi)
    R[1, 1] = np.cos(phi)

    #     # and scaling with the parameters obtained in 1. And 2. (let’s denote these transformed points A3 and B3)
    #     transform point A2 AND B2 with inverse rotation
    A3 = R @ A2_scaled
    B3 = R @ B2_scaled

    # - compute the half point on the line segment A3-B3 (let’s denote it with HP2).
    HP2 = (A3 + B3) / 2

    # define a vector pointing from HP1 to HP2.
    offset = HP2 - HP1

    return offset