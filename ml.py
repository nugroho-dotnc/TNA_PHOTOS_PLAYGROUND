"""
Instruksi Pembuatan Function untuk Modul ML / CNN Object Detection
"""

def predict(file, conf_threshold, classes=None):
    """
    Fungsi: Menjalankan inferensi YOLOv8 pada gambar untuk mendeteksi objek.
    Input:
      - file (UploadFile): Gambar input. (Wajib)
      - conf_threshold (float): Threshold confidence minimum (0.0-1.0). (Wajib)
      - classes (string): Filter kelas COCO dalam format JSON array. (Opsional)
    Return:
      - JSON/Dict dengan field:
        - annotated_image (string base64): Gambar dengan bounding box dioverlay diencoding PNG base64.
        - detections (array): Array hasil deteksi (label, confidence, bbox).
    """
    pass

def classes():
    """
    Fungsi: Mengembalikan daftar nama kelas yang didukung oleh model YOLOv8 (COCO dataset).
    Input: Tidak ada.
    Return:
      - JSON/Dict dengan field:
        - classes (array): Daftar nama kelas COCO (string).
    """
    pass
