#!/bin/bash

# Ativar o ambiente virtual
source TP_Dados/bin/activate

# Verificar se a ativação foi bem-sucedida
if [ $? -ne 0 ]; then
    echo "Erro ao ativar o ambiente virtual."
    exit 1
fi

# Comandos que você deseja executar após ativar o ambiente virtual
# python meu_script.py
