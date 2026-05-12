"""
Instruksi Pembuatan Function untuk Modul Image Restoration
"""

import base64
import io
import json

import numpy as np
from PIL import Image, ImageFilter


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


def gaussian(file, kernel_size, sigma=0.0):
    """
    Fungsi: Menerapkan Gaussian Blur untuk menghaluskan gambar dan mereduksi noise.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran kernel. (Wajib)
      - sigma (float): Nilai sigma Gaussian. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    if image.mode not in ("RGB", "L"):
        image = image.convert("RGB")
    radius = float(sigma) if sigma and sigma > 0 else max(0.5, int(kernel_size) / 2.0)
    processed = image.filter(ImageFilter.GaussianBlur(radius=radius))
    return {"processed_image": _to_base64_png(processed)}


def median(file, kernel_size):
    """
    Fungsi: Menerapkan Median Filter (efektif untuk noise salt & pepper).
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran kernel. (Wajib)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    if image.mode not in ("RGB", "L"):
        image = image.convert("RGB")
    processed = image.filter(ImageFilter.MedianFilter(size=int(kernel_size)))
    return {"processed_image": _to_base64_png(processed)}


def denoise_sp(file, kernel_size=3):
    """
    Fungsi: Mendeteksi dan menghilangkan noise salt & pepper secara adaptif.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel_size (integer): Ukuran window deteksi. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    if image.mode not in ("RGB", "L"):
        image = image.convert("RGB")
    processed = image.filter(ImageFilter.MedianFilter(size=int(kernel_size)))
    return {"processed_image": _to_base64_png(processed)}


def convolve(file, kernel, normalize=False):
    """
    Fungsi: Menerapkan konvolusi custom dengan kernel yang didefinisikan pengguna.
    Input:
      - file (UploadFile): Gambar yang akan diproses. (Wajib)
      - kernel (string): Matriks kernel 2D dalam format JSON. (Wajib)
      - normalize (boolean): Jika true, kernel dibagi jumlah absolutnya. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - processed_image (string base64): Gambar hasil diencoding PNG base64.
    """
    data = _read_upload_file(file)
    image = Image.open(io.BytesIO(data))
    if image.mode not in ("RGB", "L"):
        image = image.convert("RGB")

    if isinstance(kernel, str):
        kernel = json.loads(kernel)
    kernel_arr = np.array(kernel, dtype=float)
    if kernel_arr.ndim != 2:
        raise ValueError("Kernel harus matriks 2D")

    if normalize:
        total = np.sum(np.abs(kernel_arr))
        if total != 0:
            kernel_arr = kernel_arr / total

    image_arr = np.array(image, dtype=float)
    if image_arr.ndim == 2:
        image_arr = image_arr[:, :, None]

    pad_h, pad_w = kernel_arr.shape[0] // 2, kernel_arr.shape[1] // 2
    padded = np.pad(image_arr, ((pad_h, pad_h), (pad_w, pad_w), (0, 0)), mode="edge")
    output = np.zeros_like(image_arr)

    for y in range(image_arr.shape[0]):
        for x in range(image_arr.shape[1]):
            region = padded[y : y + kernel_arr.shape[0], x : x + kernel_arr.shape[1], :]
            output[y, x, :] = np.sum(region * kernel_arr[:, :, None], axis=(0, 1))

    output = np.clip(output, 0, 255).astype(np.uint8)
    if output.shape[2] == 1:
        output = output[:, :, 0]
    processed = Image.fromarray(output)
    return {"processed_image": _to_base64_png(processed)}
