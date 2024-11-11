# Automation-Web-With-Selenium

Extração de dados do site da CELESC (Operadora de energia do estado de SC), organização em uma planilha e envio automático via email.

1 - O arquivo abresite.py acessa um site especifico, navega por ele, e extrai a informação necessária, que será salvo em um arquivo .txt, essas partes do código devem ser customizadas.

2 - Com o arquivo .txt devidamente gerado, executa-se o código organizador.py, que lê o arquivo .txt e organiza toda a estrutura em uma planilha excel, através de seu loop e seu regex exlusivo para o arquivo em questão.

3 - Com o arquivo .xlsx gerado, enviamos, por exemplo, automaticamente por email aos interessados. Falta desencolver essa parte da automação
