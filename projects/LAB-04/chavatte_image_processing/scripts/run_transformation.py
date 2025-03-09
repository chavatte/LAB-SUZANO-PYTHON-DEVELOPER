import numpy as np
import sys
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image  # Importe a classe Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from image_processing.utils import io
from image_processing.processing.transformation import resize_image

root = tk.Tk()
root.withdraw()

image_path = filedialog.askopenfilename(title="Selecione a imagem")

image = io.read_image(image_path)

resized_image = resize_image(image, 0.5)

resized_image_uint8 = (resized_image * 255).astype(np.uint8)

# Converter para RGB antes de salvar como JPEG
resized_image_pil = Image.fromarray(resized_image_uint8)
resized_image_rgb = resized_image_pil.convert('RGB')

# Salvar a imagem convertida
resized_image_rgb.save("resized_image.jpg")

print("Imagem redimensionada e salva com sucesso!")