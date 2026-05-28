# 🛒 Monitoramento de Preço Amazon com Python + Selenium

Projeto simples de automação web utilizando **Python**, **Selenium** e **ChromeDriver** para capturar automaticamente o preço de um produto na Amazon.

---

# 📌 Tecnologias utilizadas

* Python
* Selenium
* WebDriver Manager
* Google Chrome

---

# 🚀 Como o projeto funciona

O script realiza os seguintes passos:

1. Abre o navegador Google Chrome automaticamente
2. Acessa uma página de produto da Amazon
3. Aguarda o carregamento da página
4. Localiza os elementos HTML do preço
5. Captura o valor inteiro e decimal
6. Exibe o preço no terminal
7. Fecha o navegador

---

# 💻 Código do projeto

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# driver do navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# URL do produto
url = 'https://www.amazon.com.br/dp/B0DYVPCX34'

# Abrir site
driver.get(url)

# Aguarda o carregamento
time.sleep(60)

# Captura do preço
inteiro = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
decimal = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text

# Exibição do resultado
print(f'Preço: R${inteiro},{decimal}')

# Fecha o navegador
driver.quit()
```

---

# 📖 Explicação do código

## Importação das bibliotecas

```python
from selenium import webdriver
```

Controla automaticamente o navegador.

```python
from selenium.webdriver.common.by import By
```

Permite localizar elementos HTML da página.

```python
from selenium.webdriver.chrome.service import Service
```

Gerencia o ChromeDriver.

```python
from webdriver_manager.chrome import ChromeDriverManager
```

Instala automaticamente a versão correta do ChromeDriver.

```python
import time
```

Usado para adicionar pausas durante a execução.

---

# ⚙️ Instalação

## 1️⃣ Instale o Python

Acesse:

https://www.python.org/downloads/

---

## 2️⃣ Instale as bibliotecas necessárias

Abra o terminal e execute:

```bash
pip install selenium webdriver-manager
```

---

# ▶️ Como executar

No terminal:

```bash
python nome_do_arquivo.py
```

---

# ✅ Exemplo de saída

```bash
Preço: R$2.499,90
```

---

# 🎯 Objetivo do projeto

Este projeto foi criado para praticar:

* Automação Web
* Web Scraping
* Selenium
* Python
* Manipulação de elementos HTML

---

# 🔥 Melhorias futuras

* Monitoramento automático de preços
* Alertas via WhatsApp
* Envio de e-mail
* Interface gráfica
* Banco de dados
* Monitoramento de múltiplos produtos

---

# 👨‍💻 Autor

Desenvolvido por **Elcio Mello** para estudos de automação web com Python.
