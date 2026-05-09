"""
Instruksi Pembuatan Function untuk Modul Histogram Analysis
"""

def analyze(file):
    """
    Fungsi: Menghitung histogram distribusi piksel untuk satu gambar.
    Input:
      - file (UploadFile): File gambar yang akan dianalisis. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - R, G, B, L (array[256] float): Histogram channel merah, hijau, biru, dan luminance.
        - mean (float): Rata-rata nilai piksel keseluruhan gambar.
        - std (float): Standar deviasi nilai piksel.
        - min (integer): Nilai piksel minimum.
        - max (integer): Nilai piksel maksimum.
    """
    pass

def compare(file_before, file_after):
    """
    Fungsi: Menghitung dan membandingkan histogram dua gambar (before dan after) dalam satu request.
    Input:
      - file_before (UploadFile): Gambar sebelum operasi. (Wajib)
      - file_after (UploadFile): Gambar sesudah operasi. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - before (object): Objek histogram gambar before (struktur sama seperti analyze).
        - after (object): Objek histogram gambar after (struktur sama seperti analyze).
    """
    pass
