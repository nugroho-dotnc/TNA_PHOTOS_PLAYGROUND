"""
Modul Image Enhancement
Input  : numpy array BGR (dari cv2.imread)
Return : numpy array BGR hasil pemrosesan
"""

import cv2
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────

def brightness_contrast(image, alpha, beta):
    """
    Mengatur kecerahan dan kontras gambar.
    Rumus: output = clip(alpha * input + beta, 0, 255)
    - image  : numpy array BGR
    - alpha  : float, faktor kontras (0.0 - 3.0)
    - beta   : float, offset kecerahan (-100 hingga +100)
    - return : numpy array BGR hasil
    """
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)


def equalize(image, channel):
    """
    Histogram equalization untuk meningkatkan kontras secara global.
    - image   : numpy array BGR
    - channel : string, "gray" | "rgb"
    - return  : numpy array BGR hasil
    """
    if channel == "gray":
        gray   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        eq     = cv2.equalizeHist(gray)
        result = cv2.cvtColor(eq, cv2.COLOR_GRAY2BGR)

    elif channel == "rgb":
        b, g, r = cv2.split(image)
        result  = cv2.merge([
            cv2.equalizeHist(b),
            cv2.equalizeHist(g),
            cv2.equalizeHist(r),
        ])

    else:
        raise ValueError(f"Channel '{channel}' tidak dikenal. Pilih: gray, rgb.")

    return result


def sharpen(image, intensity):
    """
    Mempertajam gambar dengan kernel sharpening via konvolusi 2D.
    - image     : numpy array BGR
    - intensity : float, intensitas sharpening (0.0 - 5.0)
    - return    : numpy array BGR hasil
    """
    kernel = np.array([
        [ 0,          -intensity,          0],
        [-intensity,   1 + 4*intensity,   -intensity],
        [ 0,          -intensity,          0]
    ], dtype=np.float64)

    result = cv2.filter2D(image, -1, kernel)
    return np.clip(result, 0, 255).astype(np.uint8)


def smooth(image, kernel_size):
    """
    Menghaluskan gambar (blur) dengan Gaussian Blur.
    - image       : numpy array BGR
    - kernel_size : integer, ukuran kernel Gaussian (ganjil: 3, 5, 7, 9, ...)
    - return      : numpy array BGR hasil
    """
    if kernel_size < 3:
        kernel_size = 3
    if kernel_size % 2 == 0:
        kernel_size += 1  # pastikan ganjil

    return cv2.GaussianBlur(image, (kernel_size, kernel_size), sigmaX=0)


# ──────────────────────────────────────────────────────────────────────────────
# TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    img = cv2.imread("pxfuel.jpg")  # ganti dengan path gambar kamu

    cv2.imwrite("out_brightness_contrast.png", brightness_contrast(img, alpha=1.5, beta=30))
    cv2.imwrite("out_equalize_gray.png",       equalize(img, "gray"))
    cv2.imwrite("out_equalize_rgb.png",        equalize(img, "rgb"))
    cv2.imwrite("out_sharpen.png",             sharpen(img, intensity=2.0))
    cv2.imwrite("out_smooth.png",              smooth(img, kernel_size=7))

    print("Semua hasil enhance.py tersimpan.")