import numpy as np
import mediapy as media
# Import necessary libraries/modules

RGB_TO_GRAY_MAT = np.array([0.2989, 0.5870, 0.1140])
# Define a matrix for converting RGB to grayscale

def main(video_path, video_type):
    """
    Main entry point for ex1
    :param video_path: path to video file
    :param video_type: category of the video (either 1 or 2)
    :return: a tuple of integers representing the frame number for which the scene cut was detected
    (i.e., the last frame index of the first scene and the first frame index of the second scene)
    """
    # Main function for scene change detection

    video = media.read_video(video_path)
    # Read the video using the 'mediapy' module
    np_video = np.array(video)
    # Convert the video frames to a NumPy array

    video_g = (np_video @ RGB_TO_GRAY_MAT).astype(int)
    # Convert the RGB video to grayscale using the defined matrix

    histograms = np.array([np.histogram(img, bins=256, range=(0, 256))[0] for img in video_g])
    # Calculate histograms for each frame in the grayscale video

    cumsums = np.cumsum(histograms, axis=1)
    # Calculate the cumulative sum of histograms along the columns

    # If the video is of category 2,
    # we will have to perform the (stronger) algorithm
    # of subtracting columns from the cumulative histograms.
    # Otherwise, the video is from category 1, so it will be enough for us to perform the weaker algorithm,
    # that is, to subtract the normal histograms of each successive pair of frames.
    if video_type == 1:
        dists = histograms[:-1] - histograms[1:]
        # Calculate the differences between consecutive histograms
    else: # video_type == 2
        dists = cumsums[:-1] - cumsums[1:]
        # Calculate the differences between consecutive cumulative histograms
    dists = np.linalg.norm(dists, axis=1)
    # Calculate the Euclidean norm of each row in the differences

    mx = np.argmax(dists)
    # Find the index of the maximum value in the norm array, indicating the scene change
    return mx, mx + 1
    # Return a tuple representing the detected scene change: (last frame index of the first scene,
    # first frame index of the second scene)
