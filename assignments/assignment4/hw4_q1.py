"""
Compute the Mandelbrot fractal
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


def mandel(
    n: int,
    thresh: float = 50.0,
    xlims: np.ndarray = np.array([-2, 1]),
    nx: int = 1500,
    ylims: np.ndarray = np.array([-1.5, 1.5]),
    ny: int = 1500,
) -> np.ndarray:
    """Computes the Mandelbrot fractal on some given set of numbers.

    Parameters
    ----------
    n : int
        Number of iterations.
    thresh : float
        Threshold which decides if a number is a part of the set.
    xlims, ylims : np.ndarray
        Limits for the computation of the fractal.
    nx, ny : int
        Number of points between xlims.min() and xlims.max() to calculate the set on.

    Returns
    -------
    mandelbrot_set : np.ndarray
        A binary image with a value of 1 if the point belongs to the set.
        The shape of the resulting image is (nx, ny).
    """
    x = np.linspace(xlims[0], xlims[1], nx)
    y = np.linspace(ylims[0], ylims[1], ny)

    # Broadcasting rules makes this line create the base image
    c = x[:, np.newaxis] + 1j * y[np.newaxis, :]

    z = c
    for _ in range(n):
        z = z ** 2 + c

    mandelbrot_set = np.abs(z) < thresh
    return mandelbrot_set


if __name__ == "__main__":
    mandelbrot_set = mandel(50)
    fig, ax = plt.subplots()
    ax.imshow(mandelbrot_set.T, extent=[-2, 1, -1.5, 1.5], cmap="gray")
    ax.axis("off")
    plt.show()
    fig.savefig("mandelbrot_tmp.png")
