"""
Instruksi Pembuatan Function untuk Modul Edge Detection & Morphology
"""

def threshold(file, thresh, method):
    """
    Fungsi: Mengkonversi gambar ke biner berdasarkan nilai ambang batas.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - thresh (integer): Nilai ambang batas. (Wajib)
      - method (string): Metode ("binary", "otsu", "adaptive"). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar biner diencoding PNG base64.
    """
    pass

def canny(file, low, high):
    """
    Fungsi: Deteksi tepi dengan algoritma Canny.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - low (integer): Threshold bawah. (Wajib)
      - high (integer): Threshold atas. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Peta tepi diencoding PNG base64.
    """
    pass

def sobel(file, axis):
    """
    Fungsi: Deteksi tepi dengan operator Sobel.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - axis (string): Sumbu gradient ("x", "y", "both"). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Peta gradient diencoding PNG base64.
    """
    pass

def prewitt(file):
    """
    Fungsi: Deteksi tepi dengan operator Prewitt.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Peta tepi Prewitt diencoding PNG base64.
    """
    pass

def robert(file):
    """
    Fungsi: Deteksi tepi dengan operator Robert Cross.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Peta tepi Robert diencoding PNG base64.
    """
    pass

def laplacian(file, ksize):
    """
    Fungsi: Deteksi tepi dengan operator Laplacian.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - ksize (integer): Ukuran kernel aperture. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Peta tepi Laplacian diencoding PNG base64.
    """
    pass

def log(file, sigma):
    """
    Fungsi: Laplacian of Gaussian (LoG) deteksi tepi.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - sigma (float): Nilai sigma untuk Gaussian pre-smoothing. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Peta tepi LoG diencoding PNG base64.
    """
    pass

def erode(file, kernel_size, iterations=1):
    """
    Fungsi: Operasi morfologi erosion untuk memperkecil area putih.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - kernel_size (integer): Ukuran structuring element. (Wajib)
      - iterations (integer): Jumlah iterasi erosion. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil erosion diencoding PNG base64.
    """
    pass

def dilate(file, kernel_size, iterations=1):
    """
    Fungsi: Operasi morfologi dilation untuk memperluas area putih.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - kernel_size (integer): Ukuran structuring element. (Wajib)
      - iterations (integer): Jumlah iterasi dilation. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil dilation diencoding PNG base64.
    """
    pass
