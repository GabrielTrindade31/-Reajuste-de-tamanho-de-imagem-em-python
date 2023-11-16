from PIL import Image

# Abre a imagem
imagem = Image.open("vs_code_python\.vscode\Controle3.png")
print("Para aumentar a imagem digite 1, para diminuir a imagem digite 2:")
tamanho = int(input())
if tamanho == 1:
    print("quanto quer aumentar em porcentagem ?")
    # Obtém as dimensões da imagem original
    largura_original, altura_original = imagem.size2
    porcentagem = (int(input())+100)/100
    nova_largura = int(largura_original * (porcentagem))
    nova_altura = int(altura_original * (porcentagem))
    # Redimensiona a imagem usando o método resize()
    nova_imagem = imagem.resize((nova_largura, nova_altura))
if tamanho == 2:
    print("quanto quer diminuir em porcentagem ?")
    # Obtém as dimensões da imagem original
    largura_original, altura_original = imagem.size
    porcentagem = abs(int(input())-100)/100
    nova_largura = int(largura_original * (porcentagem))
    nova_altura = int(altura_original * (porcentagem))
    # Redimensiona a imagem usando o método resize()
    nova_imagem = imagem.resize((nova_largura, nova_altura))
# Salva a nova imagem
nova_imagem.save("vs_code_python\.vscode\imagem_nova.png")
