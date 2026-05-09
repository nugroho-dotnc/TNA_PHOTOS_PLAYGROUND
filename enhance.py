"""
Instruksi Pembuatan Function untuk Modul Image Enhancement
"""

def brightness_contrast(file, alpha, beta):
    """
    Fungsi: Mengatur kecerahan (brightness) dan kontras gambar menggunakan rumus linear: output = alpha * input + beta.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - alpha (float): Faktor kontras (0.0 - 3.0). (Wajib)
      - beta (float): Offset kecerahan (-100 hingga +100). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def equalize(file, channel):
    """
    Fungsi: Melakukan histogram equalization untuk meningkatkan kontras secara global.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - channel (string): Mode equalization ("gray" atau "rgb"). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def sharpen(file, intensity):
    """
    Fungsi: Mempertajam gambar dengan menerapkan kernel sharpening via konvolusi 2D.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - intensity (float): Intensitas sharpening (0.0 - 5.0). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def smooth(file, kernel_size):
    """
    Fungsi: Menghaluskan gambar (blur) dengan Gaussian Blur menggunakan ukuran kernel yang dapat dikonfigurasi.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran kernel Gaussian (ganjil, misal 3, 5, 7, 9). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass
