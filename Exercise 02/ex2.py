import numpy as np
from matplotlib import pyplot as plt
from scipy.io import wavfile as wav
import librosa
import librosa.display
from scipy.signal import stft, istft

"""
:param audio_path: path to q1 audio file
:return: return q1 denoised version
"""
def q1(audio_path) -> np.array:
    # Read audio file
    signal, sample_rate = librosa.load(audio_path, sr=4000)

    # Perform FFT on the audio signal
    f = np.fft.fft(signal)

    # Set the frequency component with the maximum magnitude to zero
    f[np.argmax(np.abs(f))] = 0

    # Set another frequency component with the maximum magnitude to zero
    f[np.argmax(np.abs(f))] = 0

    # Inverse FFT to obtain the denoised signal
    new_signal = np.fft.ifft(f).real

    # Normalize the denoised signal
    new_signal = (new_signal / np.max(np.abs(new_signal))) * 32767

    # # Write the denoised signal to a new audio file
    # wav.write("new_q1.wav", sample_rate, new_signal.astype(np.int16))


    # Return the denoised signal as a numpy array
    return new_signal

"""
    :param audio_path: path to q2 audio file
    :return: return q2 denoised version
"""
def q2(audio_path) -> np.array:

    # Read audio file
    sample_rate, signal = wav.read(audio_path)

    # Compute the STFT using scipy.signal.stft
    _, _, stft_matrix = stft(signal, fs=sample_rate, nperseg=400, noverlap=200)


    # Apply time-frequency masking to set certain frequency components to zero
    stft_matrix[58:63, 28:85] = 0


    # Convert the modified STFT back to time domain using scipy.signal.istft
    _, reconstructed_audio = istft(stft_matrix, fs=sample_rate, nperseg=400, noverlap=200)

    # Normalize the reconstructed audio signal
    new_signal = (reconstructed_audio / np.max(np.abs(reconstructed_audio))) * 32767

    # wav.write("new_q2.wav", sample_rate, new_signal.astype(np.int16))


    # Return the denoised signal as a numpy array
    return new_signal

