import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Inicializa o navegador Chrome
navegador = webdriver.Chrome()

# Abre o site específico da Celesc
navegador.get('https://www.celesc.com.br/avisos-de-desligamentos')

# Troca o contexto para o iframe que contém os elementos necessários
iframe = WebDriverWait(navegador, 10).until(
    EC.presence_of_element_located((By.ID, 'blockrandom-161'))
)
navegador.switch_to.frame(iframe)

# Lista de municípios a serem processados
municipios = ["PALHOCA", "SANTO AMARO DA IMPERATRIZ", "GAROPABA", "AGUAS MORNAS", "FLORIANOPOLIS", "SAO JOSE",
              "SAO PEDRO DE ALCANTARA"]

# Caminho onde os arquivos serão salvos
pasta_destino = r'C:\Users\Felipe Folster\PycharmProjects\pythonProject\venv\Scripts\Arquivos_txt'

# Certifique-se de que a pasta existe, ou crie-a
os.makedirs(pasta_destino, exist_ok=True)

for municipio in municipios:
    try:
        # Localiza o elemento <select> e o inicializa como um objeto Select
        select_element = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.NAME, 'munic'))
        )
        select = Select(select_element)

        # Verifica se a opção está disponível no dropdown
        opcoes = [opt.text for opt in select.options]
        if municipio not in opcoes:
            print(f"Município {municipio} não disponível. Pulando.")
            continue

        # Seleciona a opção do município atual
        select.select_by_visible_text(municipio)

        # Aguarda o botão de envio estar disponível e usa JavaScript para forçar o clique
        submit_button = WebDriverWait(navegador, 10).until(
            EC.element_to_be_clickable((By.NAME, 'Submit'))
        )
        navegador.execute_script("arguments[0].click();", submit_button)

        # Aguarda o elemento <pre> que contém os dados ser carregado
        element = WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, 'pre'))
        )

        # Cria um arquivo de texto específico para o município atual
        arquivo_caminho = os.path.join(pasta_destino, f'{municipio.lower().replace(" ", "_")}.txt')
        with open(arquivo_caminho, 'w', encoding="utf-8") as arquivo:
            arquivo.write(element.text)

        # Recarrega a página e redefine o iframe
        navegador.refresh()
        navegador.switch_to.frame(WebDriverWait(navegador, 10).until(
            EC.presence_of_element_located((By.ID, 'blockrandom-161'))
        ))

    except TimeoutException as e:
        print(f"Erro ao processar {municipio}: {e}")
    except NoSuchElementException as e:
        print(f"Erro ao localizar elemento para {municipio}: {e}")

# Fecha o navegador após processar todos os municípios
navegador.quit()

