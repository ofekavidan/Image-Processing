# Image Processing - Scene Change Detection

Project Overview

This project focuses on detecting scene changes in videos by analyzing differences between consecutive frames. The detection is based on histogram analysis of the grayscale representation of video frames. The project implements two algorithms based on the type of video being analyzed.

Key Components:

Grayscale Conversion: The RGB video frames are converted into grayscale for simplified analysis using a predefined matrix.

Histogram Calculation: Histograms are generated for each frame of the video.

Scene Change Detection: Differences between consecutive histograms (or cumulative histograms) are calculated to detect where a scene change occurs.
