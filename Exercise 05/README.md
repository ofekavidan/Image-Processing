# Image Processing - Exercise 5: Image Restoration Using GAN Inversion

Project Overview

This project explores image restoration techniques using GAN inversion, specifically leveraging StyleGAN2. The goal is to restore degraded images that have been altered by various forms of degradation, including grayscale conversion and masking. The restoration process involves optimizing the latent vector of the image to closely match the original, high-quality image.

Key Techniques:

GAN Inversion: Uses pre-trained StyleGAN2 to invert the latent vector and optimize it for restoring degraded images.

Optimization: The latent vector is iteratively optimized using gradient descent to minimize the difference between the generated image and the target degraded image.

Degradation Models: Various degradation processes, such as masking or grayscale conversion, are applied to test the robustness of the restoration algorithm.

![image](https://github.com/user-attachments/assets/addc68aa-3db2-491e-b173-fec620cb352d)

![image](https://github.com/user-attachments/assets/3652682d-b223-4971-9046-24ae8c04a3be)
