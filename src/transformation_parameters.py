
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