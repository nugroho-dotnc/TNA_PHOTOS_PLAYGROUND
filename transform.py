"""
Instruksi Pembuatan Function untuk Modul Geometric Transformation
"""

def rotate(file, angle, interpolation=None):
    """
    Fungsi: Memutar gambar pada sumbu tengah (center pivot) dengan sudut yang ditentukan.
    Input:
      - file (UploadFile): Gambar yang akan diputar. (Wajib)
      - angle (float): Sudut rotasi dalam derajat. (Wajib)
      - interpolation (string): Metode interpolasi ("nearest" atau "bilinear"). (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def flip(file, direction):
    """
    Fungsi: Membalik gambar secara horizontal, vertikal, atau keduanya.
    Input:
      - file (UploadFile): Gambar yang akan dibalik. (Wajib)
      - direction (string): Arah flip ("horizontal", "vertical", "both"). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass

def crop(file, x, y, w, h):
    """
    Fungsi: Memotong bagian tertentu dari gambar berdasarkan koordinat piksel.
    Input:
      - file (UploadFile): Gambar yang akan dipotong. (Wajib)
      - x (integer): Koordinat X kiri atas. (Wajib)
      - y (integer): Koordinat Y kiri atas. (Wajib)
      - w (integer): Lebar area crop. (Wajib)
      - h (integer): Tinggi area crop. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil crop diencoding PNG base64.
    """
    pass

def resize(file, width, height, interpolation=None):
    """
    Fungsi: Mengubah dimensi gambar ke ukuran baru yang ditentukan.
    Input:
      - file (UploadFile): Gambar yang akan diubah ukurannya. (Wajib)
      - width (integer): Lebar target dalam piksel. (Wajib)
      - height (integer): Tinggi target dalam piksel. (Wajib)
      - interpolation (string): Metode interpolasi. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil resize diencoding PNG base64.
        - new_size (object): Dimensi gambar setelah resize {width, height}.
    """
    pass

def translate(file, tx, ty):
    """
    Fungsi: Menggeser gambar secara horizontal dan/atau vertikal.
    Input:
      - file (UploadFile): Gambar yang akan digeser. (Wajib)
      - tx (integer): Pergeseran horizontal. (Wajib)
      - ty (integer): Pergeseran vertikal. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass
