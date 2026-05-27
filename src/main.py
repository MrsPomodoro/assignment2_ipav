# This is a main  script.


import cv2
import numpy as np
import matplotlib.pyplot as plt


from transformation_parameters import (
    compute_rotation_angle,
    compute_scaling,
    compute_offset
)

# TODO: The provided images T1.jpg and T1_transformed.jpg represent the original and a transformed image.
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




if __name__ == '__main__':
    # plot both images into one figure
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original_image)
    plt.title('Original image')

    plt.subplot(1, 2, 2)
    plt.imshow(transformed_image)
    plt.title('Transformed image')

    plt.show()