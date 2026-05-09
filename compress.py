"""
Instruksi Pembuatan Function untuk Modul Image Compression
"""

def jpeg(file, quality):
    """
    Fungsi: Mengkompresi gambar menggunakan algoritma JPEG.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - quality (integer): Kualitas JPEG (1-100). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar terkompresi diencoding PNG base64.
        - original_kb (float): Ukuran file original dalam KB.
        - compressed_kb (float): Ukuran file setelah kompresi dalam KB.
        - ratio (float): Rasio kompresi.
        - method (string): Metode yang digunakan ("JPEG").
    """
    pass
