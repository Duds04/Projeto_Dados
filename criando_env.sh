#!/bin/bash

# Defina o nome do ambiente virtual
AMBIENTE="TP_Dados"

# Crie o ambiente virtual
python3 -m venv $AMBIENTE

# Ative o ambiente virtual
source $AMBIENTE/bin/activate

# Mensagem para indicar que o ambiente foi ativado
echo "Ambiente virtual '$AMBIENTE' ativado."

# Aqui você pode adicionar outros comandos a serem executados após a ativação
# python3 meuArquivo.py
pip install pandas numpy matplotlib seaborn scipy unidecode ipykernel