'''	
                    #Opções de extração de dados
                    
<option value="AGROLANDIA">AGROLANDIA</option>
<option value="AGRONOMICA">AGRONOMICA</option>
<option value="AGUAS MORNAS">AGUAS MORNAS</option>
<option value="ALFREDO WAGNER">ALFREDO WAGNER</option>
<option value="ANCHIETA">ANCHIETA</option>
<option value="ANITA GARIBALDI">ANITA GARIBALDI</option>
<option value="ANTONIO CARLOS">ANTONIO CARLOS</option>
<option value="APIUNA">APIUNA</option>
<option value="ARABUTA">ARABUTA</option>
<option value="ARAQUARI">ARAQUARI</option>
<option value="ARARANGUA">ARARANGUA</option>
<option value="ARROIO TRINTA">ARROIO TRINTA</option>
option value="ASCURRA">ASCURRA</option>
<option value="AURORA">AURORA</option>
<option value="BALN. GAIVOTA">BALN. GAIVOTA</option>
<option value="BALN. PICARRAS">BALN. PICARRAS</option>
<option value="BALNEARIO ARROIO DO SILVA">BALNEARIO ARROIO DO SILVA</option>
<option value="BALNEARIO BARRA DO SUL">BALNEARIO BARRA DO SUL</option>
<option value="BALNEARIO CAMBORIU">BALNEARIO CAMBORIU</option>
<option value="BANDEIRANTE">BANDEIRANTE</option>
<option value="BARRA BONITA">BARRA BONITA</option>
<option value="BARRA VELHA">BARRA VELHA</option>
<option value="BELA VISTA DO TOLDO">BELA VISTA DO TOLDO</option>
<option value="BENEDITO NOVO">BENEDITO NOVO</option>
<option value="BIGUACU">BIGUACU</option>
<option value="BLUMENAU">BLUMENAU</option>
<option value="BOMBINHAS">BOMBINHAS</option>
<option value="BOTUVERA">BOTUVERA</option>
<option value="BRUSQUE">BRUSQUE</option>
<option value="CACADOR">CACADOR</option>
<option value="CALMON">CALMON</option>
<option value="CAMBORIU">CAMBORIU</option>
<option value="CAMPO ALEGRE">CAMPO ALEGRE</option>
<option value="CANELINHA">CANELINHA</option>
<option value="CELSO RAMOS">CELSO RAMOS</option>
<option value="CHAPECO">CHAPECO</option>
<option value="CONCORDIA">CONCORDIA</option>
<option value="CORONEL FREITAS">CORONEL FREITAS</option>
<option value="CORREIA PINTO">CORREIA PINTO</option>
<option value="CORUPA">CORUPA</option>
<option value="CRICIUMA">CRICIUMA</option>
<option value="CUNHA PORA">CUNHA PORA</option>
<option value="CURITIBANOS">CURITIBANOS</option>
<option value="DIONISIO CERQUEIRA">DIONISIO CERQUEIRA</option>
<option value="FAXINAL DOS GUEDES">FAXINAL DOS GUEDES</option>
<option value="FLOR DO SERTAO">FLOR DO SERTAO</option>
<option value="FLORIANOPOLIS">FLORIANOPOLIS</option>
<option value="FRAIBURGO">FRAIBURGO</option>
<option value="GASPAR">GASPAR</option>
<option value="GOVERNADOR CELSO RAMOS">GOVERNADOR CELSO RAMOS</option>
<option value="GUABIRUBA">GUABIRUBA</option>
<option value="GUARACIABA">GUARACIABA</option>
<option value="GUARAMIRIM">GUARAMIRIM</option>
<option value="GUARUJA DO SUL">GUARUJA DO SUL</option>
<option value="HERVAL D'OESTE">HERVAL D'OESTE</option>
<option value="IBIRAMA">IBIRAMA</option>
<option value="ILHOTA">ILHOTA</option>
<option value="IMBITUBA">IMBITUBA</option>
<option value="INDAIAL">INDAIAL</option>
<option value="IOMERE">IOMERE</option>
<option value="IPORA DO OESTE">IPORA DO OESTE</option>
<option value="IPUMIRIM">IPUMIRIM</option>
<option value="IRACEMINHA">IRACEMINHA</option>
<option value="IRINEOPOLIS">IRINEOPOLIS</option>
<option value="ITA">ITA</option>
<option value="ITAIOPOLIS">ITAIOPOLIS</option>
<option value="ITAJAI">ITAJAI</option>
<option value="ITAPEMA">ITAPEMA</option>
<option value="ITAPIRANGA">ITAPIRANGA</option>
<option value="ITAPOA">ITAPOA</option>
<option value="ITUPORANGA">ITUPORANGA</option>
<option value="JABORA">JABORA</option>
<option value="JARAGUA DO SUL">JARAGUA DO SUL</option>
<option value="JOACABA">JOACABA</option>
<option value="JOINVILLE">JOINVILLE</option>
<option value="JUPIA">JUPIA</option>
<option value="LAGES">LAGES</option>
<option value="LAGUNA">LAGUNA</option>
<option value="LAURO MULLER">LAURO MULLER</option>
<option value="LINDOIA DO SUL">LINDOIA DO SUL</option>
<option value="LONTRAS">LONTRAS</option>
<option value="LUIZ ALVES">LUIZ ALVES</option>
<option value="MAFRA">MAFRA</option>
<option value="MAJOR GERCINO">MAJOR GERCINO</option>
<option value="MAJOR VIEIRA">MAJOR VIEIRA</option>
<option value="MARAVILHA">MARAVILHA</option>
<option value="MASSARANDUBA">MASSARANDUBA</option>
<option value="MATOS COSTA">MATOS COSTA</option>
<option value="MONTE CASTELO">MONTE CASTELO</option>
<option value="NAVEGANTES">NAVEGANTES</option>
<option value="NOVA TRENTO">NOVA TRENTO</option>
<option value="NOVA VENEZA">NOVA VENEZA</option>
<option value="ORLEANS">ORLEANS</option>
<option value="OTACILIO COSTA">OTACILIO COSTA</option>
<option value="PAIAL">PAIAL</option>
<option value="PALHOCA">PALHOCA</option>
<option value="PALMEIRA">PALMEIRA</option>
<option value="PALMITOS">PALMITOS</option>
<option value="PAPANDUVA">PAPANDUVA</option>
<option value="PARAISO">PARAISO</option>
<option value="PASSOS MAIA">PASSOS MAIA</option>
<option value="PENHA">PENHA</option>
<option value="PERITIBA">PERITIBA</option>
<option value="PETROLANDIA">PETROLANDIA</option>
<option value="PINHEIRO PRETO">PINHEIRO PRETO</option>
<option value="PONTE ALTA">PONTE ALTA</option>
<option value="PONTE ALTA DO NORTE">PONTE ALTA DO NORTE</option>
<option value="PORTO BELO">PORTO BELO</option>
<option value="PORTO UNIAO">PORTO UNIAO</option>
<option value="POUSO REDONDO">POUSO REDONDO</option>
<option value="PRESIDENTE NEREU">PRESIDENTE NEREU</option>
<option value="PRINCESA">PRINCESA</option>
<option value="RANCHO QUEIMADO">RANCHO QUEIMADO</option>
<option value="RIO DAS ANTAS">RIO DAS ANTAS</option>
<option value="RIO DO CAMPO">RIO DO CAMPO</option>
<option value="RIO DO OESTE">RIO DO OESTE</option>
<option value="RIO DO SUL">RIO DO SUL</option>
<option value="RIO DOS CEDROS">RIO DOS CEDROS</option>
<option value="RIO NEGRINHO">RIO NEGRINHO</option>
<option value="RIO NEGRO - PR">RIO NEGRO - PR</option>
<option value="RODEIO">RODEIO</option>
<option value="ROMELANDIA">ROMELANDIA</option>
<option value="S.FRANCISCO DO SUL">S.FRANCISCO DO SUL</option>
<option value="SALETE">SALETE</option>
<option value="SANTA CECILIA">SANTA CECILIA</option>
<option value="SANTA HELENA">SANTA HELENA</option>
<option value="SANTA ROSA DO SUL">SANTA ROSA DO SUL</option>
<option value="SANTA TEREZINHA">SANTA TEREZINHA</option>
<option value="SANTO AMARO DA IMPERATRIZ" selected="selected">SANTO AMARO DA IMPERATRIZ</option>
<option value="SAO BENTO DO SUL">SAO BENTO DO SUL</option>
<option value="SAO BERNARDINO">SAO BERNARDINO</option>
<option value="SAO CRISTOVAO DO SUL">SAO CRISTOVAO DO SUL</option>
<option value="SAO JOAO BATISTA">SAO JOAO BATISTA</option>
<option value="SAO JOAO DO ITAPERIU">SAO JOAO DO ITAPERIU</option>
<option value="SAO JOAO DO OESTE">SAO JOAO DO OESTE</option>
<option value="SAO JOAQUIM">SAO JOAQUIM</option>
<option value="SAO JOSE">SAO JOSE</option>
<option value="SAO JOSE DO CEDRO">SAO JOSE DO CEDRO</option>
<option value="SAO JOSE DO CERRITO">SAO JOSE DO CERRITO</option>
<option value="SAO LOURENCO DO OESTE">SAO LOURENCO DO OESTE</option>
<option value="SAO MIGUEL DO OESTE">SAO MIGUEL DO OESTE</option>
<option value="SAO PEDRO DE ALCANTARA">SAO PEDRO DE ALCANTARA</option>
<option value="SCHROEDER">SCHROEDER</option>
<option value="SEARA">SEARA</option>
<option value="SOMBRIO">SOMBRIO</option>
<option value="TAIO">TAIO</option>
<option value="TANGARA">TANGARA</option>
<option value="TIJUCAS">TIJUCAS</option>
<option value="TIMBO">TIMBO</option>
<option value="TIMBO GRANDE">TIMBO GRANDE</option>
<option value="TRES BARRAS">TRES BARRAS</option>
<option value="TROMBUDO CENTRAL">TROMBUDO CENTRAL</option>
<option value="TUBARAO">TUBARAO</option>
<option value="TUNAPOLIS">TUNAPOLIS</option>
<option value="URUBICI">URUBICI</option>
<option value="URUPEMA">URUPEMA</option>
<option value="VARGEAO">VARGEAO</option>
<option value="VIDAL RAMOS">VIDAL RAMOS</option>
<option value="VIDEIRA">VIDEIRA</option>
'''
