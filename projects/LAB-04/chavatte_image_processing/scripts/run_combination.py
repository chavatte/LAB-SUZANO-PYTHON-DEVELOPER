import numpy as np
import sys
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from image_processing.utils import io
from image_processing.processing.combination import find_difference, transfer_histogram

root = tk.Tk()
root.withdraw()

image1_path = filedialog.askopenfilename(title="Selecione a primeira imagem")
image2_path = filedialog.askopenfilename(title="Selecione a segunda imagem")

image1 = io.read_image(image1_path)
image2 = io.read_image(image2_path)

difference_image = find_difference(image1, image2)
difference_image_uint8 = (difference_image * 255).astype(np.uint8)

io.save_image(difference_image_uint8, "difference_image.jpg")

histogram_image = transfer_histogram(image1, image2)

histogram_image_uint8 = (histogram_image * 255).astype(np.uint8)

io.save_image(histogram_image_uint8, "histogram_image.jpg")

print("Imagens processadas e salvas com sucesso!")