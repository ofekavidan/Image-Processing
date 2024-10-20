# Image Processing - High-Resolution Image Enhancement

Project Overview

The goal of this project is to develop an algorithm that seamlessly combines a low-resolution image with a high-resolution region of the same image. The challenge is to enhance the quality of the low-resolution image by blending the high-resolution details into the corresponding areas without creating visual artifacts.

Key Techniques:

SIFT (Scale-Invariant Feature Transform): Used to identify key points of interest in both low and high-resolution images.

RANSAC (Random Sample Consensus): Applied to estimate the geometric transformation between the matched points in the images.

Image Warping: Uses the estimated transformation matrix to align the high-resolution portion with the low-resolution image.

Blending: Merges the aligned high-resolution region with the low-resolution image, ensuring smooth transitions.

![image](https://github.com/user-attachments/assets/c26cabdb-239c-4dab-80f1-79c9a3bf7070)

