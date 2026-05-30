
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
def compute_offset(A1, B1, A2, B2, rotation_angle, scale, image_shape):

    # half-point of A1-B1 from assignment description
    HP1 = (np.array(A1) + np.array(B1)) / 2

    height, width = image_shape[:2]       # image center

    T = np.eye(3)                          # translation matrix based on Example09
    T[0, 2] = -width * 0.5
    T[1, 2] = -height * 0.5

    phi = np.deg2rad(-rotation_angle)      # rotation matrix based on Example09

    R = np.eye(3)
    R[0, 0] = np.cos(phi)
    R[0, 1] = -np.sin(phi)
    R[1, 0] = np.sin(phi)
    R[1, 1] = np.cos(phi)

    S = np.eye(3)                             # scaling matrix

    S[0, 0] = 1 / scale
    S[1, 1] = 1 / scale

    # inverse transform around image center
    M = np.linalg.inv(T) @ R @ S @ T

    # homogeneous coordinates
    A2_h = np.array([A2[0], A2[1], 1])
    B2_h = np.array([B2[0], B2[1], 1])

    # transform points
    A3_h = M @ A2_h
    B3_h = M @ B2_h

    A3 = A3_h[:2]
    B3 = B3_h[:2]

    # half-point of A3-B3 from assignment description
    HP2 = (A3 + B3) / 2

    # offset vector from assignment description
    offset = HP2 - HP1

    # debug logs
    print("HP1 =", HP1)
    print("HP2 =", HP2)
    print("offset =", offset)
    print("HP2 - HP1 =", HP2 - HP1)
    print("A3 =", A3)
    print("B3 =", B3)

    return offset