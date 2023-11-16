from PIL import Image
import numpy as np
import cv2

# Abre a imagem
imagem = cv2.imread("vs_code_python\.vscode\controle3.jpg")

# Converte a imagem para escala de cinza
gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Aplica o detector de bordas Canny
edges = cv2.Canny(gray, 100, 200)

# Encontra os contornos das bordas
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Cria uma máscara com os contornos encontrados
mask = np.zeros(imagem.shape[:2], np.uint8)
cv2.drawContours(mask, contours, -1, 255, -1)

# Aplica a máscara na imagem original
res = cv2.bitwise_and(imagem, imagem, mask=mask)

# Salva a imagem resultante em formato PNG
cv2.imwrite("vs_code_python\.vscode\imagem_sem_fundo.png", res)
