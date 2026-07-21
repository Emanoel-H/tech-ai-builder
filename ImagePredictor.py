import os
import tkinter as tk
from tkinter import filedialog

import cv2
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    decode_predictions,
    preprocess_input,
)


def selecionar_imagem():
    """Abre uma janela do sistema operacional para escolher uma imagem."""
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do tkinter
    root.attributes("-topmost", True)  # Traz a janela de seleção para frente

    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=[
            ("Imagens", "*.jpg *.jpeg *.png *.bmp *.webp"),
            ("Todos os arquivos", "*.*"),
        ],
    )
    return caminho_arquivo


def main():
    # 1. Selecionar o arquivo localmente
    print("Aguardando seleção do arquivo...")
    imagem_path = selecionar_imagem()

    if not imagem_path:
        print("Nenhum arquivo foi selecionado. Encerrando.")
        return

    # 2. Carregar e tratar a imagem
    imagem = cv2.imread(imagem_path)

    if imagem is None:
        print(
            "Erro ao carregar a imagem. Verifique se o caminho não contém caracteres especiais."
        )
        return

    imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

    # 3. Carregar o modelo pré-treinado
    print("Carregando o modelo MobileNetV2...")
    modelo = MobileNetV2(weights="imagenet")

    # 4. Pré-processamento
    imagem_redimensionada = cv2.resize(imagem_rgb, (224, 224))
    imagem_array = np.expand_dims(imagem_redimensionada, axis=0)
    imagem_array = preprocess_input(imagem_array)

    # 5. Predição
    print("Classificando imagem...")
    predicoes = modelo.predict(imagem_array)
    rotulos = decode_predictions(predicoes, top=3)[0]

    # 6. Exibir Resultados
    print("\n" + "=" * 30)
    print(f"Objeto principal: {rotulos[0][1]} ({rotulos[0][2]*100:.2f}%)")
    print("=" * 30)

    print("\nTop 3 palpites do modelo:")
    for i, (imagenet_id, classe, probabilidade) in enumerate(rotulos):
        print(f"{i+1}. {classe}: {probabilidade*100:.2f}%")

    if __name__ == "__main__":
        main()