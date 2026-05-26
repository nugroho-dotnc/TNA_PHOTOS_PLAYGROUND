"""
Instruksi Pembuatan Function untuk Modul Image Compression
"""

import base64
import io
from PIL import Image


def _read_upload_file(file):
    if hasattr(file, "file"):
        file.file.seek(0)
        data = file.file.read()
        file.file.seek(0)
        return data
    if hasattr(file, "read"):
        data = file.read()
        return data if isinstance(data, bytes) else data.encode()
    raise ValueError("UploadFile tidak valid")


def _to_base64_png(image):
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode("utf-8")


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
    data = _read_upload_file(file)
    original_kb = len(data) / 1024.0
    image = Image.open(io.BytesIO(data))
    if image.mode not in ("RGB", "L"):
        image = image.convert("RGB")

    output_jpeg = io.BytesIO()
    image.save(output_jpeg, format="JPEG", quality=int(quality))
    compressed_bytes = output_jpeg.getvalue()
    compressed_kb = len(compressed_bytes) / 1024.0

    compressed_image = Image.open(io.BytesIO(compressed_bytes))
    if compressed_image.mode not in ("RGB", "L"):
        compressed_image = compressed_image.convert("RGB")

    ratio = original_kb / compressed_kb if compressed_kb > 0 else 0.0

    return {
        "processed_image": _to_base64_png(compressed_image),
        "original_kb": round(original_kb, 3),
        "compressed_kb": round(compressed_kb, 3),
        "ratio": round(ratio, 3),
        "method": "JPEG",
    }


if __name__ == "__main__":
    import os
    os.makedirs("compress", exist_ok=True)
    
    def save_res(res_dict, filename):
        filepath = os.path.join("compress", filename)
        print(f"Hasil {filename}:", list(res_dict.keys()))
        with open(filepath, "wb") as f:
            f.write(base64.b64decode(res_dict["processed_image"]))

    with open("pxfuel.jpg", "rb") as f:
        data = f.read()
    
    class MockFile:
        def read(self):
            return data

    res = jpeg(MockFile(), 50)
    print("Stats compression:", {k: v for k, v in res.items() if k != "processed_image"})
    save_res(res, "out_compress_jpeg.png")
    
    print("Semua hasil compress.py tersimpan.")
