"""
Instruksi Pembuatan Function untuk Modul Geometric Transformation
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


def _get_resample(interpolation):
    if interpolation is None:
        return Image.NEAREST
    if interpolation.lower() == "bilinear":
        return Image.BILINEAR
    return Image.NEAREST


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    processed = image.convert("RGBA").rotate(-float(angle), resample=_get_resample(interpolation), expand=True)
    return {"processed_image": _to_base64_png(processed)}


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    direction = direction.lower()
    if direction == "horizontal":
        processed = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif direction == "vertical":
        processed = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif direction == "both":
        processed = image.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.FLIP_TOP_BOTTOM)
    else:
        raise ValueError("Arah flip harus 'horizontal', 'vertical', atau 'both'")
    return {"processed_image": _to_base64_png(processed)}


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    x, y, w, h = int(x), int(y), int(w), int(h)
    x = max(0, x)
    y = max(0, y)
    w = max(0, w)
    h = max(0, h)
    processed = image.crop((x, y, x + w, y + h))
    return {"processed_image": _to_base64_png(processed)}


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    width, height = int(width), int(height)
    processed = image.resize((width, height), resample=_get_resample(interpolation))
    return {
        "processed_image": _to_base64_png(processed),
        "new_size": {"width": width, "height": height},
    }


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
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    tx, ty = int(tx), int(ty)
    width, height = image.size
    processed = Image.new(image.mode, (width, height))
    processed.paste(image, (tx, ty))
    return {"processed_image": _to_base64_png(processed)}
