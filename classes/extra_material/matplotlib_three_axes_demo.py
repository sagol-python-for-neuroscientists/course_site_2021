"""
The goal of this demo, which should be run during class 6, is to show how
useful and better the OO interface of Python truly is. The final code
here is pretty simple, but it should be written from scratch, in front
of the students. This also drives home the point of procedural programming
and shows them how the instructor thinks when designing his code.

The "plotting example", also from class 6, refers to showing how to use
the "plot()" method of a DF instead of this code. The generated plots
are sometimes not as nice, but they're definitely easier to generate.

"plotting example" also shows "pd.read_clipboard()" by taking data
from online resources (https://rcompanion.org/rcompanion/d_07.html)
and "pasting" them into a dataframe, and then
plotting it with a couple lines of code. Finally we show how two lines
of seaborn code can make this whole story to be much easier.
"""

import numpy as np
import matplotlib.pyplot as plt


def make_single_sine(t: np.ndarray, freq: float=1.0) -> np.ndarray:
    """Creates a one dimensional sine wave with the given freq (Hz)"""
    return np.sin(2 * np.pi * t * freq)


def make_sines(freqs: list, t: np.ndarray) -> np.ndarray:
    """Creates a 2D array, where each row is a single sine wave with a
    given frequency."""
    rows = len(freqs)
    columns = len(t)
    sine_waves = np.zeros((rows, columns))
    for idx, freq in enumerate(freqs):
        sine_waves[idx] = make_single_sine(t, freq)
    return sine_waves


if __name__ == "__main__":
    freqs = [1, 5, 10]  # Hz
    t = np.arange(0, 5, 0.01)
    sine_waves = make_sines(freqs, t)

    fig, axes = plt.subplots(len(freqs), 1, sharex=True)
    for ax, freq, sine_wave in zip(axes, freqs, sine_waves):
        ax.plot(sine_wave)
        ax.set_ylabel(f"{str(freq)} [Hz]")

    plt.show()



