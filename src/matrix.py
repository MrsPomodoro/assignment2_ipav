
#################################
# TODO ASSIGNMENT PART 2:
#  1. Use the parameters to setup the transformation matrix that likely produced the transformed image in the first place.
#  2. Remember, it was a series of several transformations: translation, rotation around image center,
#  scaling relative to the image center.
#################################

# matrix.py
# author: Barbara Klimek
# This module handles:
# - computing affine matrix


import numpy as np

#forward affine transformation matrix.
def build_affine_matrix(rotation_angle, scale, offset, image_shape):

    phi = np.deg2rad(rotation_angle)       # convert angle from degrees to radians
    height, width = image_shape[:2]        # get image height and width

    # compute image center
    cx = width / 2
    cy = height / 2

    # translation to image center
    T1 = np.eye(3)
    T1[0,2] = -cx
    T1[1,2] = -cy

    # scaling matrix
    S = np.eye(3)
    S[0,0] = scale
    S[1,1] = scale

    # rotation matrix
    R = np.eye(3)
    R[0,0] = np.cos(phi)
    R[0,1] = -np.sin(phi)
    R[1,0] = np.sin(phi)
    R[1,1] = np.cos(phi)

    # translation back from image center
    T2 = np.eye(3)
    T2[0,2] = cx
    T2[1,2] = cy

    # translation offset matrix
    Toffset = np.eye(3)
    Toffset[0,2] = offset[0]
    Toffset[1,2] = offset[1]

    # final affine transformation matrix
    #M = Toffset @ T2 @ R @ S @ T1
    M = T2 @ R @ S @ T1 @ Toffset

    print(M)
    return M
