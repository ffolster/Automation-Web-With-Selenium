from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Inicializa o navegador Chrome
navegador = webdriver.Chrome()

# Abre o site específico da Celesc
navegador.get('https://www.celesc.com.br/avisos-de-desligamentos')

# Troca o contexto para o iframe que contém os elementos necessários
navegador.switch_to.frame(navegador.find_element(By.ID, 'blockrandom-161'))

# Aguarda 2 segundos para garantir que o iframe seja carregado (não recomendado; veja WebDriverWait)
time.sleep(2)

# Localiza o elemento <select> pelo atributo 'name' e o inicializa como um objeto Select
select = Select(navegador.find_element(By.NAME, 'munic'))

# Aguarda 1 segundo antes de interagir com o <select>
time.sleep(1)

# Seleciona a opção "PALHOCA" no dropdown
select.select_by_visible_text('PALHOCA')

# Aguarda 3 segundos para garantir que a página seja atualizada
time.sleep(3)

# Clica no botão de envio para submeter o formulário
navegador.find_element(By.NAME, 'Submit').click()

# Aguarda 3 segundos para que os resultados sejam carregados
time.sleep(3)

# Localiza o elemento <pre> que contém os dados desejados
element = navegador.find_element(By.TAG_NAME, 'pre')

# Aguarda 1 segundo antes de prosseguir
time.sleep(1)

# Abre (ou cria) um arquivo de texto no modo escrita com codificação UTF-8
arquivo = open('Celesc.txt', 'w', encoding="utf-8")

# Escreve o conteúdo do elemento <pre> no arquivo
print(element.text, file=arquivo)

# Fecha o arquivo após salvar os dados
arquivo.close()

# Aguarda 3 segundos antes de fechar o navegador
time.sleep(3)

# Fecha o navegador
navegador.close()
