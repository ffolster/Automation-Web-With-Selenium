#!/bin/bash

# Diretórios e caminhos
ARQUIVOS_TXT_DIR="~/celesc/arquivos_txt"
SCRIPTS_DIR="~/celesc/scripts"
XLSX_FILE="${SCRIPTS_DIR}/manutencoes_formatadas.xlsx"
EMAIL_DESTINO="ffolster@gmail.com,felipe@maisinternet.net.br,jakson@maisinternet.net.br,caio@maisinternet.net.br"
ASSUNTO="Manutenções CELESC"
MENSAGEM="Segue em anexo o relatório de manutenções CELESC."
ARQUIVO_ANEXO="~/celesc/scripts/manutencoes_formatadas.xlsx"
LOG_DIR="${SCRIPTS_DIR}/log"

# Criando diretório de logs, se não existir
mkdir -p "$LOG_DIR"

# Nome do log baseado na data atual
DATA=$(date +%Y-%m-%d_%H-%M-%S)  # Formato: 2024-11-23_10-30-00
LOG_FILE="${LOG_DIR}/log_${DATA}.log"

# Redireciona saída e erros para o log
exec > >(tee -a "$LOG_FILE") 2>&1

echo "===== INICIANDO PROCESSO: $(date) ====="

# Limpeza de logs antigos (mais de 15 dias)
echo "Limpando logs com mais de 15 dias no diretório: $LOG_DIR"
find "$LOG_DIR" -type f -name "log_*.log" -mtime +15 -exec rm -f {} \;
echo "Logs antigos removidos."

# 1. Limpar os arquivos .txt do diretório de textos
echo "Limpando arquivos .txt no diretório: $ARQUIVOS_TXT_DIR"
find "$ARQUIVOS_TXT_DIR" -type f -name "*.txt" -exec rm -f {} \;
echo "Arquivos .txt limpos."

# 2. Limpar o arquivo .xlsx no diretório de scripts
if [ -f "$XLSX_FILE" ]; then
    echo "Removendo arquivo .xlsx: $XLSX_FILE"
    rm -f "$XLSX_FILE"
    echo "Arquivo .xlsx removido."
else
    echo "Nenhum arquivo .xlsx encontrado para remover."
fi

# 3. Executar o script abresite.py
echo "Executando o script abresite.py..."
python3 "$SCRIPTS_DIR/abresite.py"
if [ $? -ne 0 ]; then
    echo "Erro ao executar abresite.py. Abortando."
    exit 1
fi
echo "Script abresite.py concluído."

# 4. Executar o script organiza.py
echo "Executando o script organiza.py..."
python3 "$SCRIPTS_DIR/organiza.py"
if [ $? -ne 0 ]; then
    echo "Erro ao executar organiza.py. Abortando."
    exit 1
fi
echo "Script organiza.py concluído."

echo "Processo finalizado com sucesso."

# Enviando o e-mail com anexo usando msmtp

echo "Enviando e-mail com o arquivo anexo..."

(
echo "To: $EMAIL_DESTINO"
echo "Subject: $ASSUNTO"
echo "MIME-Version: 1.0"
echo "Content-Type: multipart/mixed; boundary=\"boundary\""
echo ""
echo "--boundary"
echo "Content-Type: text/plain; charset=utf-8"
echo ""
echo "$MENSAGEM"
echo ""
echo "--boundary"
echo "Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
echo "Content-Disposition: attachment; filename=$(basename "$ARQUIVO_ANEXO")"
echo "Content-Transfer-Encoding: base64"
echo ""
base64 "$ARQUIVO_ANEXO"
echo "--boundary--"
) | msmtp "$EMAIL_DESTINO"

if [ $? -eq 0 ]; then
    echo "E-mail enviado com sucesso para $EMAIL_DESTINO."
else
    echo "Falha ao enviar o e-mail."
    exit 1
fi

echo "Processo concluído com sucesso."
