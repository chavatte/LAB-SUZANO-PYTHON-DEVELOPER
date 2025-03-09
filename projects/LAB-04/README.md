# LAB-04: Processamento de Imagens em Python

## [chavatte-image-processing] - Sistema de Processamento de Imagens

[`chavatte-image-processing`](https://pypi.org/project/chavatte-image-processing/) é uma biblioteca Python para processamento de imagens com funcionalidades como redimensionamento, combinação de imagens e transferência de histograma.

## Descrição

Este projeto implementa funcionalidades de processamento de imagens utilizando Python, com foco em operações de combinação e transformação.

O `chavatte-image-processing` oferece um conjunto de ferramentas para manipular imagens, incluindo:

* **Combinação:**
    * Encontrar a diferença estrutural entre duas imagens.
    * Transferir o histograma de uma imagem para outra.
* **Transformação:**
    * Redimensionar imagens.

## Tecnologias Utilizadas

* Python
* scikit-image
* Pillow (PIL)
* NumPy
* networkx
* cycler
* kiwisolver

## Aprendizado

O desenvolvimento deste projeto proporcionou o aprendizado em diversas áreas, tais como:

* **Lógica de processamento de imagens:** Implementação de algoritmos para encontrar diferenças entre imagens, transferir histogramas e redimensionar imagens.
* **Manipulação de arrays NumPy:** Utilização de arrays NumPy para representar e manipular imagens.
* **Utilização de bibliotecas de processamento de imagens:** Aprendizado do uso de bibliotecas como scikit-image e Pillow para realizar operações de processamento de imagens.
* **Manipulação de arquivos de imagem:** Leitura e escrita de arquivos de imagem em diferentes formatos.
* **Empacotamento de projetos Python com `setup.py`:** Criação de um pacote Python instalável.
* **Boas práticas de desenvolvimento:** Aplicação de boas práticas de desenvolvimento, como organização do código e nomenclatura clara.


## Funcionalidades

| O pacote `chavatte-image-processing` é utilizado para: |
| :---------------------------------- |
| -   Encontrar a diferença entre imagens. |
| -   Transferir o histograma de imagens. |
| -   Redimensionar imagens.           |
| -   Visualizar imagens.              |

## Instalação

### Opção 1: Instalação via pip (Recomendado)

Você pode instalar o pacote usando o pip:

**Bash**

```
pip install chavatte-image-processing
```

### Opção 2: Instalação a partir do arquivo `requirements.txt` (Alternativa)

Se você preferir instalar as dependências manualmente, você pode usar o arquivo `requirements.txt` fornecido no repositório:

* 1. Clone o repositório para o seu computador:

**Bash**

```
   git clone https://github.com/chavatte/LAB-SUZANO-PYTHON-DEVELOPER
   cd projects\LAB-04\chavatte_image_processing
```

* 2. Instale as dependências usando o pip e o arquivo requirements.txt:

**Bash**

```
pip install -r requirements.txt
```

**Escolha a Opção Mais Adequada:**

* **Recomendado:** A primeira opção (instalação via pip) é a mais simples e direta para a maioria dos usuários.
* **Alternativa:** A segunda opção (instalação com `requirements.txt`) é útil em situações específicas, como quando você precisa instalar as dependências manualmente.


## Exemplo de Uso (biblioteca):

Aqui estão alguns exemplos de como usar as funcionalidades da biblioteca

### Redimensionar uma imagem

**Bash**

```
from chavatte_image_processing import transformation
from chavatte_image_processing import io

# Carrega a imagem
image = io.read_image("caminho/para/sua/imagem.jpg")

# Redimensiona a imagem para 50% do tamanho original
resized_image = transformation.resize_image(image, 0.5)

# Salva a imagem redimensionada
io.save_image(resized_image, "imagem_redimensionada.jpg")
```

### Encontrar a diferença entre duas imagens

**Bash**

```
from chavatte_image_processing import combination
from chavatte_image_processing import io

# Carrega as imagens
image1 = io.read_image("caminho/para/imagem1.jpg")
image2 = io.read_image("caminho/para/imagem2.jpg")

# Encontra a diferença entre as imagens
difference_image = combination.find_difference(image1, image2)

# Salva a imagem de diferença
io.save_image(difference_image, "imagem_diferenca.jpg")
```

### Transferir o histograma de uma imagem para outra

**Bash**

```
from chavatte_image_processing import combination
from chavatte_image_processing import io

# Carrega as imagens
image1 = io.read_image("caminho/para/imagem1.jpg")
image2 = io.read_image("caminho/para/imagem2.jpg")

# Transfere o histograma da imagem 2 para a imagem 1
histogram_image = combination.transfer_histogram(image1, image2)

# Salva a imagem com o histograma transferido
io.save_image(histogram_image, "imagem_histograma.jpg")
```

## Executando os Scripts

### Scripts de Linha de Comando:

Você pode executar os scripts `run_combination.py` e `run_transformation.py` para realizar operações específicas na linha de comando.

**Bash**

```
#Este script permite encontrar a diferença entre duas imagens e transferir o histograma.
python scripts/run_combination.py
````

**Bash**

```
# Este script permite redimensionar uma imagem.
python scripts/run_transformation.py
````

### Exemplo de Uso (Código):
Aqui está um exemplo de como usar as funções do pacote `chavatte-image-processing` diretamente no seu código:

**Bash**

```
from image_processing.utils import io
from image_processing.processing.combination import find_difference, transfer_histogram
from image_processing.processing.transformation import resize_image

# Carregar imagens
image1 = io.read_image("imagem1.jpg")
image2 = io.read_image("imagem2.jpg")

# Encontrar a diferença
difference_image = find_difference(image1, image2)
io.save_image(difference_image, "diferenca.jpg")

# Transferir histograma
histogram_image = transfer_histogram(image1, image2)
io.save_image(histogram_image, "histograma_transferido.jpg")

# Redimensionar imagem
resized_image = resize_image(image1, 0.5)
io.save_image(resized_image, "imagem_redimensionada.jpg")
```

## Autor
João Carlos Chavatte(DEV Chavatte)

## Licença
MIT