"""
Modul Histogram Analysis
Input  : numpy array BGR (dari cv2.imread)
Return : dict berisi data histogram dan statistik
"""

import cv2
import numpy as np


# ──────────────────────────────────────────────────────────────────────────────
# HELPER
# ──────────────────────────────────────────────────────────────────────────────

def _compute_histogram(image):
    """
    Hitung histogram dan statistik dari sebuah gambar BGR.
    Return dict: R, G, B, L (array 256), mean, std, min, max.
    """
    b_hist = cv2.calcHist([image], [0], None, [256], [0, 256]).flatten().tolist()
    g_hist = cv2.calcHist([image], [1], None, [256], [0, 256]).flatten().tolist()
    r_hist = cv2.calcHist([image], [2], None, [256], [0, 256]).flatten().tolist()

    gray   = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    l_hist = cv2.calcHist([gray], [0], None, [256], [0, 256]).flatten().tolist()

    pixels = gray.flatten().astype(np.float64)

    return {
        "R":    r_hist,
        "G":    g_hist,
        "B":    b_hist,
        "L":    l_hist,
        "mean": round(float(np.mean(pixels)), 4),
        "std":  round(float(np.std(pixels)),  4),
        "min":  int(np.min(pixels)),
        "max":  int(np.max(pixels)),
    }


# ──────────────────────────────────────────────────────────────────────────────
# FUNCTIONS
# ──────────────────────────────────────────────────────────────────────────────

def analyze(image):
    """
    Menghitung histogram distribusi piksel untuk satu gambar.
    - image  : numpy array BGR
    - return : dict dengan field R, G, B, L (array 256), mean, std, min, max
    """
    return _compute_histogram(image)


def compare(image_before, image_after):
    """
    Membandingkan histogram dua gambar (before dan after).
    - image_before : numpy array BGR, gambar sebelum operasi
    - image_after  : numpy array BGR, gambar sesudah operasi
    - return       : dict dengan field "before" dan "after"
                     (masing-masing struktur sama seperti analyze)
    """
    return {
        "before": _compute_histogram(image_before),
        "after":  _compute_histogram(image_after),
    }


# ──────────────────────────────────────────────────────────────────────────────
# TEST
# ──────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    import json
    import os
    os.makedirs("histogram", exist_ok=True)

    img        = cv2.imread("pxfuel.jpg")       # gambar asli
    img_bright = cv2.imread("pxfuel.jpg") # gambar sudah diproses (contoh)

    # Test analyze
    result_analyze = analyze(img)
    print("=== ANALYZE ===")
    print(f"  mean : {result_analyze['mean']}")
    print(f"  std  : {result_analyze['std']}")
    print(f"  min  : {result_analyze['min']}")
    print(f"  max  : {result_analyze['max']}")
    print(f"  R[0] : {result_analyze['R'][0]}")   # frekuensi piksel nilai 0 channel R
    
    with open(os.path.join("histogram", "out_analyze.json"), "w") as f:
        json.dump(result_analyze, f, indent=4)
    print("Hasil analyze tersimpan ke histogram/out_analyze.json")

    # Test compare
    result_compare = compare(img, img_bright)
    print("\n=== COMPARE ===")
    print(f"  before mean : {result_compare['before']['mean']}")
    print(f"  after  mean : {result_compare['after']['mean']}")
    
    with open(os.path.join("histogram", "out_compare.json"), "w") as f:
        json.dump(result_compare, f, indent=4)
    print("Hasil compare tersimpan ke histogram/out_compare.json")