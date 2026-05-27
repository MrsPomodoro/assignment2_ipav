# test_transformation_parameters.py
# author: Barbara Klimek
# test_transformation_parameters.py
# author: Barbara Klimek

from src.transformation_parameters import (
    compute_rotation_angle,
    compute_scaling,
    compute_offset
)


#  rotation tests

# test 1: right -> up = +90 degrees
rot_A1 = [0, 0]
rot_B1 = [1, 0]

rot_A2 = [0, 0]
rot_B2 = [0, 1]


# test 2: right -> left = +180 degrees
rot_A1b = [0, 0]
rot_B1b = [1, 0]

rot_A2b = [0, 0]
rot_B2b = [-1, 0]


# test 3: right -> down = -90 degrees
rot_A1c = [0, 0]
rot_B1c = [1, 0]

rot_A2c = [0, 0]
rot_B2c = [0, -1]


# test 4: no rotation = 0 degrees
rot_A1d = [0, 0]
rot_B1d = [1, 0]

rot_A2d = [0, 0]
rot_B2d = [1, 0]


# test 5: 45 degrees rotation
rot_A1e = [0, 0]
rot_B1e = [1, 0]

rot_A2e = [0, 0]
rot_B2e = [1, 1]


#  scaling tests

# test 1: scaling factor = 2.0
scale_A1 = [0, 0]
scale_B1 = [1, 0]

scale_A2 = [0, 0]
scale_B2 = [2, 0]


# test 2: scaling factor = 0.5
scale_A1b = [0, 0]
scale_B1b = [2, 0]

scale_A2b = [0, 0]
scale_B2b = [1, 0]


# test 3: scaling factor = 3.0
scale_A1c = [0, 0]
scale_B1c = [1, 1]

scale_A2c = [0, 0]
scale_B2c = [3, 3]


# test 4: no scaling = 1.0
scale_A1d = [0, 0]
scale_B1d = [2, 2]

scale_A2d = [0, 0]
scale_B2d = [2, 2]


# test 5: scaling with vertical vectors = 4.0
scale_A1e = [0, 0]
scale_B1e = [0, 1]

scale_A2e = [0, 0]
scale_B2e = [0, 4]


#  offset test

# original vector
offset_A1 = [0, 0]
offset_B1 = [2, 0]

# translated by (+5, +3)
offset_A2 = [5, 3]
offset_B2 = [7, 3]

offset_rotation_angle = 0
offset_scale = 1


if __name__ == '__main__':

    print("---- ROTATION TESTS ----\n")

    angle = compute_rotation_angle(rot_A1, rot_B1, rot_A2, rot_B2)
    print(f"Test 1 result: {angle:.2f} degrees")
    print("Expected:      90.00 degrees\n")

    angle = compute_rotation_angle(rot_A1b, rot_B1b, rot_A2b, rot_B2b)
    print(f"Test 2 result: {angle:.2f} degrees")
    print("Expected:      180.00 degrees\n")

    angle = compute_rotation_angle(rot_A1c, rot_B1c, rot_A2c, rot_B2c)
    print(f"Test 3 result: {angle:.2f} degrees")
    print("Expected:      -90.00 degrees\n")

    angle = compute_rotation_angle(rot_A1d, rot_B1d, rot_A2d, rot_B2d)
    print(f"Test 4 result: {angle:.2f} degrees")
    print("Expected:      0.00 degrees\n")

    angle = compute_rotation_angle(rot_A1e, rot_B1e, rot_A2e, rot_B2e)
    print(f"Test 5 result: {angle:.2f} degrees")
    print("Expected:      45.00 degrees\n")


    print("---- SCALING TESTS ----\n")

    scale = compute_scaling(scale_A1, scale_B1, scale_A2, scale_B2)
    print(f"Test 1 result: {scale:.2f}")
    print("Expected:      2.00\n")

    scale = compute_scaling(scale_A1b, scale_B1b, scale_A2b, scale_B2b)
    print(f"Test 2 result: {scale:.2f}")
    print("Expected:      0.50\n")

    scale = compute_scaling(scale_A1c, scale_B1c, scale_A2c, scale_B2c)
    print(f"Test 3 result: {scale:.2f}")
    print("Expected:      3.00\n")

    scale = compute_scaling(scale_A1d, scale_B1d, scale_A2d, scale_B2d)
    print(f"Test 4 result: {scale:.2f}")
    print("Expected:      1.00\n")

    scale = compute_scaling(scale_A1e, scale_B1e, scale_A2e, scale_B2e)
    print(f"Test 5 result: {scale:.2f}")
    print("Expected:      4.00\n")


    print("---- OFFSET TEST ----\n")

    offset = compute_offset(
        offset_A1,
        offset_B1,
        offset_A2,
        offset_B2,
        offset_rotation_angle,
        offset_scale
    )

    print(f"Offset vector: {offset}")
    print("Expected:      [5. 3.]")