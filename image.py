"""
Instruksi Pembuatan Function untuk Modul Image Management
"""

def upload(file):
    """
    Fungsi: Mengupload file gambar ke server. Backend membaca file, menyimpan salinan original ke dalam sesi UUID, lalu mengembalikan metadata dan representasi base64 gambar tersebut.
    Input: 
      - file (UploadFile): File gambar yang diupload. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - id (string UUID): ID sesi unik untuk gambar ini.
        - width (integer): Lebar gambar dalam piksel.
        - height (integer): Tinggi gambar dalam piksel.
        - format (string): Format asli gambar.
        - size_kb (float): Ukuran file original dalam kilobyte.
        - image_b64 (string): Gambar original diencoding sebagai PNG base64.
    """
    pass

def reset(id):
    """
    Fungsi: Mengembalikan gambar ke kondisi original sesuai UUID sesi.
    Input:
      - id (string): UUID sesi gambar yang ingin direset. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar original diencoding ulang sebagai PNG base64.
        - message (string): Pesan konfirmasi.
    """
    pass

def save(image_b64, format, filename=None):
    """
    Fungsi: Mengkonversi gambar hasil (base64) menjadi file binary siap download.
    Input:
      - image_b64 (string): Gambar hasil editing diencoding base64. (Wajib)
      - format (string): Format output yang diinginkan (PNG/JPEG/BMP). (Wajib)
      - filename (string): Nama file output. (Opsional)
    Return:
      - Binary file (bytes): Raw binary file gambar dengan Content-Type sesuai format.
    """
    pass
