"""
Instruksi Pembuatan Function untuk Modul Image Restoration
"""

def gaussian(file, kernel_size, sigma=0.0):
    """
    Fungsi: Menerapkan Gaussian Blur untuk menghaluskan gambar dan mereduksi noise.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran kernel. (Wajib)
      - sigma (float): Nilai sigma Gaussian. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def median(file, kernel_size):
    """
    Fungsi: Menerapkan Median Filter (efektif untuk noise salt & pepper).
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran kernel. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def denoise_sp(file, kernel_size=3):
    """
    Fungsi: Mendeteksi dan menghilangkan noise salt & pepper secara adaptif.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran window deteksi. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def convolve(file, kernel, normalize=False):
    """
    Fungsi: Menerapkan konvolusi custom dengan kernel yang didefinisikan pengguna.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel (string): Matriks kernel 2D dalam format JSON. (Wajib)
      - normalize (boolean): Jika true, kernel dibagi jumlah absolutnya. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass
