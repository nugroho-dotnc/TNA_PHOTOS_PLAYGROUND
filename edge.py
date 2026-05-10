"""
Modul Edge Detection & Morphology
Input  : numpy array BGR (dari cv2.imread)
Return : numpy array BGR hasil pemrosesan
"""

import cv2
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────

def threshold(image, thresh, method):
    """
    Mengkonversi gambar ke biner berdasarkan nilai ambang batas.
    - image  : numpy array BGR
    - thresh : integer, nilai ambang batas (0-255)
    - method : string, "binary" | "otsu" | "adaptive"
    - return : numpy array BGR (gambar biner)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "binary":
        _, result = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

    elif method == "otsu":
        _, result = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    elif method == "adaptive":
        result = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            blockSize=11,
            C=2
        )
    else:
        raise ValueError(f"Method '{method}' tidak dikenal. Pilih: binary, otsu, adaptive.")

    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


def canny(image, low, high):
    """
    Deteksi tepi dengan algoritma Canny.
    - image  : numpy array BGR
    - low    : integer, threshold bawah
    - high   : integer, threshold atas
    - return : numpy array BGR (peta tepi)
    """
    gray    = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges   = cv2.Canny(blurred, low, high)

    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)


def sobel(image, axis):
    """
    Deteksi tepi dengan operator Sobel.
    - image  : numpy array BGR
    - axis   : string, "x" | "y" | "both"
    - return : numpy array BGR (peta gradient)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if axis == "x":
        result = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        result = np.uint8(np.absolute(result))

    elif axis == "y":
        result = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        result = np.uint8(np.absolute(result))

    elif axis == "both":
        gx     = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
        gy     = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
        result = np.uint8(np.clip(np.sqrt(gx**2 + gy**2), 0, 255))

    else:
        raise ValueError(f"Axis '{axis}' tidak dikenal. Pilih: x, y, both.")

    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


def prewitt(image):
    """
    Deteksi tepi dengan operator Prewitt.
    - image  : numpy array BGR
    - return : numpy array BGR (peta tepi Prewitt)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(np.float64)

    kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float64)
    ky = np.array([[-1,-1,-1], [ 0, 0, 0], [ 1, 1, 1]], dtype=np.float64)

    gx     = cv2.filter2D(gray, -1, kx)
    gy     = cv2.filter2D(gray, -1, ky)
    result = np.uint8(np.clip(np.sqrt(gx**2 + gy**2), 0, 255))

    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


def robert(image):
    """
    Deteksi tepi dengan operator Robert Cross.
    - image  : numpy array BGR
    - return : numpy array BGR (peta tepi Robert)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).astype(np.float64)

    kx = np.array([[ 1,  0], [ 0, -1]], dtype=np.float64)
    ky = np.array([[ 0,  1], [-1,  0]], dtype=np.float64)

    gx     = cv2.filter2D(gray, -1, kx)
    gy     = cv2.filter2D(gray, -1, ky)
    result = np.uint8(np.clip(np.sqrt(gx**2 + gy**2), 0, 255))

    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


def laplacian(image, ksize):
    """
    Deteksi tepi dengan operator Laplacian.
    - image  : numpy array BGR
    - ksize  : integer, ukuran kernel (harus ganjil: 1, 3, 5, ...)
    - return : numpy array BGR (peta tepi Laplacian)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if ksize % 2 == 0:
        ksize += 1

    lap    = cv2.Laplacian(gray, cv2.CV_64F, ksize=ksize)
    result = np.uint8(np.clip(np.absolute(lap), 0, 255))

    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


def log(image, sigma):
    """
    Laplacian of Gaussian (LoG) deteksi tepi.
    - image  : numpy array BGR
    - sigma  : float, nilai sigma untuk Gaussian pre-smoothing
    - return : numpy array BGR (peta tepi LoG)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ksize = int(2 * np.ceil(3 * sigma) + 1)
    if ksize % 2 == 0:
        ksize += 1
    ksize = max(ksize, 3)

    blurred = cv2.GaussianBlur(gray, (ksize, ksize), sigmaX=sigma)
    lap     = cv2.Laplacian(blurred, cv2.CV_64F)
    result  = np.uint8(np.clip(np.absolute(lap), 0, 255))

    return cv2.cvtColor(result, cv2.COLOR_GRAY2BGR)


def erode(image, kernel_size, iterations=1):
    """
    Operasi morfologi erosion (memperkecil area putih).
    - image       : numpy array BGR
    - kernel_size : integer, ukuran structuring element
    - iterations  : integer, jumlah iterasi (default=1)
    - return      : numpy array BGR hasil erosion
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.erode(image, kernel, iterations=iterations)


def dilate(image, kernel_size, iterations=1):
    """
    Operasi morfologi dilation (memperluas area putih).
    - image       : numpy array BGR
    - kernel_size : integer, ukuran structuring element
    - iterations  : integer, jumlah iterasi (default=1)
    - return      : numpy array BGR hasil dilation
    """
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_size, kernel_size))
    return cv2.dilate(image, kernel, iterations=iterations)


# ──────────────────────────────────────────────────────────────────────────────
# TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    img = cv2.imread("pxfuel.jpg")  # ganti dengan path gambar kamu

    cv2.imwrite("out_threshold_binary.png",   threshold(img, 127, "binary"))
    cv2.imwrite("out_threshold_otsu.png",     threshold(img, 0,   "otsu"))
    cv2.imwrite("out_threshold_adaptive.png", threshold(img, 0,   "adaptive"))
    cv2.imwrite("out_canny.png",              canny(img, 50, 150))
    cv2.imwrite("out_sobel_x.png",            sobel(img, "x"))
    cv2.imwrite("out_sobel_y.png",            sobel(img, "y"))
    cv2.imwrite("out_sobel_both.png",         sobel(img, "both"))
    cv2.imwrite("out_prewitt.png",            prewitt(img))
    cv2.imwrite("out_robert.png",             robert(img))
    cv2.imwrite("out_laplacian.png",          laplacian(img, 3))
    cv2.imwrite("out_log.png",                log(img, 1.0))
    cv2.imwrite("out_erode.png",              erode(img, 5, iterations=2))
    cv2.imwrite("out_dilate.png",             dilate(img, 5, iterations=2))

    print("Semua hasil edge.py tersimpan.")