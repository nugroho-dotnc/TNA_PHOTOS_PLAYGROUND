"""
Instruksi Pembuatan Function untuk Modul Image Segmentation
"""

def threshold(file, thresh, method):
    """
    Fungsi: Segmentasi berbasis threshold biner, memisahkan foreground & background dengan overlay warna.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - thresh (integer): Nilai ambang batas. (Wajib)
      - method (string): Metode ("binary", "otsu", "adaptive"). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar tersegmentasi dengan overlay warna diencoding PNG base64.
    """
    pass

def edge(file, low, high):
    """
    Fungsi: Segmentasi berbasis tepi menggunakan Canny lalu mewarnai tiap kontur secara acak.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - low (integer): Threshold bawah Canny. (Wajib)
      - high (integer): Threshold atas Canny. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar dengan kontur berwarna berbeda diencoding PNG base64.
    """
    pass

def region(file, n_segments):
    """
    Fungsi: Segmentasi berbasis region menggunakan SLIC atau K-Means.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - n_segments (integer): Jumlah region target (2-8). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar dengan region berwarna rata-rata klaster diencoding PNG base64.
    """
    pass
