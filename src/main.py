# This is a main  script.


import cv2
import numpy as np
import matplotlib.pyplot as plt


from transformation_parameters import (
    compute_rotation_angle,
    compute_scaling,
    compute_offset
)

from matrix import(
build_affine_matrix
)

# TODO ASSIGMENT MAIN: The provided images T1.jpg and T1_transformed.jpg represent the original and a transformed image.
#  Your job is to obtain the transformation parameters (and thus, the transformation matrix) that was used to
#  transform the original image to produce the transformed image.
#  The transformation used was a combination of a translation with a certain x- and y-offset, rotating around the image
#  center, and a scaling operation relative to the image center (using a single scaling factor for both x- and y-axis).

# load original and transformed images based on example from example09 code
original_image = cv2.imread('data/T1.jpg', cv2.IMREAD_UNCHANGED)
transformed_image = cv2.imread('data/T1_transformed.jpg', cv2.IMREAD_UNCHANGED)

# BGR -> RGB conversion based on example from example09 code
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
transformed_image = cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB)

# manually selected corresponding points
A1 = [235, 45]; A2 = [125, 95]
B1 = [275, 335]; B2 = [370, 225]

#TODO:Use the parameters to setup the transformation matrix that likely produced the transformed image in the first place.
# - Remember, it was a series of several transformations: translation, rotation around image center, scaling relative to the image center.
# - Use it now to undo the transformation of the transformed image, by applying the inverse of the affine transformation
# and doing backward mapping for image transformation.
# - You can use OpenCV functionality for the warping similar to how we did it in the lectures, given that you have an
# affine transformation matrix as numpy array M of size 3x3, you could use this function: img_result = cv2.warpAffine(img, M[0:2,0:3], img.shape[1::-1], flags=cv2.INTER_LINEAR)
# - In other words: there is no obligation to use the backward-mapping function from the lectures.
# - This step basically resembles a semi-automatic registration procedure with manual landmark selection (so if done right the new image should look similar to the original image/the newly created image should be registered to the original image).


if __name__ == '__main__':
# 1. Compute transformation parameters: calculate the rotation, scale and offset for the
    rotation_angle = compute_rotation_angle(A1, B1, A2, B2)
    scale = compute_scaling(A1, B1, A2, B2)
    offset = compute_offset( A1,B1,A2,B2, rotation_angle, scale, original_image.shape)

# debug logs
    print(f"Rotation angle: {rotation_angle:.2f} degrees")
    print(f"Scaling factor: {scale:.2f}")
    print(f"Offset vector: {offset}")

# 2. Build affine transformation matrixes

#forward affine transformation matrix.
    M = build_affine_matrix( rotation_angle, scale, offset, transformed_image.shape)
    M_inv = np.linalg.inv(M)

# Verify affine transformation - debug logs
    A1_h = np.array([A1[0], A1[1], 1])
    B1_h = np.array([B1[0], B1[1], 1])
    A2_h = np.array([A2[0], A2[1], 1])
    B2_h = np.array([B2[0], B2[1], 1])

    print(f"M(A1) = {M @ A1_h}, A2 = {A2}")
    print(f"M(B1) = {M @ B1_h}, B2 = {B2}")
    print(f"M_inv(A2) = {M_inv @ A2_h}, A1 = {A1}")
    print(f"M_inv(B2) = {M_inv @ B2_h}, B1 = {B1}")

    HP1_h = np.array([255, 190, 1])

    print("M(HP1) =", M @ HP1_h)
    print("HP transformed =", (np.array(A2) + np.array(B2)) / 2)


#3. applied the function from assignment's description img_result = cv2.warpAffine(img, M[0:2,0:3], img.shape[1::-1], flags=cv2.INTER_LINEAR)
    img_result = cv2.warpAffine(
        transformed_image,
        M_inv[0:2, 0:3],
        transformed_image.shape[1::-1],
        flags=cv2.INTER_LINEAR
    )
#4. difference = original - registered, in assigmnet tells (you need to think of a suited datatype here)
    img_difference = np.abs(
            original_image.astype(np.float32)
            - img_result.astype(np.float32)
        )

#4. Visualize registration result
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(original_image)
    plt.title("Original")

    plt.subplot(1, 4, 2)
    plt.imshow(transformed_image)
    plt.title("Transformed")

    plt.subplot(1, 4, 3)
    plt.imshow(img_result)
    plt.title("Computed Result")

    plt.subplot(1, 4, 4)
    plt.imshow(img_difference.astype(np.uint8))
    plt.title("Difference Image")

    plt.show()

