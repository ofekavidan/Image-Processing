import cv2
import numpy as np

# used a code from:
# https://stackoverflow.com/questions/52495105/wrong-colors-in-result-pyramid-blending-using-opencv-and-python
# Function to create a hybrid image
# IMPORTANT MARK!!! I assumed that the pictures in the same size
def hybrid(first_img_path, sec_img_path):
    # Read the first image in grayscale
    image_low = cv2.imread(first_img_path, cv2.IMREAD_GRAYSCALE)

    # Read the second image in grayscale
    image_high_orig = cv2.imread(sec_img_path, cv2.IMREAD_GRAYSCALE)

    # Define the kernel size for Gaussian blur
    kernel_size = 67

    # Apply Gaussian blur to the first image
    image_low = cv2.GaussianBlur(image_low, (kernel_size, kernel_size), 0)

    # Apply Gaussian blur to the second image
    image_high = cv2.GaussianBlur(image_high_orig, (kernel_size, kernel_size), 0)

    # Apply high-pass filter to the second image
    image_high = cv2.subtract(image_high_orig, image_high)

    # Add the low-pass and high-pass images
    hybrid_img = cv2.addWeighted(image_low, 1, image_high, 1, 0)

    # # Save the hybrid image
    # cv2.imwrite('hybrid_img.jpg', hybrid_img)
    #
    # # Display the hybrid image
    # cv2.imshow('hybrid_img', hybrid_img)
    # cv2.waitKey()
    # cv2.destroyAllWindows()
    return hybrid_img.astype(np.uint8)


# Function to perform pyramid blending
# IMPORTANT MARK!!! I assumed that the pictures in the same size
def pyramid_blend(A, B, m, num_levels):
    # Threshold the mask image
    m[m == 255] = 1

    # Get the height and width of image A
    height, width, _ = A.shape

    # Resize image B and the mask to match the dimensions of image A
    B = cv2.resize(B, (width, height))
    m = cv2.resize(m, (width, height))

    # Create Gaussian pyramids for images A, B, and the mask
    GA, GB, GM = A.copy(), B.copy(), m.copy()
    gpA, gpB, gpM = [GA], [GB], [GM]

    for i in range(num_levels):
        GA = cv2.pyrDown(GA)
        GB = cv2.pyrDown(GB)
        GM = cv2.pyrDown(GM)

        gpA.append(np.float32(GA))
        gpB.append(np.float32(GB))
        gpM.append(np.float32(GM))

    # Create Laplacian pyramids for images A and B
    lpA, lpB, gpMr = [gpA[num_levels - 1]], [gpB[num_levels - 1]], [gpM[num_levels - 1]]

    for i in range(num_levels - 1, 0, -1):
        size = (gpA[i - 1].shape[1], gpA[i - 1].shape[0])
        LA = np.subtract(gpA[i - 1], cv2.pyrUp(gpA[i], dstsize=size))
        LB = np.subtract(gpB[i - 1], cv2.pyrUp(gpB[i], dstsize=size))

        lpA.append(LA)
        lpB.append(LB)
        gpMr.append(gpM[i - 1])

    # Blend the Laplacian pyramids
    LS = []
    for la, lb, gm in zip(lpA, lpB, gpMr):
        gm_resized = cv2.resize(gm, (la.shape[1], la.shape[0]))
        ls = la * gm_resized + lb * (1.0 - gm_resized)
        LS.append(ls)

    # Reconstruct the blended image from the Laplacian pyramids
    ls_ = LS[0]
    for i in range(1, num_levels):
        size = (LS[i].shape[1], LS[i].shape[0])
        ls_ = cv2.add(cv2.pyrUp(ls_, dstsize=size), np.float32(LS[i]))
        ls_[ls_ > 255] = 255
        ls_[ls_ < 0] = 0


    # cv2.imwrite('pyramid_blend_img.jpg', ls_)


    return ls_.astype(np.uint8)

