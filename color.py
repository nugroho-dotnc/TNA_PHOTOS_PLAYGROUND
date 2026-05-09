"""
Instruksi Pembuatan Function untuk Modul Color Processing
"""

def grayscale(file):
    """
    Fungsi: Mengkonversi gambar berwarna ke mode grayscale (hitam-putih).
    Input:
      - file (UploadFile): Gambar berwarna. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar grayscale diencoding PNG base64.
    """
    pass

def channel(file, channel):
    """
    Fungsi: Mengisolasi satu channel warna (R, G, atau B).
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - channel (string): Channel yang diisolasi ("R", "G", "B"). (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar dengan channel terisolasi diencoding PNG base64.
    """
    pass

def hue_saturation(file, hue_shift, sat_scale):
    """
    Fungsi: Menggeser hue dan mengubah saturasi gambar via HSV.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - hue_shift (integer): Pergeseran hue dalam derajat (-180 hingga +180). (Wajib)
      - sat_scale (float): Faktor skala saturasi. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    pass
