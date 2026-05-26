"""
Modul Image Segmentation
Input  : numpy array BGR (dari cv2.imread)
Return : numpy array BGR hasil segmentasi
"""

import cv2
import numpy as np
import random
import base64

def _to_base64_png(image):
    _, buffer = cv2.imencode('.png', image)
    return base64.b64encode(buffer).decode('utf-8')


# ──────────────────────────────────────────────────────────────────────────────
# FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────

def threshold(image, thresh, method):
    """
    Segmentasi berbasis threshold — memisahkan foreground & background
    dengan overlay warna merah pada area foreground.
    - image  : numpy array BGR
    - thresh : integer, nilai ambang batas (0-255)
    - method : string, "binary" | "otsu" | "adaptive"
    - return : numpy array BGR (gambar tersegmentasi dengan overlay warna)
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if method == "binary":
        _, mask = cv2.threshold(gray, thresh, 255, cv2.THRESH_BINARY)

    elif method == "otsu":
        _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    elif method == "adaptive":
        mask = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            blockSize=11,
            C=2
        )
    else:
        raise ValueError(f"Method '{method}' tidak dikenal. Pilih: binary, otsu, adaptive.")

    # Overlay warna merah pada foreground (area putih di mask)
    overlay          = image.copy()
    overlay[mask == 255] = [0, 0, 200]  # BGR merah

    # Blend dengan gambar asli
    result = cv2.addWeighted(image, 0.4, overlay, 0.6, 0)
    return {"processed_image": _to_base64_png(result)}


def edge(image, low, high):
    """
    Segmentasi berbasis tepi — Canny lalu tiap kontur diberi warna acak.
    - image  : numpy array BGR
    - low    : integer, threshold bawah Canny
    - high   : integer, threshold atas Canny
    - return : numpy array BGR (gambar dengan kontur berwarna berbeda)
    """
    gray      = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred   = cv2.GaussianBlur(gray, (5, 5), 0)
    edges_map = cv2.Canny(blurred, low, high)

    contours, _ = cv2.findContours(
        edges_map,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = image.copy()
    random.seed(42)  # seed agar warna konsisten tiap run
    for cnt in contours:
        color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255),
        )
        cv2.drawContours(result, [cnt], -1, color, thickness=2)

    return {"processed_image": _to_base64_png(result)}


def region(image, n_segments):
    """
    Segmentasi berbasis region menggunakan K-Means clustering.
    Setiap piksel diganti warna rata-rata klasternya.
    - image      : numpy array BGR
    - n_segments : integer, jumlah region/klaster (2-8)
    - return     : numpy array BGR (gambar tersegmentasi per region)
    """
    n_segments = max(2, min(8, n_segments))  # clamp ke 2-8

    h, w   = image.shape[:2]
    pixels = image.reshape((-1, 3)).astype(np.float32)

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        100,   # max iterasi
        0.2    # epsilon
    )

    _, labels, centers = cv2.kmeans(
        pixels,
        n_segments,
        None,
        criteria,
        attempts=10,
        flags=cv2.KMEANS_RANDOM_CENTERS
    )

    centers = np.uint8(centers)
    result  = centers[labels.flatten()].reshape((h, w, 3))
    return {"processed_image": _to_base64_png(result)}


# ──────────────────────────────────────────────────────────────────────────────
# TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import os
    os.makedirs("segment", exist_ok=True)
    img = cv2.imread("pxfuel.jpg")  # ganti dengan path gambar kamu

    def save_res(res_dict, filename):
        filepath = os.path.join("segment", filename)
        print(f"Hasil {filename}:", list(res_dict.keys()))
        with open(filepath, "wb") as f:
            f.write(base64.b64decode(res_dict["processed_image"]))

    save_res(threshold(img, 127, "binary"), "out_segment_threshold_binary.png")
    save_res(threshold(img, 0,   "otsu"), "out_segment_threshold_otsu.png")
    save_res(threshold(img, 0,   "adaptive"), "out_segment_threshold_adaptive.png")
    save_res(edge(img, 50, 150), "out_segment_edge.png")
    save_res(region(img, 3), "out_segment_region_3.png")
    save_res(region(img, 5), "out_segment_region_5.png")

    print("Semua hasil segment.py tersimpan.")