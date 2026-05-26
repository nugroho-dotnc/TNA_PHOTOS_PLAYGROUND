"""
Instruksi Pembuatan Function untuk Modul Color Processing
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


def grayscale(file):
    """
    Fungsi: Mengkonversi gambar berwarna ke mode grayscale (hitam-putih).
    Input:
      - file (UploadFile): Gambar berwarna. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar grayscale diencoding PNG base64.
    """
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    processed = image.convert("L")
    return {"processed_image": _to_base64_png(processed)}


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data)).convert("RGB")
    r, g, b = image.split()
    channel = channel.upper()
    if channel == "R":
        processed = Image.merge("RGB", (r, Image.new("L", image.size), Image.new("L", image.size)))
    elif channel == "G":
        processed = Image.merge("RGB", (Image.new("L", image.size), g, Image.new("L", image.size)))
    elif channel == "B":
        processed = Image.merge("RGB", (Image.new("L", image.size), Image.new("L", image.size), b))
    else:
        raise ValueError("Channel harus 'R', 'G', atau 'B'")
    return {"processed_image": _to_base64_png(processed)}


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data)).convert("RGB")
    hsv = image.convert("HSV")
    h, s, v = hsv.split()
    h_adjust = int(round(float(hue_shift) * 255.0 / 360.0))
    h = h.point(lambda p: (p + h_adjust) % 256)
    s = s.point(lambda p: int(max(0, min(255, p * float(sat_scale)))))
    processed = Image.merge("HSV", (h, s, v)).convert("RGB")
    return {"processed_image": _to_base64_png(processed)}


if __name__ == "__main__":
    import os
    os.makedirs("color", exist_ok=True)
    
    def save_res(res_dict, filename):
        filepath = os.path.join("color", filename)
        print(f"Hasil {filename}:", list(res_dict.keys()))
        with open(filepath, "wb") as f:
            f.write(base64.b64decode(res_dict["processed_image"]))

    with open("pxfuel.jpg", "rb") as f:
        data = f.read()
    
    class MockFile:
        def read(self):
            return data

    save_res(grayscale(MockFile()), "out_color_grayscale.png")
    save_res(channel(MockFile(), "R"), "out_color_channel_R.png")
    save_res(hue_saturation(MockFile(), 45, 1.5), "out_color_hue_sat.png")
    
    print("Semua hasil color.py tersimpan.")
